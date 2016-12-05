// This is the js for the default/index.html view.

var app = function () {

    var self = {};

    Vue.config.silent = false; // show all warnings

    // Extends an array
    self.extend = function (a, b) {
        for (var i = 0; i < b.length; i++) {
            a.push(b[i]);
        }
    };

    // Enumerates an array.
    var enumerate = function (v) {
        var k = 0;
        return v.map(function (e) {
            e._idx = k++;
        });
    };

    // Decorate the array of images.
    var decorate = function (v) {
        return v.map(function (e) {
            e._pending = false;
        });
    };

    self.get_info = function () {
        $.getJSON(get_info_url, function (data) {
            self.vue.movie_list = data.movie_list;
            enumerate(self.vue.movie_list);
            decorate(self.vue.movie_list);
        });
    };

    self.mouse_over = function (movie_idx, star_idx) {
        self.vue.movie_list[movie_idx].num_stars_display = star_idx;
    };

    self.mouse_out = function (movie_idx) {
        self.vue.movie_list[movie_idx].num_stars_display = self.vue.movie_list[movie_idx].num_stars;
    };

    self.set_stars = function (movie_idx, star_idx) {
        var movie = self.vue.movie_list[movie_idx];
        movie.num_stars = star_idx;
        movie._pending = true;
        self.vue.$set(self.vue.movie_list, movie_idx, movie);
        $.post(vote_url,
            {
                movie_id: movie.id,
                num_stars: star_idx
            },
            function () {
                movie = self.vue.movie_list[movie_idx];
                movie._pending = false;
                self.vue.$set(self.vue.movie_list, movie_idx, movie);
            }
        )
    };

    // Complete as needed.
    self.vue = new Vue({
        el: "#vue-div",
        delimiters: ['${', '}'],
        unsafeDelimiters: ['!{', '}'],
        data: {
            movie_list: [],
            is_logged_in: is_logged_in,
            star_indices: [1, 2, 3, 4, 5]
        },
        methods: {
            mouse_over: self.mouse_over,
            mouse_out: self.mouse_out,
            set_stars: self.set_stars
        }

    });

    self.get_info();
    $("#vue-div").show();

    return self;
};

var APP = null;

// This will make everything accessible from the js console;
// for instance, self.x above would be accessible as APP.x
jQuery(function () {
    APP = app();
});
