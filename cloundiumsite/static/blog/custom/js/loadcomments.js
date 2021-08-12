$(document).ready(function(){
    $("#loadMoreComments").on("click", function(){
        var _currentComments=$(".comment-box").length;
        var _limit=$(this).attr('data-limit');
        var _total=$(this).attr('data-total');
        var _blogpostid = $(this).attr('data-blogpostid');
        console.log(_currentComments,_limit,_total,_blogpostid,'fefef')
        //start AJAX
        $.ajax({
            url:'/load-more-comments',
            data:{
                limit:_limit,
                offset:_currentComments,
                blog_post_id:_blogpostid,
            },
            dataType:'json',
            beforeSend: function(){
                $("#loadMoreComments").attr('disabled',true);
                $(".load-more-icon").addClass('fa-spin');
            },
            success:function(res){
                $("#filteredComments").append(res.data);
                $("#loadMoreComments").attr('disabled',false);
                $(".load-more-icon").removeClass('fa-spin');

                var _totalShowing=$(".comment-box").length;
                console.log(res.data);
				if(_totalShowing==_total){
					$("#loadMoreComments").remove();
				}
            }
        })
    });

    $("#loadMoreReplies").on("click", function(){
        
        var _limit=$(this).attr('data-limit');
        var _total=$(this).attr('data-total');
        var _blogcommentid = $(this).attr('data-blogcommentid');
        var _currentReplies=$(".reply-box-for-"+_blogcommentid).length;
        
        console.log(_currentReplies,_limit,_total,_blogcommentid)
        //start AJAX
        $.ajax({
            
            url:'/load-more-replies',
            data:{
                limit:_limit,
                offset:_currentReplies,
                post_comment_id:_blogcommentid,
            },
            dataType:'json',
            beforeSend: function(){
                $("#loadMoreReplies").attr('disabled',true);
                $(".load-more-icon").addClass('fa-spin');
            },
            success:function(res){
                $("#filteredReplies").append(res.data);
                $("#loadMoreReplies").attr('disabled',false);
                $(".load-more-icon").removeClass('fa-spin');
                
                var _totalShowing=$(".reply-box-for-"+_blogcommentid).length;
				if(_totalShowing==_total){
					$("#loadMoreReplies").remove();
				}
            }
        })
    });
}); 