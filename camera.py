
import datetime
import os
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from picamera import PiCamera, Color
from time import sleep

# file and directory settings
datetime = datetime.datetime.today()
capture_file_name = datetime.strftime('%Y%m%d%H%M%S') + '.jpg'
save_directory_path = 'LOCAL DIRECTORY PATH'
google_drive_folder_id = 'GOOGLE DRIVE FOLDER PATH'

# OAuth
gauth = GoogleAuth()
gauth.CommandLineAuth()
drive = GoogleDrive(gauth)

# take picture
camera = PiCamera()
camera.resolution = (860, 600)
camera.annotate_background = Color('black')
camera.annotate_foreground = Color('white')
camera.annotate_text = datetime.strftime('%Y/%m/%d %H:%M:%S')
sleep(5)
camera.capture(save_directory_path + capture_file_name)

if os.path.exists(save_directory_path + capture_file_name) :
  # upload
  f = drive.CreateFile({
    'title': capture_file_name,
    'mimeType': 'image/jpeg',
    'parents': [{'kind': 'drive#fileLink', 'id':google_drive_folder_id}]
  })
  f.SetContentFile(save_directory_path + capture_file_name)
  f.Upload()

  #remove file
  os.remove(save_directory_path + capture_file_name)

else :
  f = drive.CreateFile({
    'title': datetime.strftime('%Y%m%d%H%M%S') + '.txt',
    'parents': [{'kind': 'drive#fileLink', 'id':google_drive_folder_id}]
  })
  f.SetContentString('file not found')
  f.Upload()
