import PIL.Image as Image,PIL.ImageFont as ImageFont,PIL.ImageDraw as ImageDraw

image1 = Image.open("D:\\huangLeiPictures\\cat.jpg")
draw = ImageDraw.Draw(image1)

ft = ImageFont.truetype("C:\\WINDOWS\\Fonts\\STXINGKA.TTF",120)
draw.rectangle((180,100,900,900),outline = "red")
draw.text((200,400),"黄雷必胜",font=ft,fill="blue")
image1.save("D:\\huangLeiPictures\\cat_new_wallpaper2.jpg","JPEG")