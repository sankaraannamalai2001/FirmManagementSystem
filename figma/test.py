from captcha import ImageCaptcha
image = ImageCaptcha(width=280,height=80)
msg = "hello"
res = image.generate(msg)
image.write(msg,"captcha.png")