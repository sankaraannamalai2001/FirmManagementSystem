# import requests
# import math, random
#
# digits = "0123456789"
# OTP = ""
#
# # length of password can be changed
# # by changing value in range
# for i in range(4):
#     OTP += digits[math.floor(random.random() * 10)]
#
# otp = OTP
# print(otp)


import requests, math, random

url = "https://www.fast2sms.com/dev/bulkV2"
digits = "0123456789"
OTP = ""
for i in range(4):
    OTP += digits[math.floor(random.random() * 10)]

otp = OTP
print(otp)
querystring = {
    "authorization": "ysBq4GOZykH2OrmqabVvHiEfy61jEidM5XPWg4ebaaMbJbUlBkOlhr0qZjoa",
    "message": otp,
    "language": "english",
    "route": "q",
    "numbers": "6383519268"}

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