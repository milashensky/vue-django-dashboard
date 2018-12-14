from django.views.generic import View
from django.shortcuts import get_object_or_404

from rest_framework.decorators import api_view
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.response import Response

from common.serializers import ItemSerializer

from common.mixins import ApiMixin, LoginRequiredMixin
from common.models import Item
from common.forms import ItemForm


@api_view(['GET'])
def api_root(request, format=None):
    """
    The entry endpoint of our API.
    """
    return Response({
        'users': reverse('user-list', request=request),
        'groups': reverse('group-list', request=request),
    })


class ItemDetail(RetrieveUpdateDestroyAPIView):
    model = Item
    serializer_class = ItemSerializer


    def get_queryset(self, *args, **kwargs):
        return Item.objects.filter(pk=self.kwargs.get('pk'), owner=self.request.user)


class ItemsList(ListCreateAPIView):
    model = Item
    serializer_class = ItemSerializer

    def get_queryset(self, *args, **kwargs):
        return Item.objects.filter(owner=self.request.user)

    def post(self, request, *args, **kwargs):
        self.data = request.data
        self.data['owner'] = request.user.pk
        form = ItemForm(self.data)
        if form.is_valid():
            item = form.save()
            return Response({
                "status": True,
                "item": {
                    "id": item.pk,
                    "itemName": item.item_name,
                    "price": item.price,
                    "name": item.name
                }
            })
        return Response({"state": False, "errors": form.errors})
