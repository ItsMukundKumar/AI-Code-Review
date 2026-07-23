import subprocess


def getDiff():
    return subprocess.check_output(['git', 'show'], text=True)


print(getDiff())