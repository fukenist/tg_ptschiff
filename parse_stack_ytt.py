import youtube_dl
import urllib.request
import re, os
import requests
import time

proxies = {"https" : "http://sergey.iliev:xxxxxxxx%5Bprerttr@54.81.231.53:8888"}


html = requests.get("https://www.youtube.com/c/peterschiff/videos", proxies=proxies)

video_ids = re.findall(r"watch\?v=(\S{11})", html.content.decode())
#get array of mp3s in folder 
mp3s = []
for x in os.listdir():    
    if x.endswith(".mp3"):
        mp3s.append(x)

ydl_opts = {
    'format': 'bestaudio/best',
    'cachedir' : 'False',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '96',
    }]
}
  
txt_file = open('outfile.txt', 'r')
file_content = txt_file.read()
content_list = file_content.split()
txt_file.close()

x = video_ids
y = content_list
print(x)
print(y)
result = set(x) - set(y)
print(result)
with open('outfile.txt', 'a') as outfile:
    outfile.write('\n'.join(result) + '\n')

def dwl_vid():
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([zxt])

for item in result:
    if len(item) == 11:    
        video_one = 'https://www.youtube.com/watch?v=' + item
        zxt = video_one.strip()
        dwl_vid()


new_mp3s = []
for x in os.listdir():    
    if x.endswith(".mp3"):
        new_mp3s.append(x)

print(mp3s)
print(new_mp3s)
result_mp3 = set(new_mp3s) - set(mp3s)
for x in result_mp3:
    base_url = "https://api.telegram.org/botxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

    my_file = open(x, "rb")

    parameters = {
        'chat_id' : '-xxxxxxxxxx'
    }

    files = {
        'audio' : my_file
    }

    resp = requests.get(base_url, data=parameters, files=files)



print(result_mp3)
        