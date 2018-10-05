"use strict";

class Autobox {
    constructor(elem, apiSource) {
        this.elem = elem;
        this.apiSource = apiSource;

        this.datalist = document.getElementById(this.elem.getAttribute('list'));
        this.group = this.elem.getAttribute('group');
    }

    updateDropdown() {
        this.queryApi().then((response) => this.updateHTML(response))
    };

    updateHTML(suggestions) {
        // remove all existing nodes
        while(this.datalist.firstChild) {
            this.datalist.removeChild(this.datalist.firstChild);
        }
        for(let i = 0; i < suggestions.length; i++) {
            let opt = document.createElement('OPTION');
            opt.value = suggestions[i];
            this.datalist.appendChild(opt);
        }
    };

    queryApi() {
        let form = new FormData();
        form.append('query', this.elem.value);
        // if this textbox is associated with a particular group, add that query parameter
        if(this.group) {
            form.append('group', this.group);
        }
        return fetch(this.apiSource, {method: 'POST', body: form})
            .then((response) => response.json())
    };
}

window.addEventListener('load', function() {
    let autoboxes = document.getElementsByClassName('autocomplete');
    for(let i = 0; i < autoboxes.length; i ++) {
        let abox = new Autobox(autoboxes[i], window.location.origin + '/api/users/search');
        autoboxes[i].addEventListener('input', function(event) {
            abox.updateDropdown();
        });
    }
});