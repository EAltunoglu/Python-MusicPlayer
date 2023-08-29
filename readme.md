**Python MP3 Music Player**

![](RackMultipart20220613-1-7mm63_html_10cde913d42c20b.jpg)

**How to run**

You should change the 13th line of the code to your music folder.

MUSIC\_FOLDER\_PATH = &quot;C:/Users/YOURUSER/Music&quot;

Commands:

pip install -r requirements.txt

python code.py

**In case of error:** pygame.error: Failed loading libmpg123-0.dll: Module Not Found.

I have added libmpg123-0.dll. Paste it to C:\Windows\System32.

**UI**

![](RackMultipart20220613-1-7mm63_html_94075b65b8d9ce2e.jpg)

1. Tracklist
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
- Play and Pause buttons have both different colors and different shapes.
- The volume slider at the minimum position does not set the volume level to 0%. Instead, it is set to 5%. To mute the player, you are supposed to click on the speaker button. With these features, the user can clearly understand whether the player is muted.
- When a track ends, the next track is played automatically. If shuffle is enabled, it randomly selects.
- All other buttons are functional as well.

**How to improve**

- The shuffle button does not indicate whether it is activated.
- Support other sound file formats such as .wav.
- Sliders could be thinner.
- Playlist creation should be supported.
- Keyboard support could be added.
