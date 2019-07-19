# DjangoRESTframework-JWT



REST service that can fetch bank details, using the data given in the API’s query parameters.

This is JWT authenticated. You will need a valid access tocken inorder to access contents from this API.



<h3>API formats:</h3>
1. GET API to fetch a bank details, given branch IFSC code :  	curl -X GET -H 'Accept: application/json' -H "Authorization: Bearer {access token here}" https://fyleapi.herokuapp.com/?ifsc={ifsc code here}

   <br>

2. GET API to fetch all details of branches, given bank name and a city :    curl -X GET -H 'Accept: application/json' -H "Authorization: Bearer {access token here}"  https://fyleapi.herokuapp.com/?bank={bank name here}/city={city name here}



<h3>Example API calls:</h3>
1. IFSC:	curl -X GET -H 'Accept: application/json' -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTYzOTY0OTMzLCJqdGkiOiJhNDJlODU3ZGIzNTI0NmIxOTc1ZjU1OGQ3ZWU0ZjhiZSIsInVzZXJfaWQiOjF9.arJWRI1IS35VYMxABOP20ESUPwnPdpWCM67woSEJ14U"  https://fyleapi.herokuapp.com/?ifsc=ABHY0065003

   <br>

2. BANK/CITY:     curl -X GET -H 'Accept: application/json' -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTYzOTY0OTMzLCJqdGkiOiJhNDJlODU3ZGIzNTI0NmIxOTc1ZjU1OGQ3ZWU0ZjhiZSIsInVzZXJfaWQiOjF9.arJWRI1IS35VYMxABOP20ESUPwnPdpWCM67woSEJ14U" -G "https://fyleapi.herokuapp.com/?" --data-urlencode "bank=ABHYUDAYA COOPERATIVE BANK LIMITED/city=MUMBAI" 

<br><br>

<h3>Including Offset and Limits:</h3>
Example Request:	[ limit = 10 | offset = 3]

curl -X GET -H 'Accept: application/json' -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTYzOTY0OTMzLCJqdGkiOiJhNDJlODU3ZGIzNTI0NmIxOTc1ZjU1OGQ3ZWU0ZjhiZSIsInVzZXJfaWQiOjF9.arJWRI1IS35VYMxABOP20ESUPwnPdpWCM67woSEJ14U" -G "https://fyleapi.herokuapp.com/?" --data-urlencode "bank=ABHYUDAYA COOPERATIVE BANK LIMITED/city=MUMBAI/limit=10/offset=3"

