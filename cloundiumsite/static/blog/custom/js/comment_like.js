// * FUNCTION TO LIKE THE POST
function like_post(e) {
    var like_id = $(e).attr('id');
    var url_for_like_post = $(e).attr('data-likeurl');
    var post_id = $(e).attr('data-postid');
    console.log(like_id,url_for_like_post,post_id,'new');

    $.ajax({
        type: 'POST',
        url: url_for_like_post,
        data:{
            post_id:post_id,
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
            action: 'post'
        },
        success: function (json) {
            
            var is_post_liked = json['is_post_liked']
            var post_likes_count = json['likes_count']
            console.log(is_post_liked)

            // * MODIFYING THE LIKES COUNT
            document.getElementById("like_count_for_"+post_id).innerHTML = post_likes_count

            // * MODIFYING THE SAVE BUTTON
            if(is_post_liked === false)
            {
                $("#like_post_button_"+post_id).html('<i class="fa fa-heart-o" aria-hidden="true"></i>');
                $("#like_post_button_"+post_id).removeClass("post_liked");
                // document.getElementById("post_save_message").innerHTML = "Save"
                console.log('not liked')
            }
            else
            {
                $("#like_post_button_"+post_id).html('<i class="fa fa-heart" aria-hidden="true"></i>');
                $("#like_post_button_"+post_id).addClass("post_liked");
                // document.getElementById("post_save_message").innerHTML = "Saved"
                console.log('liked')
            }
        },
        error: function (xhr, errmsg, err) {
        }
    });
}



// * FUNCTION TO FOLLOW A USER
function follow_user(e) {
    var followed_user_id = $(e).attr('data-followed_user_id');
    var followurl = $(e).attr('data-followurl');
    console.log(followed_user_id,followurl);

    $.ajax({
        type: 'POST',
        url: followurl,
        data:{
            followed_user_id:followed_user_id,
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
            action: 'post'
        },
        success: function (json) {
            
            var is_followed= json['followed']
            var followers_count = json['followers_count']
            console.log(is_followed,followers_count)

            // * MODIFYING THE LIKES COUNT
            document.getElementById("follower_count_for_"+followed_user_id).innerHTML = followers_count
            

            // * MODIFYING THE SAVE BUTTON
            if(is_followed === false)
            {   
                $("#follow_button_for_"+followed_user_id).parent().css( "background-color", "#2bb3c0" )
                $("#follow_button_for_"+followed_user_id).html('<span id="is_'+followed_user_id+'_followed">Follow</span>');
                $("#follow_button_for_"+followed_user_id).removeClass("post_liked");
                // document.getElementById("post_save_message").innerHTML = "Save"
                console.log('not liked')
            }
            else
            {
                $("#follow_button_for_"+followed_user_id).parent().css( "background-color", "#3bc067" )
                $("#follow_button_for_"+followed_user_id).html('<span id="is_'+followed_user_id+'_followed">Following</span>');
                $("#follow_button_for_"+followed_user_id).addClass("post_liked");
                // document.getElementById("post_save_message").innerHTML = "Saved"
                console.log('liked')
            }
        },
        error: function (xhr, errmsg, err) {
        }
    });
}


// * FUNCTION FOR COMMENT LIKE AND DISLIKE
function comment_liked(e){
    var _commentid = $(e).attr('data-commentid');
    var _commentlikeurl = $(e).attr('data-commentlikeurl');
    var _id = $(e).attr('id');
    console.log(_commentid,_commentlikeurl,_id,_commentid+"_comment_like_count",'frfrfrf');
    $.ajax({
        type: 'POST',
        url: _commentlikeurl,
        data:{
            commentid:_commentid,
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
            action: 'post'
        },
        success: function (json) {
            
            var _commentlikescount = json['likes_count']
            var comment_dislikes_count = json['dislikes_count']
            var is_comment_liked = json['is_comment_liked']
            var is_comment_disliked = json['is_comment_disliked']
            console.log(_commentlikescount,comment_dislikes_count,is_comment_liked,is_comment_disliked)

            // * MODIFYING THE LIKES AND DISLIKES COUNT
            document.getElementById("comment_like_count_for_"+_commentid).innerHTML = _commentlikescount
            document.getElementById("comment_dislike_count_for_"+_commentid).innerHTML = comment_dislikes_count

            // * MODIFYING THE LIKE BUTTON
            if(is_comment_liked === false)
            {
                $("#"+_commentid+"_comment_like_button").html('<i class="fa fa-thumbs-o-up" aria-hidden="true"></i>');
                $("#"+_commentid+"_comment_like_button").removeClass("comment_liked");
                console.log('unlike')
            }
            else
            {
                $("#"+_commentid+"_comment_like_button").html('<i class="fa fa-thumbs-up" aria-hidden="true"></i>');
                $("#"+_commentid+"_comment_like_button").addClass("comment_liked");
                console.log('like')
            }

            // * MODIFYING THE DISLIKE BUTTON
            if(is_comment_disliked === false)
            {
                $("#"+_commentid+"_comment_dislike_button").html('<i class="fa fa-thumbs-o-down" aria-hidden="true"></i>');
                $("#"+_commentid+"_comment_dislike_button").removeClass("comment_disliked");
                console.log('unlike')
            }
            else
            {
                $("#"+_commentid+"_comment_dislike_button").html('<i class="fa fa-thumbs-down" aria-hidden="true"></i>');
                $("#"+_commentid+"_comment_dislike_button").addClass("comment_disliked");
                console.log('like')
            }
        },
        error: function (xhr, errmsg, err) {
        }
    });
}


// * FUNCTION FOR REPLY LIKE AND DISLIKE
function reply_liked(e){
    var _replyid = $(e).attr('data-replyid');
    var _replylikeurl = $(e).attr('data-replylikeurl');
    var _id = $(e).attr('id');
    console.log(_replyid,_replylikeurl,_id,_replyid+"_reply_like_count");
    $.ajax({
        type: 'POST',
        url: _replylikeurl,
        data:{
            replyid:_replyid,
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
            action: 'post'
        },
        success: function (json) {
            
            var _replylikescount = json['likes_count']
            var reply_dislikes_count = json['dislikes_count']
            var is_reply_liked = json['is_reply_liked']
            var is_reply_disliked = json['is_reply_disliked']
            console.log(_replylikescount,reply_dislikes_count,is_reply_liked,is_reply_disliked)

            // * MODIFYING THE LIKES AND DISLIKES COUNT
            document.getElementById("reply_like_count_for_"+_replyid).innerHTML = _replylikescount
            document.getElementById("reply_dislike_count_for_"+_replyid).innerHTML = reply_dislikes_count

            // * MODIFYING THE LIKE BUTTON
            if(is_reply_liked === false)
            {
                $("#"+_replyid+"_reply_like_button").html('<i class="fa fa-thumbs-o-up" aria-hidden="true"></i>');
                $("#"+_replyid+"_reply_like_button").removeClass("reply_liked");
                console.log('unlike')
            }
            else
            {
                $("#"+_replyid+"_reply_like_button").html('<i class="fa fa-thumbs-up" aria-hidden="true"></i>');
                $("#"+_replyid+"_reply_like_button").addClass("reply_liked");
                console.log('like')
            }

            // * MODIFYING THE DISLIKE BUTTON
            if(is_reply_disliked === false)
            {
                $("#"+_replyid+"_reply_dislike_button").html('<i class="fa fa-thumbs-o-down" aria-hidden="true"></i>');
                $("#"+_replyid+"_reply_dislike_button").removeClass("reply_disliked");
                console.log('unlike')
            }
            else
            {
                $("#"+_replyid+"_reply_dislike_button").html('<i class="fa fa-thumbs-down" aria-hidden="true"></i>');
                $("#"+_replyid+"_reply_dislike_button").addClass("reply_disliked");
                console.log('like')
            }
        },
        error: function (xhr, errmsg, err) {
        }
    });
}

// * FUNCTION TO SAVE THE POST
function save_post(e) {
    var tag_id = $(e).attr('id');
    var url_for_save_post = $(e).attr('data-url');
    var post_id = $(e).attr('data-postid');
    console.log(tag_id,url_for_save_post,post_id,'new');

    $.ajax({
        type: 'POST',
        url: url_for_save_post,
        data:{
            post_id:post_id,
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
            action: 'post'
        },
        success: function (json) {
            
            var is_post_favourite = json['is_favourite']
            var saves_count = json['saves_count']
            console.log(is_post_favourite)

            // * MODIFYING THE LIKES COUNT
            document.getElementById("save_count_for_"+post_id).innerHTML = saves_count

            // * MODIFYING THE SAVE BUTTON
            if(is_post_favourite === false)
            {
                $("#save_post_button_"+post_id).html('<i class="fa fa-bookmark-o" aria-hidden="true"></i>');
                $("#save_post_button_"+post_id).removeClass("post_saved");
                // document.getElementById("post_save_message").innerHTML = "Save"
                console.log('not saved')
            }
            else
            {
                $("#save_post_button_"+post_id).html('<i class="fa fa-bookmark" aria-hidden="true"></i>');
                $("#save_post_button_"+post_id).addClass("post_saved");
                // document.getElementById("post_save_message").innerHTML = "Saved"
                console.log('saved')
            }
        },
        error: function (xhr, errmsg, err) {
        }
    });
}


function commentReplyToggle(parent_id)
{
    const row = document.getElementById(parent_id);
    if (row.classList.contains('d-none'))
    {
        row.classList.remove('d-none');
    }
    else
    {
        row.classList.add('d-none');
    }
}

function load_more_replies(params) {
    var _currentComments=$(".comment-box").length;
    var _limit=$(this).attr('data-limit');
    var _total=$(this).attr('data-total');
    var _blogpostid = $(this).attr('data-blogpostid');
}