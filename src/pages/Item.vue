<template lang="html">
    <div>
        <h4>Edit {{ item && item.name }}</h4>
        <div class="row">
            <form class="col s12" @submit.prevent="updateItem">
                <div class="row" :id="id">
                    <div class="input-field col s12 m6">
                        <input type="text" id="name" :class="(errors && errors.name? 'invalid': 'valid')" v-model="item.name"/>
                        <label htmlFor="name">Name</label>
                        <p class="red-text text-darken-1" v-if="errors && errors.name" v-for="error in errors.name">{{ error }}</p>
                    </div>
                    <div class="input-field col s12 m6">
                        <input type="text" id="item_name" :class="(errors && errors.item_name? 'invalid': 'valid')" v-model="item.itemName"/>
                        <label htmlFor="item_name">Item Name</label>
                        <p class="red-text text-darken-1" v-if="errors && errors.item_name" v-for="error in errors.item_name">{{ error }}</p>
                    </div>
                    <div class="input-field col s12 m6">
                        <input type="text" id="price" :class="(errors && errors.price? 'invalid': 'valid')" v-model="item.price"/>
                        <label htmlFor="price">Price</label>
                        <p class="red-text text-darken-1" v-if="errors && errors.price" v-for="error in errors.price">{{ error }}</p>
                    </div>
                </div>
                <button type="submit" class="btn blue lighten-1">Save</button>
            </form>
        </div>
    </div>
</template>

<script>
export default {
    data: function () {
        return {
            item: {},
            errors: {},
        }
    },
    computed:{
        id: function () {
            let id = this.$route.params.id;
            this.getItem(id);
            return id;
        }
    },
    methods: {
        updateItem: function () {
            let item = JSON.parse(JSON.stringify(this.item));
            item.item_name = item.itemName;
            this.$resource('/api/item{/id}/').update({id: this.id}, item).then(resp => {
                if (resp.body.errors) {
                    this.errors = resp.body.errors
                } else {
                    this.errors = {}
                    M.toast({html: 'Successfuly saved.', classes: 'green' })
                }
            })
        },
        getItem: function (id) {
            this.$resource('/api/item{/id}/').get({id}).then(resp => {
                this.item = resp.body;
                setTimeout(function () {
                    M.updateTextFields();
                }, 200);
            }).catch((a) => {
                this.$router.push('/dashboard');
            })
        }
    },
}
</script>

<style lang="css">
</style>
