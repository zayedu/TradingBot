# utils.py
import threading

def run_in_main_thread(target, *args):
    if threading.current_thread() is threading.main_thread():
        target(*args)
    else:
        raise RuntimeError("This function must be run in the main thread")
