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
        counter = 1
        if "Screenshot" in filename:
            # base_filename = f"SS_{time.strftime('%m-%d-%y_%I.%M %p').replace('_0', '_')}" # with year
            base_filename = f"SS_{time.strftime('%m-%d_%I.%M %p').replace('_0', '_')}"
            ext = ".png"
        else:
            # base_filename = f"SR_{time.strftime('%m-%d-%y_%I.%M %p').replace('_0', '-')}" # with year
            base_filename = f"SR_{time.strftime('%m-%d_%I.%M %p').replace('_0', '_')}" 
            ext = ".mov"

        new_filename = f"{base_filename}{ext}"

        # Check if the file exists and append an integer suffix if it does
        while os.path.exists(os.path.join(directory, new_filename)):
            new_filename = f"{base_filename}_{counter}{ext}"
            counter += 1

        src_path = src_path.replace('.Screen', 'Screen')
        try:
            self.wait_for_file(str(src_path))
            os.rename(src_path, os.path.join(directory, new_filename))
            
        except:
            os.rename(src_path.replace("\u202F", " "), os.path.join(directory, new_filename))

    def wait_for_file(self, file_path, timeout=3):
        start_time = time.time()
        while True:
            if os.path.exists(file_path):
                print(file_path, "exists")
                if os.path.getsize(file_path) > 0:
                    return True
            if time.time() - start_time >= timeout:
                return False 
            time.sleep(0.1)  


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
