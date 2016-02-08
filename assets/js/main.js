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
