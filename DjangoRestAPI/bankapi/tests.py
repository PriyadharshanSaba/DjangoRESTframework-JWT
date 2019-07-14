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


http http://127.0.0.1:8000/?ifsc=ABHY0065003 "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTYzMTIyMTIxLCJqdGkiOiIzY2ZjYzQzMGRkMjA0NTUwYjE4Y2M2YmU1NTViYjNiYiIsInVzZXJfaWQiOjF9.ku_N1nilyALRxxzpMxGunKEhJkzx1ft8Ckdy_dDeDDs"


curl -H 'Accept: application/json' -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTYzMTE1NTYwLCJqdGkiOiI1MmMxZDlmODk5ZTY0YThiYjIzZTE4OWM2NmI1MGY2YSIsInVzZXJfaWQiOjF9.DhogyKmMV96ckotiMWdasTNaHX0OW_DpetWhqJ8IPHQ" http://127.0.0.1:8000/hello/

curl -X GET -H 'Accept: application/json' -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTYzMTE1MTk0LCJqdGkiOiIzNWE1OTYyZTE4MzQ0ODU3YjMxMDM2N2RiNzRiMWE5NSIsInVzZXJfaWQiOjF9.wwHPQjw7yf2_JGT-g88tOLXbnnvw1bvZDRPVg6wpcBg" http://127.0.0.1:8000/?ifsc=ABHY0065003
"""
