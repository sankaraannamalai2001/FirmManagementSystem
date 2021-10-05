from captcha.image import ImageCaptcha

image = ImageCaptcha(width = 280, height = 90)
import string
import random
S = 5

ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k = S))
captcha_text = str(ran)

data = image.generate(captcha_text)
image.write(captcha_text, 'CAPTCHA.png')