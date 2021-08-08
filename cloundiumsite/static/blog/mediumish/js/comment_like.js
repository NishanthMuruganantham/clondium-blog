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
            var _commentlikescount = json['result']
            var is_post_liked = json['is_post_liked']
            console.log(is_post_liked)
            document.getElementById("comment_like_count_for_"+_commentid).innerHTML = _commentlikescount

            if(is_post_liked === false)
            {
                $("#"+_id).html('<i class="fa fa-thumbs-o-up" aria-hidden="true"></i>');
                $("#"+_id).removeClass("comment_liked");
                console.log('unlike')
            }
            else
            {
                $("#"+_id).html('<i class="fa fa-thumbs-up" aria-hidden="true"></i>');
                $("#"+_id).addClass("comment_liked");
                console.log('like')
            }
        },
        error: function (xhr, errmsg, err) {
        }
    });
}