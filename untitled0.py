import cv2
#import numpy as np
def crop(start_raw,start_col,end_raw,end_cal):
    img=cv2.imread("face_5.png")
    height, width = img.shape[:2]
    
    
    
    start_raw, start_col = int(height* float(f1)), int(width *float(f2))
    end_raw, end_cal= int(height* float(f3)), int(width* float(f4))
    c_img=img[start_raw:end_raw,start_col:end_cal]
    
    
    
    cv2.imshow("Orginal Immage",img)
    cv2.waitKey(0)
    cv2.imshow("Croped Immage",c_img)
    cv2.waitKey(0)

i=1
while i<=1:
  
 f1=float(input('Enter The start rawing  Factor'))
 f2=float(input('Enter The start_col  Factor'))
 f3=float(input('Enter The end_rawg  Factor'))
 f4=float(input('Enter The end_cal  Factor'))
 i=i+1    
 crop(f1,f2,f3,f4)
 cv2.destroyAllWindows()
 