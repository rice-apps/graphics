// Fix Navigation on Scroll
$(window).scroll(function(){
    	if ($(this).scrollTop() > 150) {
        	$('.navbar').addClass('fix-scroll');
        	$('.navbar-fix').addClass('space');
    	} else {
        	$('.navbar').removeClass('fix-scroll');
        	$('.navbar-fix').removeClass('space');
    	}
	});
