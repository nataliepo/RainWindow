// old apigee stuff that did not work

	var token = '';
	
	// Initializing the SDK
	var client = new Usergrid.Client({
		orgName:'changpo', 
		appName:'rainwindow',
		// accessToken: token
	});
	
	
	client.setToken(token);
	
	
	// fetch how many events there are.
	var options = {
		method:'GET',
		endpoint:'tickets'
	};
	client.request(options, function (err, data) {
		if (err) {
			// Error - GET failed
			console.log("GET error: ", err);
		} else {
			console.log("GET response: ", data);
			// Data will contain raw results from API call
			// Success - GET worked
		}
	});
	
	
	// Initializing the SDK
	/*
			var client = new Usergrid.Client({
				orgName:'changpo', // Your Usergrid organization name (or apigee.com username for App Services)
				appName:'rainwindow', // Your Usergrid app name

			});

			// Make a new "book" collection and read data
			var options = {
				type:'books',
				qs:{ql:'order by created DESC'}
			}

			var books;

			client.createCollection(options, function (err, books) {
    			if (err) {
    				alert("Couldn't get the list of books.");
    			} else {
    				while(books.hasNextEntity()) {
    					var book = books.getNextEntity();
    					alert(book.get("title")); // Output the title of the book
    				}
    			}
    		});

			// Uncomment the next 4 lines if you want to write data

			// book = { "title": "the old man and the sea" };
			// books.addEntity(book, function (error, response) {
			// 	if (error) { alert("Couldn't add the book.");
			// 	} else { alert("The book was added."); } });
	
	*/