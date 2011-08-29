$(function(){
	
	$("form").submit(function(form, button){
		
		form = $(this);
	
		button = form.find("button").attr("disabled", "disabled").addClass("ui-state-disabled");
		
		$.ajax({
			
			dataType: "json",
			
			data: form.serialize(),
			
			type: "POST",
			
			url: form.attr("action"),
			
			error: function() {
				
				modal({
					
					icon: "alert",
					
					title: "Oh No!",
					
					message: "It seems as though there is a problem communicating with the server. Please try your request again later."
					
				});
				
			},
			
			success: function(data) {
				
				modal({
					
					icon: data.code === 200 ? "info" : "alert",
					
					title: data.title,
					
					message: data.message
					
				});
				
				if (data.code === 200) {
				
					form.find("input[type='text'], textarea").val("");
					
				}
				
				Recaptcha.reload();
				
			},
			
			complete: function() {
				
				button.attr("disabled", "").removeClass("ui-state-disabled");
				
			}
			
		});
		
		return false;
		
	});
	
	$('#body').autoResize();
	
});