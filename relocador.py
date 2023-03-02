import sys
import time 
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:\Users\Usuario\teste>
class FileEventHandler(FileSystemEventHandler):
    def on_created(self, event):
        print(f"esse arquivo foi {event.src_path} criado!")
    
    def on_deleted(self, event):
        print(f"esse arquivo foi {event.src_path} deletado")
    
    def on_modified(self, event):
        print(f"esse arquivo foi {event.src_path} modificado")

    def on_moved(self, event):
        print(f"esse arquivo foi {event.src_path} movindo")

event_hadler = FileEventHandler()
observer = Observer()
observer.schedule(event_hadler, from_dir, recursive=True)
observer.start()

try:
    while True:
        time.sleep(2)
        print("executando.....")
except KeyboardInterrupt:
    print("Interrompido!")
    observer.stop()
