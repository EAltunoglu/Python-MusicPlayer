**Python MP3 Music Player**

Eren Altunoğlu - 2017400120

![](RackMultipart20220613-1-7mm63_html_10cde913d42c20b.jpg)

**How to run**

You should change 13th line of the code to your music folder.

MUSIC\_FOLDER\_PATH = &quot;C:/Users/YOURUSER/Music&quot;

Commands:

pip install -r requirements.txt

python code.py

**In case of error:** pygame.error: Failed loading libmpg123-0.dll: Module Not Found.

I have added libmpg123-0.dll to the zip file. Paste it to C:\Windows\System32.

**UI**

![](RackMultipart20220613-1-7mm63_html_94075b65b8d9ce2e.jpg)

1. Track list
2. Previous track button
3. Play/Pause button
4. Next track button
5. Mute/Unmute Button
6. Volume slider
7. Shuffle button
8. Label for current position at playing track
9. Track progress slider
10. Playing track length

![](RackMultipart20220613-1-7mm63_html_771422a7537671af.jpg)

**Features**

- When you click any track on the list, it starts to play.
- Play and Pause buttons have both different color and different shape.
- Volume slider at minimum position does not set volume level to 0%. Instead, it sets to 5%. To mute player, you are supposed to click on speaker button. With these features, user can clearly understand whether player is muted.
- When a track ends, next track is played automatically. If shuffle enabled, it randomly selects.
- All other buttons are functional as well.

**How to improve**

- Shuffle button does not indicate whether it is activated.
- Support other sound file formats such as .wav.
- Sliders could be thinner.
- Playlist creation should be supported.
- Keyboard support could be added. For example, F12 + right arrow could play next.