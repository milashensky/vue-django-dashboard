from django.urls import path, re_path

from common.views import IndexView
from common.api import ItemDetail, ItemsList


urlpatterns = [
    re_path(r'^api/items', ItemsList.as_view(), name="items_api"),
    re_path(r'^api/item/(?P<pk>\d+)/$', ItemDetail.as_view(), name="item_api"),

    re_path(r'^', IndexView.as_view(), name="index"),
]
