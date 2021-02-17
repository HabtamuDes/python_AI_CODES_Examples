import urllib.request
import cv2
import numpy as np
from PIL import Image
import pytesseract


url= "http://10.221.190.20:8080/shot.jpg"

while True:
    imgResp = urllib.request.urlopen(url)
    imgNp = np.array(bytearray(imgResp.read()),dtype=np.uint8)
    img = cv2.imdecode(imgNp,-1)
    cv2.imshow("From Wireless Mob-Camera", img)
    text = pytesseract.image_to_string(img, lang = 'eng')


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
print(text)
# When everything is done, release the capture
cv2.destroyAllWindows()
