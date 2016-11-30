// This is the js for the default/index.html view.

var app = function() {

    var self = {};

    Vue.config.silent = false; // show all warnings

    self.extend = function(a, b) {
        for (var i = 0; i < b.length; i++) {
            a.push(b[i]);
        }
    };

    // // Generate url to get posts based on the index interval.
    function generate_posts_url(start_idx, end_idx) {
        var parameters = {
            start_index: start_idx,
            end_index: end_idx
        };
        return get_posts_url + "?" + $.param(parameters);
    }

    self.get_posts = function() {
        $.getJSON(generate_posts_url(0, 4), function(data) {
            self.vue.has_more = data.has_more;
            self.vue.logged_in = data.logged_in;
            self.vue.posts = data.posts;
            self.vue.user_email = data.user_email;
            for (var i = 0; i < self.vue.posts.length; i++) {
                self.vue.posts[i].edit = false;
                self.vue.edit_status[self.vue.posts[i].id] = false;
                self.vue.posts[i].temp = self.vue.posts[i].post_content;
            }
        })
    };

    self.get_more = function() {
        var posts_len = self.vue.posts.length;
        $.getJSON(generate_posts_url(posts_len, posts_len + 4), function(data) {
            self.vue.has_more = data.has_more;
            self.extend(self.vue.posts, data.posts);
        });

    };

    self.add_post_button = function() {
        self.vue.is_adding_post = !self.vue.is_adding_post;
    };

    self.cancel_post_button = function() {
        self.vue.is_adding_post = !self.vue.is_adding_post;
        self.vue.form_post_content = null;
    };

    self.edit_post_button = function(post_id) {
        self.vue.edit_status[post_id] = !self.vue.edit_status[post_id];
    };

    self.add_post = function() {
        self.vue.is_adding_post = !self.vue.is_adding_post;
        $.post(add_post_url,
            {
                post_content: self.vue.form_post_content
            },
            function(data) {
                $.web2py.enableElement($("#add_post_submit"));
                if (self.vue.posts.length == 4) {
                    self.vue.has_more = true;
                    self.vue.posts.pop();
                }
                self.vue.posts.unshift(data.post);
                self.vue.form_post_content = null;
            });
    };

    self.save_post = function(text, post_id, post) {
        $.post(edit_post_url,
            {
                post_id: post_id,
                post_content: text
            },
            function(data) {
                var post_id = data.post.id;
                for (var i = 0; i < self.vue.posts.length; i++) {
                    if (self.vue.posts[i].id == post_id) {
                        self.vue.posts[i].updated_on = data.post.updated_on;
                        break;
                    }
                }
                post.temp = text;
            });
    };

    self.cancel_post = function(post, post_temp) {
        post.post_content = post_temp;
    };

    self.delete_post = function(post_id) {
        $.post(del_post_url,
            {
                post_id: post_id
            },
            function() {
                var index = null;
                for (var i = 0; i < self.vue.posts.length; i++) {
                    if (self.vue.posts[i].id == post_id) {
                        index = i + 1;
                        break;
                    }
                }
                if (index) {
                    self.vue.posts.splice(index - 1, 1);
                }
                if (self.vue.posts.length < 4) {
                    $.getJSON(generate_posts_url(self.vue.posts.length, 4), function(data) {
                        self.vue.has_more = data.has_more;
                        self.extend(self.vue.posts, data.posts);
                    });
                }
            }
        )
    };

    // Complete as needed.
    self.vue = new Vue({
        el: "#vue-div",
        delimiters: ['${', '}'],
        unsafeDelimiters: ['!{', '}'],
        data: {
            has_more: false,
            logged_in: false,
            posts: [],
            is_adding_post: false,
            form_post_content: null,
            user_email: null,
            edit_status: [],
            is_editing_post: false
        },
        methods: {
            // get_more: self.get_more,
            add_post_button: self.add_post_button,
            cancel_post_button: self.cancel_post_button,
            add_post: self.add_post,
            get_more: self.get_more,
            delete_post: self.delete_post,
            edit_post_button: self.edit_post_button,
            save_post: self.save_post,
            cancel_post: self.cancel_post
        }

    });

    self.get_posts();
    // self.add_post();
    $("#vue-div").show();

    return self;
};

var APP = null;

// This will make everything accessible from the js console;
// for instance, self.x above would be accessible as APP.x
jQuery(function(){APP = app();});

function hideEditBtn(obj) {
    $(obj).hide();
    $(obj).parent().find("#saveBtn").show();
    $(obj).parent().find("#cancelBtn").show();
    $(obj).parent().prev().find("#post").hide();
    $(obj).parent().prev().find("#textarea").show();

}

function hidePostBtn(obj) {
    $(obj).hide();
    $(obj).parent().find("#editBtn").show();
    $(obj).parent().find("#cancelBtn").hide();
    $(obj).parent().prev().find("#post").show();
    $(obj).parent().prev().find("#textarea").hide();
}

function hideCancelBtn(obj, temp) {
    $(obj).hide();
    $(obj).parent().find("#editBtn").show();
    $(obj).parent().find("#saveBtn").hide();
    $(obj).parent().prev().find("#post").show();
    $(obj).parent().prev().find("#textarea").hide();
    var text = $(obj).parent().prev().find("#textarea").val();
}


