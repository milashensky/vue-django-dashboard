<template lang="html">
    <modal :backdrop="true" @backdrop="$emit('close')">
        <div class="valign-wrapper h-100">
            <div class="center-align w-100">
                <h4>Details of {{ item.name }}</h4>
                <p>ID: {{ item.id }}</p>
                <p>NAME: {{ item.name }}</p>
                <p>ITEM NAME: {{ item.itemName }}</p>
                <p>PRICE: {{ item.price }}</p>
                <div class="row">
                    <router-link class="btn blue mr-3" :to="{ name: 'Item Detail', params: { id: item.id }}">Edit</router-link>
                    <button class="btn red mr-3" @click="deleteItem(item.id)">Delete</button>
                </div>
            </div>
        </div>
    </modal>
</template>

<script>
    import Modal from '../../components/Modal.vue'

    export default {
        props: [
            'item'
        ],
        methods: {
            deleteItem: function(id) {
                this.$resource('/api/item{/id}/').delete({id}).then(resp => {
                    this.$parent.$emit('delete-item', this.item);
                    this.$emit('close');
                    M.toast({html: 'Successfuly deleted.', classes: 'red' })
                });
            }
        },
        components: {
            Modal,
        }
    }
</script>
