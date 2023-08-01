import Image

#fluid64 = "Fluid64_half_size/00"
#fluid128 = "Fluid128_half_size/00"
#fluid512 = "Fluid512_half_size/00"
#fluid1024 = "Fluid1024_half_size/00"

out_image = "Fluid_all/00"

for pic in range(1, 26):
    blank_image = Image.open("blank.jpg")

    if pic < 10:
        image_num = "0"+str(pic)
    else:
        image_num = str(pic)

    #image64 = Image.open(fluid64+image_num+".jpg")
    #image128 = Image.open(fluid128+image_num+".jpg")
    #image512 = Image.open(fluid512+image_num+".jpg")
    #image1024 = Image.open(fluid1024+image_num+".jpg")
    image64 = Image.open("C:\Users\ASUS\Pictures\images\img_ask.jpg")
    image64 = Image.open("C:\Users\ASUS\Pictures\images\img_fdf.jpg")
    image64 = Image.open("C:\Users\ASUS\Pictures\images\img_hjk.jpg")
    image64 = Image.open("C:\Users\ASUS\Pictures\images\img_wer.jpg")
    out = out_image + image_num + ".jpg"

    #blank_image.paste(image64, (0,0)).paste(fluid128, (400,0)).paste(fluid512, (0,300)).paste(fluid1024, (400,300)).save(out)
    blank_image.paste(image64, (0, 0))
    #blank_image.paste(fluid128, (400, 0))
    #blank_image.paste(fluid512, (0, 300))
    #blank_image.paste(fluid1024, (400, 300))
    blank_image.save(out)