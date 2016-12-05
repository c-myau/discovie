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

    self.mouse_over = function (img_idx, star_idx) {
        self.vue.movie_list[img_idx].num_stars_display = star_idx;
    };

    self.mouse_out = function (img_idx) {
        self.vue.movie_list[img_idx].num_stars_display = self.vue.movie_list[img_idx].num_stars;
    };

    self.set_stars = function (img_idx, star_idx) {
        var img = self.vue.movie_list[img_idx];
        img.num_stars = star_idx;
        img._pending = true;
        self.vue.$set(self.vue.movie_list, img_idx, img);
        $.post(vote_url,
            {
                image_id: img.id,
                num_stars: star_idx
            },
            function () {
                img = self.vue.movie_list[img_idx];
                img._pending = false;
                self.vue.$set(self.vue.movie_list, img_idx, img);
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
