<template>
    <form  @submit.prevent = "uploadPhoto" merthod="POST" id="uploadForm">
        <div class="form">
            <label for="description">Description</label>
            <textarea class="control" id="description" rows="15"></textarea>
        </div>

        <div class="group">
            <label for="photo">Photo</label>
            <input type="file" class="file-submit" id="photo">
        </div>
        <button class="btn btn-primary mb-2">Submit</button>
    </form>
</template>

<script>import { createDOMCompilerError } from "@vue/compiler-dom";

    export default {
        data() {
            return {
                crsf_token: ''
            };
    },
    methods: {
        uploadPhoto(){
            let uploadForm = documnet.getElementById('uploadForm');
            console.log(uploadForm)
            let form_data = new FormData(uploadForm);
            console.log(form_data)
            
            fetch("/api/upload", {
                method: 'POST',
                body: form_data,
                headers: {
                    'X-CSRFToken': this.csrf_token
                }
                })
                .then(function (response) {
                    return response.json();
                    })
                    .then(function (data) {
                        //display a success message
                        console.log(data);
                        })
                        .catch(function (error) {
                            console.log(error);
                            });                
        },

        getCsrfToken() {
            let self = this;
            fetch('/api/csrf-token')
            .then((response) => response.json())
            .then((data) => {
                console.log(data);2
                self.csrf_token = data.csrf_token;
            })
        },

        created() {
            this.gitCsrfToken();
        },
    }
}
</script>