import sys 
import time 
import random 
import os 
import shutil
from watchdog.observers import Observer 
from watchdog.events import FileSystemEventHandler

from_dir=""
to_dir =""

list_of_files=os.listdir(from_dir)
print(list_of_files)

for file_name in list_of_files:
    name,extension,=os.path.splitext(file_name)
    print(name)
    print(extension)
    if extension==" ":
        continue
    if extension in['.gif','.png','.jpg','.jpeg','jfif']:
        path1=from_dir + '/'+file_name
        path2=to_dir+'/'+"Image_Files"
        path3=to_dir+'/'+"Image_Files"+'/'+file_name
        print("path1",path1)
        print("path3",path3)
    if os.path.exists(path2):
        print("Moving"+file_name+".....")
        shutil.move(path1,path3)
    else:
        os.makedirs(path2)
        print("Moving"+file_name+".....")
        shutil.move(path1,path3)
        
class FileEventHandler(FileSystemEventHandler):

    def on_created(self,event):
        print("Hey,{event.src_path} has been created!")
    def on_deleted(self,event):
        print("Oops!Someone deleted {event.src.path}!")
    def on_modified(self,event):
        print("Hey!the {event.src.path} is modified! ")
    def on_moved(self,event):
        print("Hey! the {event.src.path} is moved")

        try:
            while True:
                time.sleep(2)
                print("running...")
        except KeyboardInterrupt:
            print("stopped!")
            observer.stop()

class FileMovementHandler(FileSystemEventHandler):
    def on_created(self,event):
        print(event)
    #Initialie Event Handler Class
    event_handler=FileMovementHandler()
    
    #Initialize Observer
    observer=Observer()

    #Schedule the Observer
    observer.schedule(event_handler,from_dir,recursive=True)

    #Start the Observer
    observer.start()