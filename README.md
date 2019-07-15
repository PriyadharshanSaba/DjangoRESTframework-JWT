# DjangoRESTframework-JWT



REST service that can fetch bank details, using the data given in the API’s query parameters.

This is JWT authenticated. You will need a valid access tocken inorder to access contents from this API.



<h3>API formats:</h3>
1. GET API to fetch a bank details, given branch IFSC code :  	curl -X GET -H 'Accept: application/json' -H "Authorization: Bearer {access token here}" https://fyleapi.herokuapp.com/?ifsc={ifsc code here} <br>
2. GET API to fetch all details of branches, given bank name and a city :    curl -X GET -H 'Accept: application/json' -H "Authorization: Bearer {access token here}"  https://fyleapi.herokuapp.com/?bank={bank name here}/city={city name here}



<h3>Example API calls:</h3>
1. IFSC:	curl -X GET -H 'Accept: application/json' -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTYzNTU3MDU4LCJqdGkiOiJjZWQyYTQyYzQwMjU0OTI5OTE3NDNhMTY1OThjOGU2MyIsInVzZXJfaWQiOjF9.kkE4Fe6xb49C3Qs7UpknVS1VluvbnwN_x0FGsVO9vuc" https://fyleapi.herokuapp.com/?ifsc=ABHY0065003 <br>
2. BANK/CITY: curl -X GET -H 'Accept: application/json' -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTYzNTY1NDQ0LCJqdGkiOiI2MmQ3Njg0YjRhZmE0Y2Y0OGQ4ZWUyNzY0M2E3NmE1ZCIsInVzZXJfaWQiOjF9.nhjEYpHIkYmoDHNSJXzQRwnLlAmQ3ghrCAkaaoelgvw" https://fyleapi.herokuapp.com/?bank=ABHYUDAYA_COOPERATIVE_BANK_LIMITED/city=MUMBAI <br>





