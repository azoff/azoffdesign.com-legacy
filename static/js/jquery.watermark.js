/*!
 * Watermark v1.1.0
 *  A jQuery Plugin for adding watermarks to text-based form fields.
 *  http://azoffdesign.com/watermark
 *
 * Intended for use with the latest jQuery
 *  http://code.jquery.com/jquery-latest.min.js
 *
 * Copyright 2010, Jonathan Azoff
 * Dual licensed under the MIT or GPL Version 2 licenses.
 *  http://jquery.org/license
 *
 * Date: Wednesday, April 4th 2010
 */

/* 
 * Usage:
 * 
 * $(selector).watermark([options]);
 *  "options" is an optional JavaScript object that you may pass if you would like to customize
 *  the watermark application. Below is a list of properties that you may set on
 *  the options object and their respective effect:
 *   - options.color	{String} The color to use for the watermarked text (default "#AAA").
 *   - options.text		{String} The text to use for the watermark, overrides the default (default uses title attribute)
 *
 * Notes:
 * 
 * The plug-in applies a submit handler to any parent forms so that watermarked text is not submitted when the form is.
 * However, this may not prevent all cases of form submission (such as AJAX serialization + submission) so caution should be     
 * taken on the server-side to ensure validity of the submitted values.       
 *
 * Changelog:
 *
 * 1.1.0 
 *   - Updated license
 *	 - Refactored to prevent memory leaks, maximize code reuse
 *   - Added jslint to the build process
 *	 - Namespaced code
 *
 * 1.0.4
 *   - Added fix to clear input before submission if field is empty (thanks alice)
 *
 * 1.0.3
 *   - Fixed css inherit bug for ie7 (thanks ambrauer) *
 *
 * 1.0.2
 *   - Simplified dragging support
 *   - Refactored focus initialization behavior 
 *
 * 1.0.1
 *   - Improved listeners so that they handle text dragged into the boxes (thanks to Jury for this one!)
 *   
 */

/*jslint onevar: true, strict: true */
/*global jQuery: false */
"use strict";

(function($, w){

	// public exposed watermark extension
	w = $.fn.watermark = function(options) {
		return this.each(function(){
			w.init($(this), options);
		});
	};
	
	// events watermark listens to
	w.events = {
		on: "blur",
		off: "focus drop"
	};
	
	// reusable constants and strings
	w.constants = {
		color: "#AAA",
		css: "color", // cause I'm anal
		key: "w",
		applied: "watermarked",
		watermarkable: "textarea,input[type='text'],input[type='password']"
	};
	
	// constructor for each watermarkable element
	w.init = function(obj, options) {
		
		if(obj.is(w.constants.watermarkable) && !obj.data(w.constants.applied)) {
		
			options = $.extend({
				text: obj.attr("title"),
				color: w.constants.color						
			}, (options || {}));

			obj.closest("form").bind("submit", obj, w.onSubmit);
			
			// attach handlers
			obj.bind(w.events.on, options, w.on)
			   .bind(w.events.off, options, w.off);
			
			// apply the watermark
			w.on.call(obj, {data:options});
			
			obj.data(w.constants.applied, true);
			
		}

	};
	
	// applies the watermark
	w.on = function(event, obj, options) {
		obj = $(this);
		options = event.data;
		if(obj.val().length === 0 && !obj.data(w.constants.key)) {
			
			obj.data(w.constants.key, true)
			   .css(w.constants.css, options.color)
			   .val(options.text);
			
		}
	};
	
	// removes the watermark
	w.off = function(event, obj, options) {
		obj = $(this);
		options = event.data;
		if(obj.data(w.constants.key)) {
			
			obj.data(w.constants.key, false).css(w.constants.css, "");
			
			// capture drag and drop
			if (event.originalEvent && event.originalEvent.dataTransfer)  {
				obj.val(event.originalEvent.dataTransfer.getData("Text"));
			} else {
				obj.val("");
			}
	
		}
	};
	
	// clears watermarked elements on parent form submission event
	w.onSubmit = function(event, obj) {
		obj = event.data;
		if (obj.data(w.constants.key)) {
			obj.val("");
		}
		return true;
	};	
	
})(jQuery);
