(function poll() {
    setTimeout(function() {
       
        $.ajax({
            type: "GET",
            success: function(data) {
                var $response = $(data);
                var after = parseInt($response.find("#overall").text());
                var before = parseInt($("#overall").text());
                var overall = parseInt($("#req").text());
                if (after !== before) {
                    var new_requests = after-before;
                    var sum = overall + new_requests;
                    $request = $(data).find('#request');
                    $("#request").html($request);
                    $("#req").text(sum);
                    $("#title").text(sum + " " + "new requests")
                };

                if (document.hasFocus()===true){
                    $("#req").html("0");
                    $("#title").text("0 new requests")
                };
            },
            complete: poll,
            timeout: 2000
        })
    }, 3000);
})();

// datepicker function 
$('.datepicker').datetimepicker({
    'format': 'YYYY-MM-DD'
});

// contact edit function
var $form = $('#contact_form');
var $success_indicator = $('#ajax-success-indicator');
var $progress_indicator = $('#ajax-progress-indicator');

function display_form_errors(errors, form) {
    for (var k in errors) {
        $form.find('input[name=' + k + ']').after('<div class="error">' 
          + errors[k] + '</div>');
    }
}

var options = {
  dataType: 'json',
  beforeSubmit: function(){
            $progress_indicator.show();
            $success_indicator.hide();
            $('#send_button').attr('disabled', true)
          },
  success: function(data,statusTest, xhr, $form){
            $form.find('.error').remove();
            if (data['result'] == 'success'){
                $success_indicator.show();
            }
            else if (data['result'] == 'error') {
                display_form_errors(data['response'], $form);
            }
            $progress_indicator.hide();
            $('#send_button').attr('disabled', false)
          }
}

$form.ajaxForm(options);
