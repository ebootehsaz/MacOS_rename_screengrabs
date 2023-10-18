# Auto Rename Screen Recordings and Screenshots on macOS

This README explains how to automatically rename screen recordings and screenshots on macOS using a Python script and `launchd`.

## Prerequisites

- Python 3.x
- `watchdog` library
- A macOS system

## Installation

### Step 1: Install watchdog

First, install the `watchdog` Python package:

```bash
pip3 install watchdog
```

### Step 2: Copy Python Script

Copy the Python script with the code and save it, for example, as `script.py`.

### Step 3: Configure plist File

The repository includes a `.plist` file named `com.my_screen_rename.plist` that you can use to schedule the script with `launchd`. Follow the steps below to configure it:

1. **Download and Modify the plist File**: Download the `com.my_screen_rename.plist` from this repository. Open it with a text editor and replace `/path/to/your/watch_screenshots.py` with the full path where you saved your `watch_screenshots.py`. Open it with a text editor and replace `/path/to/python` with the full path where your Python executable is located. You can find this path by running `which python3` in the terminal.


2. **Move the plist File**: Move the modified `com.my_screen_rename.plist` to `~/Library/LaunchAgents/` directory:

    ```bash
    mv com.my_screen_rename.plist ~/Library/LaunchAgents/
    ```

3. **Load the plist File**: Register it with `launchd` by running the following command in the terminal:

    ```bash
    launchctl load ~/Library/LaunchAgents/com.my_screen_rename.plist
    ```

Now, the Python script will automatically run whenever you log in to your macOS system. To check the status, run:

```bash
launchctl list | grep com.my_screen_rename
```

To unload the script, execute:
```
launchctl unload ~/Library/LaunchAgents/com.my_screen_rename.plist
```

## Frequently Asked Questions (FAQ)

### Q1: How do I check if the `launchd` job is running?

Run the following command in the terminal:

```bash
launchctl list | grep com.my_screen_rename
```

If you see an output similar to the one below, it means the script is running successfully:
```
17403   0       com.my_screen_rename
```

Otherwise, you can check the logs to determine what the error is:
```
cat /tmp/watch_screenshots.stderr
```



### V1
Basic functionality
- occasional problem with MacOS hidden naming convention
- file overwrite

### V1.1
- fixed file overwrite problem
- `launchctl` reloads script on crash
- more error handling
- fixed naming convention

