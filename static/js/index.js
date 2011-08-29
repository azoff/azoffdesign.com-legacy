(function($, global, math){
	
	var frame = $(global), clouds, viewport;
	
	function animateCloud() { var 
	    cloud = $(this).stop(true, true),
	    duration = parseInt(cloud.data('duration'), 10) * 1000,
	    delay = parseInt(cloud.data('delay'), 10) * 1000,
	    callback = $.proxy(animateCloud, this);
	    cloud.animate({ translateX: 0, opacity: 1 }, 0);
	    setTimeout(function(){
	        cloud.animate({ translateX: viewport, opacity: 0 }, duration);
    	    setTimeout(callback, duration);
	    }, delay);
	}

	function animateClouds() {
	    if (!viewport || frame.width() < viewport) {
	        viewport = frame.width();
	        clouds.each(animateCloud);
	    }
	}
	
	function initClouds() {
	    clouds = $('.cloud');
	    frame.resize(animateClouds);
	    animateClouds();
	}
	
	$(initClouds);
	
})(jQuery, window, Math);