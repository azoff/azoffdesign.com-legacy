(function($, global){
	
	global = $(global);
	
	function easeOutQuad(x, t, b, c, d) {
		return -c *(t/=d)*(t-2) + b;
	}
	
	function animateCloud(cloud) {

	}
	
	function startClouds(clouds) {

	}
	
	
	$(function(){

		var clouds = $(".cloud");

		startClouds(clouds); 
		
		global.resize(function(){
			clouds.stop(true, true);
		});

		$('.tip').qtip({
			prerender: true,
			solo: true,
			position: {
				my: 'bottom center',
				at: 'top center',
				target: 'event'
			},
			show: {
				effect: function(offset) {
					$(this).fadeIn(200); // "this" refers to the tooltip
				}
			},
			style: {
				classes: 'ui-tooltip-jtools'
			}
		});

	});
	
	$.extend($.easing,{ easeOutQuad: easeOutQuad });
	
})(jQuery, window);