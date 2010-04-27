$(function(content, source, overlay){
	
	content = $("#content");
	
	$("#screen", content).overscroll();
	
	source = $("#source", content);
	
	overlay = $("#overlay", content);
	
	overlay.delayedFadeIn = function() {
		overlay.fadeTimeout = setTimeout(function(){
			overlay.fadeTimeout = null;
			overlay.stop(true, true).fadeIn("fast");
		}, 1000);
	};
	
	overlay.instantFadeOut = function() {
		if(overlay.fadeTimeout != null) {
			clearTimeout(overlay.fadeTimeout);
			overlay.fadeTimeout = null;
		} else {
			overlay.stop(true, true).fadeOut("fast");
		}
	};
	
	overlay.fadeIn("fast").parent()
		.bind("mouseenter", overlay.instantFadeOut)
		.bind("mouseleave", overlay.delayedFadeIn);
	
});