/*!
 * jQuery.jWave v1.1.0
 *  A jQuery plug-in that allows facilitated embedding of Google Wave (R) 
 *	threads into an external website or blog. 
 *
 * Copyright 2010, Jonathan Azoff
 *  Freely distributable under the terms outlined in the DBAD license:
 *  http://github.com/SFEley/candy/blob/master/LICENSE.markdown
 *
 * Date: Sunday, May 3rd 2010
 *
 * For usage examples and API documentation, see azoffdesign.com/jwave 
 */

/*jslint onevar: true, strict: true, browser: true */
/*global window, jQuery, google, gadgets */
"use strict";
(function($, doc, jwave, fn, consts) {
	
	consts = {
		ERROR_ID: " is not a valid Google Wav ID, for details refer to http://azoffdesign.com/jwave#waveid",
		FUNCTION: "function",
		UNDEFINED: "undefined",
		SCRIPT: "script",
		head: doc.getElementsByTagName("head")[0]
	};
	
	jwave = $.fn.jwave = function(id, options, callback) {
		
		if(!fn.isWaveId(id)) {
			throw(id + consts.ERROR_ID);
		}
		
		if(typeof options === consts.FUNCTION) {
			callback = options;
			options = null;
		}
		
		if(typeof callback !== consts.FUNCTION) {
			callback = $.noop;
		}
		
		options				= options || {};
		options.id			= id;
		options.callback	= callback;
		
		this.each(fn.onEachElement(options));
		
	};
	
	fn = jwave.fn = {
		
		loaded: false,
		
		queue: [],
		
		onEachElement: function(options) {
			
			return function(handler, target) {
			
				handler = fn.getWaveHandler(target, options);
				
				if(fn.loaded) {
					handler.call(target);
				} else {
					fn.queue.push(handler);
				}
				
			};
			
		},
		
		getWaveHandler: function(target, options) {
			
			return function(panel, callback) {
				options.target = target;
				panel = new google.wave.WavePanel(options);
				callback = fn.bindCallback(panel, options.callback);
				panel.loadWave(options.id);
				doc.getElementById(panel.getFrameId()).onload = callback;
			};
			
		},
		
		bindCallback: function(panel, callback) {
			
			return function() {
				callback.call(panel, panel);
			};
		
		},
		
		onGoogleApiReady: function(script) { 
			
			if(typeof google !== consts.UNDEFINED && typeof gadgets !== consts.UNDEFINED) {
				google.load("wave", "1", {callback: fn.onGoogleWaveApiReady});
			}
			
		},
		
		onGoogleWaveApiReady: function(i, len) {
			
			fn.loaded = true;
			len = fn.queue.length;
			for(i=0;i<len;i++) {
				fn.queue[i].call(fn.queue);
			}
			
		},
		
		loadGoogleApi: function(script) {
			
			if(typeof google === consts.UNDEFINED || typeof gadgets === consts.UNDEFINED) {
				if (typeof gadgets === consts.UNDEFINED) {
					script		= doc.createElement(consts.SCRIPT);
					script.src	= "https://wave.google.com/gadgets/js/core:rpc";
					script.onload = fn.onGoogleApiReady;
					consts.head.appendChild(script);	
				}
				if (typeof google === consts.UNDEFINED) {
					script		= doc.createElement(consts.SCRIPT);
					script.src	= "http://www.google.com/jsapi?callback=jQuery.fn.jwave.fn.onGoogleApiReady";
					consts.head.appendChild(script);	
				}
			} else if(typeof google.wave === consts.UNDEFINED) {
				fn.onGoogleApiReady();
			} else {
				fn.onGoogleWaveApiReady();
			}
			
		},
		
		isWaveId: function(id) {
			return id && typeof id === "string" && /^googlewave.com!w\+[A-Za-z0-9]+(\.[0-9]+)*$/.test(id);
		}
		
	};
	
	$(fn.loadGoogleApi);
	
})(jQuery, document);