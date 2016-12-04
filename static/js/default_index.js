// This is the js for the default/index.html view.

var app = function () {

    var self = {};

    Vue.config.silent = false; // Show all warnings

    // Enumerates an array.
    var enumerate = function (v) {
        var k = 0;
        return v.map(function (e) {
            e._idx = k++;
        });
    };

    // Returns movies
    self.get_movies = function () {
        //alert('Hello ' + this.name + '!');
        $.get(movies_url, $.param({q: self.vue.movie_search}), function (data) {
            //alert('Search Terms: ' + self.vue.movie_search);
            self.vue.movie_list = data.movie_list;
            enumerate(self.vue.movie_list);
        });
    };

    self.vue = new Vue({
        el: "#vue-div",
        delimiters: ['${', '}'],
        unsafeDelimiters: ['!{', '}'],
        data: {
            movie_list: [],
            movie_search: ''
        },
        methods: {
            get_movies: self.get_movies,
            do_search: self.get_movies
        }
    });

    self.get_movies();

    $("#vue-div").show();

    return self;
};

var APP = null;

// This will make everything accessible from the js console;
// for instance, self.x above would be accessible as APP.x
jQuery(function () {
    APP = app();
});
