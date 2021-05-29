import random
from googleapiclient.discovery import build
import webbrowser
import devKey

def vid(videos):
    num = str(random.randint(0, 10000))

    search = random.choice(prefix) + num + random.choice(postfix)

    search_response = youtube.search().list(
        q=search,
        part='snippet',
        maxResults=50,
        order="date"
        ).execute()

    for search_result in search_response["items"]:
        if search_result['id']['kind'] == 'youtube#video':
            videos.append('https://youtu.be/%s' % (search_result['id']['videoId']))
    if videos:
        return videos
    return vid(videos)

DEVELOPER_KEY = devKey.key
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'

youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)

prefix = ['', 'IMG ', 'IMG_', 'IMG-', 'DSC ']
postfix = [' MOV', '.MOV', ' .MOV', ' MP4', '.MP4', ' .MP4', " WMV", ".WMV", " .WMV", " FLV", ".FLV", " .FLV", "AVI", " .AVI", ".AVI"]

while True:
    l = vid([])
    random.shuffle(l)
    for i in l:
        webbrowser.open(i)
        input()
