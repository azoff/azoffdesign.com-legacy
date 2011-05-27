(function($, global){
	
	global = $(global);
	
	function easeOutQuad(x, t, b, c, d) {
		return -c *(t/=d)*(t-2) + b;
	}
	
	function animateCloud(cloud) {
		cloud.right = cloud.right || (global.width()/1.6 - cloud.elm.width());
		cloud.elm.animate({left:cloud.right, top:cloud.top, opacity:0}, cloud.time, "easeOutQuad", function(){
			cloud.elm.css({left:cloud.left, top:cloud.bottom, opacity:1});
			animateCloud(cloud);
		});
	}
	
	function startClouds(clouds) {
		animateCloud({
			elm: clouds.filter(".small"),
			left: -300,
			bottom: 40,
			top: 30,
			time: 60 * 1000
		});

		animateCloud({
			elm: clouds.filter(".medium"),
			left: -500,
			bottom: 290,
			top: 220,
			time: 45 * 1000
		});

		animateCloud({
			elm: clouds.filter(".large"),
			left: -700,
			bottom: 60,
			top: 40,
			time: 40 * 1000
		});
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