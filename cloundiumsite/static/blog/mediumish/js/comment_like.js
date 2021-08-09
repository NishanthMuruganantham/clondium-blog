function comment_liked(e){
    var _commentid = $(e).attr('data-commentid');
    var _commentlikeurl = $(e).attr('data-commentlikeurl');
    var _id = $(e).attr('id');
    console.log(_commentid,_commentlikeurl,_id,_commentid+"_comment_like_count");
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