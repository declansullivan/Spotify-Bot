# Spotify-Bot

<h2>Description</h2>

If you're like me, you wind up just shuffling all of your music when listening to Spotify instead of making decent playlists.  A problem that I faced was that Christmas music would keep appearing in the shuffle.  To fix this, I made the Christmas Skipper Spotify Bot.  This uses the Spotify API to check what song you are listening to, and it it is Christmas related, to skip it.

<hr>

<h2>How it Works</h2>

The beginning of this program that deals with getting access to the Spotify API I learned using Ian Annase's Spotipy tutorial videos on youtube.  The complete playlist can be found <a href="https://www.youtube.com/watch?v=tmt5SdvTqUI&list=PLqgOPibB_QnzzcaOFYmY2cQjs35y0is9N">here</a>.

The rest was written by me.  It works by constantly checking the song you are listening to.  Initially, the previous song you were listening to is None, and is then the last song you listened to when you start listening.  To enter the if statement to check if the song is Christmas related, the previous song must be different than the current song, so that the if statement isn't unnecessarily entered.

Once the songs differ, indicating that the next song has started, the if statement can be entered.  The previous song value is reset, and then the album name is gotten from the current song's json.  If "Christmas" is contained in the album name that the song is in, it is skipped, otherwise, it plays through.  I originally tried to use genre to skip songs, although not every song has the genre section of the json filled out, so it proved to be useless, whereas most Christmas songs are in an album with Christmas in the name.
