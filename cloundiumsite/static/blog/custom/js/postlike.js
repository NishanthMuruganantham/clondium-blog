$(document).on('click','#like_button',function(e) {
    e.preventDefault();
    
    var _postid = $(this).attr('data-postid');
    var _likeurl = $(this).attr('data-likeurl');
    console.log(_postid,_likeurl,'new');
    $.ajax({
        type: 'POST',
        url: _likeurl,
        data:{
            postid:_postid,
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
            action: 'post'
        },
        success: function (json) {
            var _isPostLiked = json['is_post_liked']
            var _likescount = json['result']
            document.getElementById("like_count").innerHTML = _likescount
            
            if($("#like_button").hasClass("posthearted"))
            {
                $("#like_button").html('<i class="fa fa-heart-o" aria-hidden="true"></i>');
                $("#like_button").removeClass("posthearted");
            }
            else
            {
                $("#like_button").html('<i class="fa fa-heart" aria-hidden="true"></i>');
                $("#like_button").addClass("posthearted");
            }
        },
        error: function (xhr, errmsg, err) {
        }
    });
})

// 









//* OLD SCRIPT

// $(document).ready(function(){
//     $("#heart").click(function(){
//         if($("#heart").hasClass("posthearted")){
//         $("#heart").html('<i class="fa fa-heart-o" aria-hidden="true"></i>');
//         $("#heart").removeClass("posthearted");
//         }else{
//         $("#heart").html('<i class="fa fa-heart" aria-hidden="true"></i>');
//         $("#heart").addClass("posthearted");
//         }
        
//         var _postid = $(this).attr('data-postid');
//         var _postslug = $(this).attr('data-postslug');
//         var _userid = $(this).attr('data-userid');
//         console.log(_postid,_userid);
//         //start AJAX
//         $.ajax({
//             url: 'http://127.0.0.1:8000/post-like/',
//             data:{
//                 postid: _postid,
//                 postslug: _postslug,
//             },
//             dataType:'json',
//         })
//     });
// });





//     if (_isPostLiked) {
//         $("#like_button").html('<i class="fa fa-heart" aria-hidden="true"></i>');
//     }
//     else {
//         $("#like_button").html('<i class="fa fa-heart-o" aria-hidden="true"></i>');
//     }