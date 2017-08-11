import PIL.Image as Image
import PIL.ImageFilter as ImageFilter

im = Image.open("D:\\huangLeiPictures\\cat.jpg")   #打开图片
w,h = im.size   #获取图片的像素，其值为象素意义上的宽和高
print(im.format)   #获取图片格式
print(im.size)    #获取图片像素
im.thumbnail((w//2,h//2))   #缩放图片大小为原来的一半
im.save("D:\\huangLeiPictures\\cat_QQ_backup.jpg",'jpeg')    #保存图片，以及保存格式为jpeg
#im.show()    #显示图片
print(im.mode)    #显示模式。 RGB（true color image），此外还有，L（luminance），CMTK（pre-press image）。
box = (100,100,200,200)
s = im.crop(box)   #图像中提取出某个矩形大小的图像。它接收一个四元素的元组作为参数，各元素为（left, upper, right, lower），坐标系统的原点（0, 0）是左上角。
#s.show()
#s = s.transpose(Image.ROTATE_180)   #旋转180°
#im.paste(s,box)   #粘贴
#im.show()

im = Image.open("D:\\huangLeiPictures\\cat.jpg")
im2 = im.filter(ImageFilter.EMBOSS)
im2.save("D:\\huangLeiPictures\\cat_QQ_2.jpg",'jpeg')
#im2.show()

newImg = Image.new("RGBA",(640,480),(0,255,0))  #创建一张大小为640*480颜色为绿色的图片
newImg.save("D:\\huangLeiPictures\\cat_newImg.png","PNG")

''' http://www.cnblogs.com/ping-y/p/6212089.html'''
