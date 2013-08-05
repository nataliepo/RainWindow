import requests
import settings
import sys

# https://api.usergrid.com/my-org/my-app/events {"counters" : {"button_clicks" : 1},"timestamp" : "0"}


# receive a token.
# POST /token '{"grant_type":"client_credentials", "client_id":"{client_id}", "client_secret":"{client_secret}"}'


#      xhr.setRequestHeader("Authorization", "Bearer " + self.getToken());


### from: http://apigee.com/docs/usergrid/content/authentication-and-access-usergrid
# curl -X POST -i -H 
# "Content-Type: application/json" 
# "https://api.usergrid.com/my-org/my-app/token" -d '{"grant_type":"client_credentials","client_id":"YXB7NAD7EM0MEeJ989xIxPRxEkQ","client_secret":"YXB7NAUtV9krhhMr8YCw0QbOZH2pxEf"}'
# curl -X POST -i -H "Content-Type: application/json" "https://api.usergrid.com/changpo/rainwindow/token" -d '{"grant_type":"client_credentials","client_id":"YXA6iCCAsP1iEeKVBuXmgPGLgw","client_secret":"YXA6vvr9e3576qMazvQKxLb5mv2l7RI"}'

# RESULT:
# {
#	"access_token":"YWMtbvriwP1rEeK_w1PPZI4T1QAAAUBwEH7sy7g4MaBaW5r7ayNWxccrL44RHDk",
# 	"expires_in":604800,
# 	"application":"882080b0-fd62-11e2-9506-e5e680f18b83"
# }

headers = {
	"grant_type": "client_credentials", 
	"client_id": settings.APIGEE_AUTH['client_id'], 
	"client_secret": settings.APIGEE_AUTH['secret'],
	'Authorization': settings.APIGEE_AUTH['secret']
}
r = requests.post("%s/%s/%s/token" % (settings.APIGEE_AUTH['base_url'],
									  settings.APIGEE_AUTH['org'],
									  settings.APIGEE_AUTH['app']), 
				  headers=headers)
									  
sys.stderr.write("result: %s\n" % r)
							
sys.exit(1)		  



# /key-check method
r = requests.get("%s/%s/%s/ticket" % (settings.APIGEE_AUTH['base_url'],
									  settings.APIGEE_AUTH['org'],
									  settings.APIGEE_AUTH['app']),
				)


sys.stderr.write("result: %s\n" % r)
assert(r.json()['success'])
print(r.json())