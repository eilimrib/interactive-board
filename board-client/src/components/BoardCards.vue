<template>
    <div class="cards_container">
        <div class="cards_content">
            <h1>Cards</h1>
            <ul class="card_list">
                <li v-for="card in cards" :key="card.id">
                    <h2>{{ card.title }}</h2>
                    <p>{{ card.value }}</p>
                    <p>{{ card.content }}</p>
                    <button @click="toggleCard(card)">
                        {{ card.completed ? 'Undo' : 'Complete' }}
                    </button>
                    <button @click="deleteCard(card)">Delete</button>
                </li>
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
                description: '',
            }
        },
        methods: {
            async getData() {
                try {
                    // fetch tasks
                    const response = await this.$http.get('http://localhost:8000/api/cards/');
                    // set the data returned as tasks
                    this.cards = response.data; 
                } catch (error) {
                    // log the error
                    console.log(error);
                }
            },
            async submitForm(){
                try {
                    // Send a POST request to the API
                    const response = await this.$http.post('http://localhost:8000/api/cards/', {
                        title: this.title,
                        value: this.value,
                        content: this.content,
                        completed: false
                    });
                    // Append the returned data to the tasks array
                    this.cards.push(response.data);
                    // Reset the title and description field values.
                    this.title = '';
                    this.value = 0;
                    this.content = '';
                } catch (error) {
                    // Log the error
                    console.log(error);
                }
            }
        },
        created() {
            // Fetch tasks on page load
            this.getData();
        }
    }
</script>