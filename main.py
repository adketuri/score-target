import xml.dom.minidom

def format_score(score):
    return "{0:.2f}%".format(score * 100)

doc = xml.dom.minidom.parse("C:\\Users\\Andrew\\AppData\\Roaming\\StepMania 5\\Save\\LocalProfiles\\00000000\\Stats.xml")
target = 0.96
folder = "SHARPNELSTREAMZ v3 Part 1"

incomplete = 0
for song in doc.getElementsByTagName("Song"):
    if folder != song.getAttribute("Dir").split("/")[1]: 
        continue
    song_name = song.getAttribute("Dir").split("/")[-2]
    for steps in song.getElementsByTagName("Steps"):
        song_difficulty = steps.getAttribute("Difficulty")
        try:
            song_score = float(steps.getElementsByTagName("HighScoreList")[0].getElementsByTagName("HighScore")[0].getElementsByTagName("PercentDP")[0].childNodes[0].data)
            if song_score < target:
                incomplete += 1
                print ("- {} [{}] {} ({})".format(song_name, song_difficulty, format_score(song_score), format_score(song_score - target)))
        except Exception, e:
            pass
if incomplete == 0:
    print ("You did it!")
else:
    print (str(incomplete) + " song(s) to raise")