import os

com = 'ffmpeg -re -i bbbVideo1.mp4 -c:a copy -f mpegts "udp://127.0.0.1:1234"'

os.system(com)


