from winotify import Notification, audio
import time

notifier = Notification(
    app_id="PDFIY",
    title="image.png",
    msg="File does not exist",
    icon="C:\\Users\\ismail\\dev\\side-projects\\pdfiy\\pdfiy.ico",
    duration="short")
notifier.set_audio(audio.Default, loop=False)
notifier.show()