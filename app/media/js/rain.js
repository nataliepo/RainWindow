



jQuery(document).ready(function () {

	jQuery.fn.updateWaitingStatus = function() {
		$.fn.checkForAccess();
	};
	
	jQuery.fn.getTicketNumber = function() {
		return $('#ticket_number').attr('value');
	};
	jQuery.fn.checkForAccess = function() {      
		var api_url = '/api/check_line.json?ticket_number=' + $.fn.getTicketNumber();
	
		$.ajax({
			type: "GET",
			url: api_url,
			contentType: "application/json",
			data: '',
			success: function(data) {
				console.log("Response from endpoint: ", data);
				if (data['access'] == true) {
					$('#access_status').html("Yes! You are in the rain room.");
				}
				else {
					$('#access_status').html("Not yet. There are " + 
							data['num_waiting'] + " in line in front of you.");
				}
			},
			error: function(error) {
				console.log("Error:", error);
			}
		});
	};

	jQuery.fn.leaveRainRoom = function() {      

		var api_url = '/api/leave.json';
	
		$.ajax({
			type: "GET",
			url: api_url,
			contentType: "application/json",
			data: '',
			success: function(data) {
				console.log("Response from endpoint: ", data);
			},
			error: function() {
			}
		});
	};

	/*
	$('.container').mousemove(function(e){
		console.log("mouse: (" + e.pageX + ", " + e.pageY + ")");
	});
	*/
	

	// $(window).unload(function(){

	$("#fake_leave").click(function(e){

		e.preventDefault();
		
		$.fn.leaveRainRoom();
		console.log("LEAVE!");
	});
	
	
	$('#access_check').click(function(e) {
		e.preventDefault();
		
		$.fn.checkForAccess();
		
		console.log("checked.");
	});
	
	$(window).unload(function() {
		$.fn.leaveRainRoom();
	});
	
	console.log("page loaded");


	$.fn.updateWaitingStatus();

});


function js_leaveRainRoom(ticket_number) {
	if (ticket_number == undefined) {
		ticket_number = document.getElementById('ticket_number').value;
	}
	var xhReq = new XMLHttpRequest();
	var api = "/api/leave.json?ticket_number=" + ticket_number;
	
	xhReq.open("GET", api);
	xhReq.send(null);
}

window.onbeforeunload = function() {
    // return 'Are you sure you want to navigate away from this page?';
	js_leaveRainRoom(document.getElementById('ticket_number').value);
};
