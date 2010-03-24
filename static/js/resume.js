$(function(win, body, work, tabs, selected){
	
	work = $("#work");
	
	selected = $(".selected li", work);
	
	tabs = $(".tabs li", work).click(function(tab){
		
		tabs.removeClass("active");
		
		tab = $(this).addClass("active");
		
		selected.removeClass("active").filter("." + tab.attr("rel")).addClass("active");
		
	});
	
});