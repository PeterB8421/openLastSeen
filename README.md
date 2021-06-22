# openLastSeen
This python script searches folder for seen.txt file and if found, opens next episode of the TV series you haven't seen yet.

To use this script, install requirements.txt. Then execute main.py with the following arguments:  
`python main.py <directory> [a]`

Arguments:  
`<directory>`: Specify directory where the tv series is stored.  
`[a]`: Optional argument to increement episode number. You should execute this after you've seen one episode.

**I only tested this on Windows, so this script might not work on Linux.**

This only works if video files are named like `SeriesName-S01E01.mkv` where the important part is that `E01` is the episode number (it can be E[any two digit number]). You also need to create empty file named `seen.txt`, the script does not create that by itself.
