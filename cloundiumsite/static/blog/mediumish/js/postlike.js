$(document).ready(function(){
    $("#heart").click(function(){
        if($("#heart").hasClass("posthearted")){
        $("#heart").html('<i class="fa fa-heart-o" aria-hidden="true"></i>');
        $("#heart").removeClass("posthearted");
        }else{
        $("#heart").html('<i class="fa fa-heart" aria-hidden="true"></i>');
        $("#heart").addClass("posthearted");
        }
        
        var _postid = $(this).attr('data-postid');
        var _postslug = $(this).attr('data-postslug');
        var _userid = $(this).attr('data-userid');
        console.log(_postid,_userid);
        //start AJAX
        $.ajax({
            url: 'http://127.0.0.1:8000/post-like/',
            data:{
                postid: _postid,
                postslug: _postslug,
            },
            dataType:'json',
        })
    });
});