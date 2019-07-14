from django.test import TestCase

# Create your tests here.

"""


curl \
  -X POST \
  -H "Content-Type: application/json" \
  -d '{"username": "pd", "password": "123"}' \
  http://127.0.0.1:8000/api/token/



curl -i -H  http://127.0.0.1:8000/hello/ "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTYzMTE0NjQxLCJqdGkiOiI4NTZhZjQ0NWY3ODU0NDgwOTUyZjFkMGU1YmVkZGU2MyIsInVzZXJfaWQiOjF9.0VGyTH0T95qUg-gLeXAa9rPQbroNnSkD585UgFpAWMU"


eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTYzMTEyNzE0LCJqdGkiOiIwNzU5ODA3Y2JlODU0NjMxYTdhYjkzNGFlOWQ0NzI5ZCIsInVzZXJfaWQiOjF9.mF-WULlBPcZ19IN4kSR53ey5DCJnwm7lFCurPeKXYzM


http http://127.0.0.1:8000/?ifsc=ABHY0065003 "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTYzNTU3MDU4LCJqdGkiOiJjZWQyYTQyYzQwMjU0OTI5OTE3NDNhMTY1OThjOGU2MyIsInVzZXJfaWQiOjF9.kkE4Fe6xb49C3Qs7UpknVS1VluvbnwN_x0FGsVO9vuc"


curl -H 'Accept: application/json' -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTYzMTE1NTYwLCJqdGkiOiI1MmMxZDlmODk5ZTY0YThiYjIzZTE4OWM2NmI1MGY2YSIsInVzZXJfaWQiOjF9.DhogyKmMV96ckotiMWdasTNaHX0OW_DpetWhqJ8IPHQ" http://127.0.0.1:8000/hello/

curl -X GET -H 'Accept: application/json' -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTYzMTI0NzcwLCJqdGkiOiI0NDZmYWQ4ZmJmNTg0NzU2YTg5Y2Y2NTk0NmFlNzhjZiIsInVzZXJfaWQiOjF9.k-MtaC3YfLYwGL-QjuB10sBpgRVJC9QY93mF-2FNDR8" http://127.0.0.1:8000/?ifsc=ABHY0065003

['ABHY0065001', 'RTGS-HO', 'ABHYUDAYA BANK BLDG., B.NO.71, NEHRU NAGAR, KURLA (E), MUMBAI-400024', 'MUMBAI', 'GREATER MUMBAI', 'MAHARASHTRA', '60']



"""
