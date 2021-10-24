$(document).ready(function(){
    $("#loadMore").on("click", function(){
        var _currentPosts=$(".post-box").length;
        var _limit=$(this).attr('data-limit');
        var _total=$(this).attr('data-total');
        console.log(_currentPosts,_limit,_total)
        //start AJAX
        $.ajax({
            url:'/load-more-data',
            data:{
                limit:_limit,
                offset:_currentPosts,
            },
            dataType:'json',
            beforeSend: function(){
                $("#loadMore").attr('disabled',true);
                $(".load-more-icon").addClass('fa-spin');
            },
            success:function(res){
                $("#filteredProducts").append(res.data);
                $("#loadMore").attr('disabled',false);
                $(".load-more-icon").removeClass('fa-spin');

                var _totalShowing=$(".post-box").length;
				if(_totalShowing==_total){
					$("#loadMore").remove();
				}
            }
        })
    });
}); 