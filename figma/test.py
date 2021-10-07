import requests
import math, random

digits = "0123456789"
OTP = ""

# length of password can be changed
# by changing value in range
for i in range(4):
    OTP += digits[math.floor(random.random() * 10)]

otp = OTP
print(otp)

url = "https://www.fast2sms.com/dev/bulkV2"

querystring = {
    "authorization": "JLEw8Sjmh0VQaPUd7NfgyOX2ixbGrqHI1DMcA4pBCzs5tvnW9Ke3gLvcS0a4fjGAilUsJRw5yECdpKko",
    "message": otp,
    "language": "english",
    "route": "q",
    "numbers": "6382519268"
    }

headers = {
    'cache-control': "no-cache"
}
try:
    response = requests.request("GET", url,
                                headers=headers,
                                params=querystring)

    print("SMS Successfully Sent")
except:
    print("Oops! Something wrong")