#!/usr/bin/python
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from subprocess import Popen

#monitors a directory and executes a subprocess when a given file is created
#in that directory

print ('monitoring creation events')

class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        createdFile = '~/exampleFile.py'
        reactionScript = '~/exampleScript.py'
    
        print(f'event type: {event.event_type}  path : {event.src_path}')
        if (event.src_path == createdFile):
            print(f'{createdFile} created!')
            p = Popen(reactionScript)
            stdout, stderr = p.communicate()


if __name__ == "__main__":
    monitoredDirectory = "~/exampleDirectory"
    
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path= monitoredDirectory, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
    