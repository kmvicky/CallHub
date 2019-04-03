/* Project specific Javascript goes here. */

var stopDefaultFormSubmit = function($form) {

	if($form === undefined) {

		$(".ui.form").on("submit", function(event) {

			event.preventDefault();
			return false;

		});

	}

	else {

		$form.on("submit", function(event) {
			
			event.preventDefault();
			return false;

		});

	}

}

var submitForm = function() {

	$form = $("form.ui.form");
	stopDefaultFormSubmit($form)

	$form.on("click", "input[type=submit]", function(event) {

		var data = $form.serializeArray()
			.filter(function(item){
				if(item.value != "") {
					return item;
				}
			});
		
		var url = $form.attr("action");

		$.ajax({
			method: "post",
			url: url,
			data: data
		}).done(function(response) {

			var series_number = "Last number of fibonacci series is:"+ response.number

			var time = "Last number of fibonacci series is:"+ response.time

			$("h5.timetaken").html(time);
			$("h5.number").html(series_number);
			$("h5.error").html("");
			
		}).fail(function(xhr, responseJSON) {

			$("h5.number").html("");
			$("h5.timetaken").html("");

			$("h5.error").html("Fibonacci series could not be fetched");
		});
	});


}


$(document).ready(function() {
	submitForm();
});
