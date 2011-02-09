(function(w){
	
	var 
	overlay,
	hoverClass = "ui-state-active",
	translucentClass = "ui-priority-secondary",
	openClass = "open";
	
	w.log = function() {
		if (console && debug) {
			return console.log.apply(console, Array.prototype.slice.call(arguments));
		}
	};
	
	$(function(){

		// get the overlay
		overlay = $("#overlay");

		// binds the handlers for the template tabs
		$(".widgit_tab").hover(onTabOver, onTabOut).click(onTabClick);

		// set up disqus counter
		loadDisqusCounter();
		
		// bind handlers for any buttons
		$("button").mouseover(function(){
			$(this).addClass("ui-state-hover");
		}).mouseout(function(){
			$(this).removeClass("ui-state-hover");
		}).mousedown(function(){
			$(this).addClass("ui-state-active");
		}).mouseup(function(){
			$(this).removeClass("ui-state-active");
		});

	});
	
	function onTabOver(tab, widgit) {
		
		tab = $(this);
		
		widgit = tab.parent();
		
		if(widgit.data(openClass)) {
		
			tab.children().addClass(hoverClass);
	
		} else {
	
			widgit.removeClass(translucentClass);
	
		}
			
	};
	
	function onTabOut(tab, widgit) {
		
		tab = $(this);
		
		widgit = tab.parent();
		
		if(widgit.data(openClass)) {
		
			tab.children().removeClass(hoverClass);
	
		} else {
	
			tab.children().removeClass(hoverClass);
	
			widgit.addClass(translucentClass);
	
		}
			
	};
	
	function onTabClick(tab, button, widgit) {

		tab = $(this);
		
		button = tab.children();
		
		widgit = tab.parent();
		
		if(widgit.data(openClass)) {

			widgit.removeClass(openClass);
			
		} else {
						
			widgit.addClass(openClass);
			
		}
		
		widgit.data(openClass, !widgit.data(openClass));
		
	};
	
	function loadDisqusCounter(links, query, i) {
		
		links = document.getElementsByTagName('a');
		
		query = '?';
		
		for(i=0; i<links.length; i++) {
			if(links[i].href.indexOf('#disqus_thread') >= 0) {
				query += 'url' + i + '=' + encodeURIComponent(links[i].href) + '&';
			}
		}
		
		$("body").append("<script src='http://disqus.com/forums/azoff/get_num_replies.js" + query + "'></script>");
		
	};
	
})(window);