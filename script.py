from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import time

class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        print(f'event type: {event.event_type}  path: {event.src_path}')
        if "Screenshot" in event.src_path or "Screen Recording" in event.src_path:
            self.rename_file(event.src_path)
            
    def rename_file(self, src_path):
        directory, filename = os.path.split(src_path)
        if "Screenshot" in filename:
            new_filename = f"SS_{time.strftime('%m-%d-%y_%I.%M%p')}.png"
        else:
            new_filename = f"SR_{time.strftime('%m-%d-%y_%I.%M%p')}.mov"
        os.rename(src_path, os.path.join(directory, new_filename))

if __name__ == "__main__":
    event_handler = MyHandler()
    observer = Observer()
    path = os.path.expanduser("~/Desktop")
    observer.schedule(event_handler, path, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
