import subprocess


def open_notepad():                                                     # TODO zmienić na subprocess.run()
    notepad = subprocess.Popen('C:\\Windows\\System32\\Notepad.exe')    # TODO import pathlib lub coś innego
    return notepad


open_notepad()
