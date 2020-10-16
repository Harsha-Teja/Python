import os
import shutil

# Change the path of the folder
os.chdir("/Users/apple/Downloads")


# This is the function perfomring the action of creating a folder and
# moving respective files with extensions mentioned in the lists below
def movingfile(searchfolder, foldername):
    print(os.path.exists(foldername))
    if os.path.exists(foldername) == True:
        pass
    else:
        os.makedirs(foldername)
    print(os.path.exists(foldername))

    for file in os.listdir():
        end = os.path.splitext(file)
        for i in searchfolder:
            if i == end[1]:
                print(i)
                src = f"/Users/apple/Documents/test/{file}"
                dest = f"/Users/apple/Documents/test/{foldername}/"
                shutil.move(src, dest)


# The list of extensions of folders
musicvideofile = [".webm", ".mp3", ".mp4"]
documentfile = [".txt", ".pdf", ".docx"]
otherfile = [".torrent", ".srt", ".html"]
photofile = [".png", ".jpg", "jpeg"]

# Calling the function with arguments for creating folder and checking the extension type
movingfile(musicvideofile, "MusicandVideo")
movingfile(documentfile, "DocumentFiles")
movingfile(otherfile, "Others")
movingfile(photofile, "Photos")
