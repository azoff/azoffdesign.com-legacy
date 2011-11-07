(function($){
    $(function(){
        function onchange(event, value){ var 
            input = $(event.target),
            log = input.siblings('fieldset').children('.log'),
            name = input.attr('id'),
            formatted = event.type === 'change' ? input.val() : (value === undefined ? 'undefined' : value),
            text = [name, ': ', formatted, '\n', log.html()];
            log.html(text.join(''));
        }
        $('.changed input, .changed textarea, .changed select').changed(onchange);
        $('.change input, .change textarea, .change select').change(onchange);
    });
})(jQuery);