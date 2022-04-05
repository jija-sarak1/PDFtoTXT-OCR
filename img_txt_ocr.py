from PIL import Image
import pyocr
import pyocr.builders

tools = pyocr.get_available_tools()
tool = tools[0]
langs = tool.get_available_languages()
lang = langs[0]
tool = pyocr.get_available_tools()[0]
builder = pyocr.builders.TextBuilder()
font = ['Aclonica','Amatic sc','Arial','Calibri','Courier','Helvetica neue','Jua','Lobster','pattaya','Times New Roman']
images =['Aclonica.png','Amatic sc.png','Arial.png','Calibri.png','Courier.png','Helvetica neue.png','Jua.png','Lobster.png','pattaya.png','Times New Roman.png']
i = 0
while i < len(images):
    txt = tool.image_to_string(
        Image.open("/home/jija/Desktop/files/OCR imgtotxt/images/"+images[i]),
        lang=lang,
        builder=builder
    )
    print(str(i+1) +".","Font" ,font[i],'\n','\n')
    print(txt)

    f = open(r"/home/jija/Desktop/files/OCR imgtotxt/output_txt/"+str(font[i]+"_img")+".txt", "w")
    f.write(txt)
    f.close()
    i+=1
    print('\n','\n')

