from paddleocr import PaddleOCR,paddleocr
import sys
import logging

#ocr不出现debug信息
paddleocr.logging.disable(logging.DEBUG)
#ocr的图片路径
img_name = sys.argv[1]
#paddleocr所用的语言，中文：ch，英文:en，繁体中文:chinese_cht
#pot的语言，中文简体：chi_sim，英文：eng，繁体中文：chi_tra

lang = sys.argv[2]
ocr = PaddleOCR(use_angle_cls=True,lang=lang)
result=ocr.ocr(img_name,cls=True)

#for line in result:
#	print(line)

for box in result[0]:
	print(box[1][0])