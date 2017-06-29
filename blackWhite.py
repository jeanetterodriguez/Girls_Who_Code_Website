from PIL import Image

#import the image
myImage= Image.open("ele2.jpg")
imageData = myImage.getdata ()
pixellist= list(imageData)

newPixellist=[]

#pixel manipulation
for pixel in pixellist:
    red=pixel[0]
    green=pixel[1]
    blue=pixel[2]
    avg=(red+green+blue)//3


   
    
    

    newRed=avg
    
    newGreen=avg
   
    newBlue=avg
   


        
    
    p=(average, average, average)
    

#add pixel to new pixel list
    newPixellist.append(p)

#open the image
newImage=Image.new("RGB",myImage.size)
newImage.putdata(newPixellist)
newImage.show()
#newImage.save("newPhoto.jpeg","jpeg")
