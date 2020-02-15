from PIL import Image
import pytesseract

file = 'IMG_2.jpg'

if __name__ == '__main__':
    f = open('text_photo.txt', 'w', encoding='utf-8')

    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    print("Process has begun")
    print(pytesseract.image_to_osd(Image.open(file)))
    text = pytesseract.image_to_string(Image.open(file), lang='eng')
    if text is '':
        print("Fail, the picture is empty")
    else:
        print("Successful")
        f.write(text)
    f.close()
