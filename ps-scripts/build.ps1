pyinstaller --onefile --exclude pip --noconsole --icon=pdfiy.ico pdfiy.py
cp dist/pdfiy.exe release/pdfiy.exe