# TwitchBot: BathyBot

My first Twitch bot: does a lot of random generic bidding, with the following simple functionalities:

### Guessing Game
Chat can trigger a guessing game with !guessgame and a number as a second arg. 
The winning guesser earns points that depend on how many guesses were posted in chat (if you guess early, you win more points etc). 
When users win a guessing game, a simple entry is created in the Repl database storing their points - these users can check their points at any time using !mypoints.

### Flip A Coin
Requests a coin flip, selects heads or tails at random and posts the result

### 8 Ball
Users can type !8ball and a question - responds with one of 20 responses. Checks to make sure a second arg (question) is provided.

### Give RAM / WAM
Keeps a counter of how many times users "give ram" to Bathybot. A throwback to an old meme of when I used to use autotune / bitcrush affects on stream and pretend to be a robot...anyway.

### Setlist / Song
Used with a TwitchLib / Unity integrated project where I performed a DJ Set; handled a setlist so users could request the current song playing. Checks to make sure only my mod or I are the users requesting to change the next song.

### Event Message Listening
Listens for a specific string in every message and responds when it sees it. Chat loves it. I have no idea why. Most commonly used to respond to common phrases such as NotLikeThis or PogBones with the corresponding Twitch global emote.
