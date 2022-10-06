<template>
    <div class="cards_container">
        <div class="cards_content">
            <h1>Cards</h1>
            <ul class="card_list">
                <div 
                    v-for="card in cards" 
                    :key="card.id"
                    class="drag-el"
                    draggable="true"
                    @dragStart="startDrag($event, card)"
                >
                    <button @click="toggleCard(card)">{{ card.title }}</button>
                    <p>{{ card.content }}</p>
                </div>
            </ul>
        </div>
        <div class="add_card">
            <form v-on:submit.prevent="submitForm">
                <div class="form-group">
                    <label for="title">Title</label>
                    <input type="text" class="form-control" id="title" v-model="title">
                </div>
                <div class="form-group">
                    <label for="value">Value</label>
                    <textarea class="form-control" id="value" v-model="value"></textarea>
                </div>
                <div class="form-group">
                    <label for="content">Content</label>
                    <textarea class="form-control" id="content" v-model="content"></textarea>
                </div>
                <div class="form-group">
                    <button type="submit">Add Card</button>
                </div>
            </form>
        </div>
    </div>
</template>


<script>
    export default {
        data() {
            return {
                cards: [],
                title: '',
                value: 0,
                list: 0, 
                localOrder: 0,
                description: '',
            }
        },
        methods: {
            async getData() {
                try {
                    const response = await this.$http.get('http://localhost:8000/api/cards/');
                    this.cards = response.data; 
                } catch (error) {
                    console.log(error);
                }
            },
            async getCard(list) {
                return this.cards.value.filter((card) => card.list == list) 
            },
            async submitForm(){
                try {
                    const response = await this.$http.post('http://localhost:8000/api/cards/', {
                        title: this.title,
                        content: this.content,
                        order: this.cards.length+1,
                        list: this.list,
                    });
                    this.cards.push(response.data);
                    // Reset the title and description field values.
                    this.title = '';
                    this.value = 0;
                    this.content = '';
                } catch (error) {
                    console.log(error);
                }
            },
            async toggleCard(card){
                try{
                    const response = await this.$http.put(`http://localhost:8000/api/cards/${card.id}/`, {
                        completed: !card.completed,
                        title: card.title,
                        value: card.value,
                        content: card.content,
                        order: this.localOrder,
                    });
                    let cardIndex = this.cards.findIndex(c => c.id === card.id);
                    // Reset the cards array with the new data of the updated task
                    this.cards = this.cards.map((card) => {
                        if(this.cards.findIndex(c => c.id === card.id) === cardIndex){
                            return response.data;
                        }
                        return card;
                    });

                }catch(error){
                    console.log(error);
                }
            },
            async deleteCard(card){
                if(confirm("Are you sure?")){
                    try{
                        await this.$http.delete(`http://localhost:8000/api/cards/${card.id}`);
                        this.getData();
                    } catch(error){
                        console.log(error)
                    }
                }      
            },
            startDrag(event, item) {
                console.log(item)
                event.dataTransfer.dropEffect = "move"
                event.dataTransfer.effectAllowed = "move"
                event.dataTransfer.setData('localOrder', item.order)
            }
        },
        created() {
            this.getData();
        }
    }
</script>