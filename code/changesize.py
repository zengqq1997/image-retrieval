from PIL import Image
import os.path
import glob
import imghdr
def convertjpg(jpgfile,outdir,width=1080,height=600):
    img=Image.open(jpgfile)
    try:
        
        new_img=img.resize((width,height),Image.BILINEAR)   
        new_img.save(os.path.join(outdir,os.path.basename(jpgfile)))
    except Exception as e:
        print(e)
def changesize():
    for jpgfile in glob.glob("C:/Users/ZQQ/Desktop/advanced/study/computervision/classtest/image-retrieval/img/*.jpg"):
        imag=imghdr.what(jpgfile)
        print (imag)
        if (imag==None or imag=='png' or imag=='gif'):
            os.remove(jpgfile)
        else:
            convertjpg(jpgfile,"C:/Users/ZQQ/Desktop/advanced/study/computervision/classtest/image-retrieval/img/")
