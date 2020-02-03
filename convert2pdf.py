import img2pdf
import os
import sys
import PyPDF2

folder = sys.argv[1]

if not os.path.exists(str(folder)):
    print("Folder does not exist. 文件夹不存在。")

with open('output.pdf', 'wb') as f:
    pics = os.listdir(str(folder))
    for pic in pics:
        num = pic.replace(".jpg", "")
