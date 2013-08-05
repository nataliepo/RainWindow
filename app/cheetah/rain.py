#def body

<div class="container">
	
	<input type="hidden" value="${ticket_number}" id="ticket_number" />
	
	
	<h3>Ticket #${ticket_number}</h3>
	
	
	#*
	<p>Fake <a id="fake_leave" onclick="js_leaveRainRoom()" href="http://www.29.io">Leave</a></p>
	*#
	
	
	
	
	<p>Do <a id="access_check" href="#">I have access</a> yet?</p>
	<h1 id="access_status">Checking...</h1>
	

	
	
</div>
#end def

#include "cheetah/shared/base.py"
