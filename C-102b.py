import cv2
import time
import random
import dropbox
def take_snapShot():
    number=random.randint(0,100)
    videoCaptureObject=cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame=videoCaptureObject.read()
        image_name="img"+str(number)+".png"
        cv2.imwrite(image_name,frame)
        start_time=time.time
        result=False
    return image_name
    print("Snapshot taken")
    videoCaptureObject.release()
    cv2.destroyAllWindows()

def upload_file(image_name):
    access_token="Sw4rol2bWC8AAAAAAAAAASEqu94jJqUu5X2D7zCb8UPMqR8GOmulikDzepRg_Rv9"
    file=image_counter
    file_from=file
    file_to="/newFolder/"+(image_name)
    dbx=dropbox.Dropbox(access_token)
    with open (file_from,"rb")as f:
        dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)
        print("file uploaded")

def main():
    while(True):
        if((time.time()-start_time)>=300):
            name=take_snapShot()
            upload_file(name)
main()
