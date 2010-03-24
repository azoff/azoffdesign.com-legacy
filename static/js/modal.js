(function(w){
	
	w.modal = function(options) {
			
		options = options || {};
		
		options.icon = options.icon ? "ui-icon-" + options.icon : "ui-icon-info";
		
		if (w.modal.dialog) {
			
			w.modal.dialog.remove();
		
		}
		
		w.modal.dialog = $('<div><img class="ui-icon ' + options.icon + '" /><div>' + (options.message || '') + '</div></div>').appendTo("body");
		
		options.buttons = options.buttons || {"Ok.":function(){}};
		
		$.each(options.buttons, function(key, handler){
			
			options.buttons[key] = function() {
				
				handler.call(w.modal.dialog);
				
				w.modal.dialog.remove();
				
				w.modal.dialog = null;
				
			}
			
		})
		
		w.modal.dialog.dialog({
			
			title: options.title || "Alert",
			
			bgiframe: true,
	
			resizable: false,
	
			modal: true,

			buttons: options.buttons
		
		});

	}
	
})(window);