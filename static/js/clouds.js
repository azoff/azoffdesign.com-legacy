$(function(left, animate){

	jQuery.extend(jQuery.easing, {
		easeOutQuad: function (x, t, b, c, d) {
			return -c *(t/=d)*(t-2) + b;
		}
	});

	width = $(window).width();

	animate = function(cloud) {
		cloud.top = cloud.top || (cloud.bottom - 30);
		cloud.right = cloud.right || (width - cloud.elm.width());
		cloud.elm.animate({left:cloud.right, top:cloud.top, opacity:0}, cloud.time, "easeOutQuad", function(){
			cloud.elm.css({left:cloud.left, top:cloud.bottom, opacity:1});
			animate(cloud);
		});
	};

	animate({
		elm: $(".cloud.small"),
		left: -300,
		bottom: 40,
		time: 60 * 1000
	});
		
	animate({
		elm: $(".cloud.medium"),
		left: -500,
		bottom: 290,
		time: 45 * 1000
	});
		
	animate({
		elm: $(".cloud.large"),
		left: -700,
		bottom: 60,
		time: 40 * 1000
	});
	
});