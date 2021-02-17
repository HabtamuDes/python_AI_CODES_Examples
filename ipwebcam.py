import urllib.request
import cv2
import numpy as np

url= "http://10.3.141.168:8080/shot.jpg"

while True:
    imgResp = urllib.request.urlopen(url)
    imgNp = np.array(bytearray(imgResp.read()),dtype=np.uint8)
    img = cv2.imdecode(imgNp,-1)
    cv2.imshow("From Wireless Mob-Camera", img)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
cv2.destroyAllWindows()
