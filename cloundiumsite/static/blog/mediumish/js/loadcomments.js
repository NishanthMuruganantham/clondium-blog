$(document).ready(function(){
    $("#loadMoreComments").on("click", function(){
        var _currentComments=$(".comment-box").length;
        var _limit=$(this).attr('data-limit');
        var _total=$(this).attr('data-total');
        var _blogpostid = $(this).attr('data-blogpostid');
        console.log(_currentComments,_limit,_total,_blogpostid)
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
				if(_totalShowing==_total){
					$("#loadMoreComments").remove();
				}
            }
        })
    });
}); 