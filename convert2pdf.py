import img2pdf
import os
import sys
import PyPDF2

folder = sys.argv[1]

if not os.path.exists(str(folder)):
    print("Folder does not exist. 文件夹不存在。")

with open('output.pdf', 'wb') as f:
    pics = os.listdir(str(folder))
    pics.sort()
    file_list = []
    for pic in pics:
        # f.write(img2pdf.convert([i for i in os.listdir(str(folder)) if i.endswith(".jpg")]))
        file_name = "{}/{}".format(folder, pic)
        file_list.append(file_name)
    f.write(img2pdf.convert(file_list))
