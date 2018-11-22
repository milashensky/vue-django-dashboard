<template lang="html">
    <modal :backdrop="true" @backdrop="$emit('close')">
        <h4>Add new item</h4>
        <div class="row">
            <form class="col s12" @submit.prevent="addItem">
                <div class="row">
                    <div class="input-field col s12 m6">
                        <input type="text" id="name" :class="(errors && errors.name? 'invalid': 'valid')" v-model="form.name"/>
                        <label htmlFor="name">Name</label>
                        <p class="red-text text-darken-1" v-if="errors && errors.name" v-for="error in errors.name">{{ error }}</p>
                    </div>
                    <div class="input-field col s12 m6">
                        <input type="text" id="item_name" :class="(errors && errors.item_name? 'invalid': 'valid')" v-model="form.item_name"/>
                        <label htmlFor="item_name">Item Name</label>
                        <p class="red-text text-darken-1" v-if="errors && errors.item_name" v-for="error in errors.item_name">{{ error }}</p>
                    </div>
                    <div class="input-field col s12 m6">
                        <input type="text" id="price" :class="(errors && errors.price? 'invalid': 'valid')" v-model="form.price"/>
                        <label htmlFor="price">Price</label>
                        <p class="red-text text-darken-1" v-if="errors && errors.price" v-for="error in errors.price">{{ error }}</p>
                    </div>
                </div>
                <button type="submit" class="btn blue lighten-1">Add</button>
            </form>
        </div>
    </modal>
</template>

<script>
    import Modal from '../../components/Modal.vue'

    export default {
        data: function(){
            return{
                form: {},
                errors: {},
            }
        },
        methods: {
            addItem: function() {
                let vm = this;
                this.$resource('/api/items').save(vm.form).then(resp => {
                    if (resp.body.status == true) {
                        vm.errors = {};
                        this.$parent.$emit('new-item', resp.body.item)
                        M.toast({html: 'Successfuly added.', classes: 'green' })
                        this.$emit('close');
                    } else {
                        vm.errors = resp.body.errors || {}
                    }
                }).catch((a) => {
                    M.toast({html: 'Error! Try again.', classes: 'red' })
                })
            }
        },
        components: {
            Modal,
        }
    }
</script>
