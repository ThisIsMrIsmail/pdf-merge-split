import sys
import subprocess
from time import sleep

def main():
    sleep(1)
    print(sys.argv)
    sleep(3)
    # if len(sys.argv) == 1:
        # subprocess.run(['/path/to/my.exe', path])
    # else:
        # print('Usage myscript.py <path>')

if __name__ == "__main__":
    main()