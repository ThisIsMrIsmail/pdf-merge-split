import os
your_path = '/home/username/Documents/Python/test.hello.pdf'
print(os.path.basename(your_path).split(".pdf")[0])