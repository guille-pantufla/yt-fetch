import youtube_dl

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

with open("music") as file:
    for line in file:
    	with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    		print(line)
    		ydl.download([line])