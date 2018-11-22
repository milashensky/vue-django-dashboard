<template>
    <div>
        <add-modal v-if="showAddModal" @close="showAddModal = false"></add-modal>
        <detail-modal v-if="selectedItem" :item="selectedItem" @close="selectedItem = '';"></detail-modal>
        <h3>Dashboard <a class="btn right grey darken-2" @click="showAddModal = true">Add +</a></h3>
        <table class="striped responsive-table">
            <thead>
                <tr>
                    <th>Name</th>
                    <th>Item Name</th>
                    <th>Item Price</th>
                </tr>
            </thead>
            <tbody>
                <tr v-if="items.length" v-for="item in items" class="hoverable" @click="selectedItem = item">
                    <td>{{ item.name }}</td>
                    <td>{{ item.itemName }}</td>
                    <td>{{ item.price }}</td>
                </tr>
                <tr v-if="!items.length">
                    <td colSpan="3" class="center-align">Empty</td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<script>
import AddModal from './Modals/AddModal.vue'
import DetailModal from './Modals/DetailModal.vue'
export default {
    methods: {
        getItems: function() {
            let vm = this;
            this.$resource('/api/items').get().then(resp => {
                vm.items = resp.body.map(x => {
                    return {
                        name: x.fields.name,
                        price: x.fields.price,
                        itemName: x.fields.item_name,
                        id: x.pk
                    }
                });
            })
        }
    },
    computed: {

    },
    data: () => {
        return {
            showAddModal: false,
            items: [],
            selectedItem: '',
        }
    },
    created: function(){
        this.getItems();
        this.$on('new-item', function(item) {
            this.items.push(item);
        });
        this.$on('delete-item', function(item) {
            let ind = this.items.find(x=> x && x.id == item.id)
            if (ind)
                this.items.splice(this.items.indexOf(ind), 1)
            else
                this.getItems();
        });
    },
    components: {
        AddModal,
        DetailModal
    }
}
</script>
