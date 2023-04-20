import os
from twitchio.ext import commands
# from twitchio.client import Client
from replit import db
import random
from keep_awake import keep_awake

# this variable is used for the TwitchLib / Unity integrated project
setListIndex = 0

# I forgor how 2 random syntax
# So instead of googling stackoverflow for the millionth time here it is:

# random.choice(list) or random.choice([array values here])
# or random.randrange(starting#, ending#, skip interval)
# shuffle: random.shuffle(list)

# -------------------------------------------------------------------

### TODO

# see if you can store objects in the db under 1 key

# Madlibs game with chat (possible???)
# you would have to make a separate command for every word entry
# also lots of DB checks but certainly not impossible
# COULD just take messages in chat.....?
# would be more nonsensical and even funnier
# pastebin API is probably a good bet here: https://pastebin.com/doc_api

# -------------------------------------------------------------------

# no more of these globals
# look at me
# we are DB entries now
db["random_number"] = 0
db["guess_game_initiated"] = False
db["number_of_guesses"] = 0
db["initial_guess_number"] = 0

# setlist for TwitchLib integration project in Unity
setlist = [
  'NANORAY - Salmon Cannon', #1
  'Crystal Aliens vs. Mutor Sound System - Another Planet', #2
  'F-Zero GX OST - Raise A Curtain', #3
  'Jet Grind Radio OST - Electric Toothbrush', #4
  'Sho-T - I Need You (True Platinum Mix)', #5
  'Tips & Tricks vs. Wisdome - Let\'s Groove', #6
  'Beatdrop - Burn Out', #7
  'Aran - Reduxation', #8
  'Rez OST - Buggie Running Beeps (Area 01)', #9
  'SAM WAITIN - Get Funky', #10
  'kors k - dirty digital', #11
  'L.E.D.-G - OUTER LIMITS (Akira Ishihara remix)', #12
  'Deejays Paradie feat. Thomas Howard - Dancin\' My Way', #13
  'OKUYATOS - Kind Lady (Interlude)', #14
  'Orange Lounge - MOBO MOGA', #15
  'James Landino (No Straight Roads OST) - vs. Sayu (Japanese)', #16
  'F-Zero GX OST - U-Rays (Tutorial)', #17
  'DV-i - Passcard (final candidate) [Ex-Sync STYLE]', #18
  'Volant - GET ELECTRIC', #19
  'RAM - Dummy', #20
  'tiger YAMATO with ultrabeatbox - R5', #21
  'Astebreed OST - Erosion', #22
  'Zektbach - ZETA', #23
  'Virtual Self - a.i.ngel (Become God)', #24
  ]


# custom functions
def increment_RAM_counter():
    db["give_ram_counter"] = int(db["give_ram_counter"]) + 1

def set_random_number(int):
    db["random_number"] = random.randrange(1, int, 1)
    db["initial_guess_number"] = int
    db["guess_game_initiated"] = True


def reset_random_number():
    db["random_number"] = 0
    db["guess_game_initiated"] = False


def increment_guesses():
    db["number_of_guesses"] = db["number_of_guesses"] + 1


def reset_guesses():
    db["number_of_guesses"] = 0
    db["initial_guess_number"] = 0


# check if database entries have been created
def check_db_key(author):

    # has to be an exception handle b/c an empty db key throws an error
    try:
        db[author + "Guesses"] == True and db[author + "Points"] == True
    except:
        db[author + "Points"] = 0
        db[author + "Guesses"] = 0


# increment database entry by 1
def increment_db(author):
    db[author + "Guesses"] = db[author + "Guesses"] + 1
    db[author +
       "Points"] = db[author + "Points"] + round(db["initial_guess_number"] / (
           (db["number_of_guesses"] + 1) * 2))


# Haven't implemented client class yet but it looks promising
""""
class Client (Client):
  
  # initialize client
  def __init__(self):
    super().__init__(
      token = os.environ['TWITCH_TOKEN'],
      client_secret = os.environ['TWITCH_CLIENT_ID'],
      initial_channels = ['bathinjan']
    )
"""

# Bot class
class Bot(commands.Bot):

    # initialize bot
    def __init__(self):
        super().__init__(
            token=os.environ['TWITCH_TOKEN'],
            prefix='!',
            initial_channels=['bathinjan', 'nicholegoodnight', 'l3blab', 'cityofstad'],
        )

    # notify when bot is online
    async def event_ready(self):
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')

    # ignore messages sent by bot
    async def event_message(self, message):
        if message.echo:
            return

        # print messages to console
        print(f"{message.author.name}: {message.content}")

        # handle and invoke commands
        await self.handle_commands(message)

        # 'pog' appears anywhere in chat
        if 'pog' in message.content.lower():
            await message.channel.send("PogBones !!!")

        # 'notlikethis' appears anywhere in chat
        if 'notlikethis' in message.content.lower():
            await message.channel.send("NotLikeThis")

        # 'gay' appears anywhere in chat
        if 'gay' in message.content.lower():
            await message.channel.send("GayPride")

        # 'GayPride' appears anywhere in chat
        if 'GayPride' in message.content.lower():
            await message.channel.send("GayPride")

        # 'trans' appears anywhere in chat
        if 'trans' in message.content.lower():
            await message.channel.send("TransgenderPride")

        # if 'buttsbot yes' appears anywhere in chat
        if 'buttsbot yes' in message.content.lower():
            await message.channel.send("buttsbot NO")

        # if 'ace' appears anywhere in chat
        if 'ace' in message.content.lower():
            await message.channel.send("AsexualPride")

        # if 'pan' appears anywhere in chat
        if 'pan' in message.content.lower():
            await message.channel.send("PansexualPride")

        # if 'bi' appears anywhere in chat
        if 'bi' in message.content.lower():
            await message.channel.send("BisexualPride")

        # if 'lesbian' appears anywhere in chat
        if 'lesbian' in message.content.lower():
            await message.channel.send("LesbianPride")

        # if 'balls' appears anywhere in chat
        if 'balls' in message.content.lower():
            await message.channel.send("cubes")

        # if 'bathybot is a liar'
        if 'bathybot is a liar' in message.content.lower():
            await message.channel.send(
                "I would never lie to you. I'm made of truths and Arby's roast beef."
            )

    ######################### COMMANDS #########################

    # Please for the love of christ alphabetize these

    # !flipacoin
    @commands.command()
    async def flipacoin(self, ctx: commands.Context):
        response = [
            'Heads',
            'Tails',
        ]
        await ctx.send(f"{random.choice(response)}")


    # !8ball
    @commands.command(aliases=["8ball"])
    async def eight_ball(self, ctx: commands.Context, question):
        responses = [
            'Yeah dude.',
            'Absolutely.',
            'Uhhhh sure.',
            'Mmmmyep.',
            'Why not.',
            'I\'m gonna say yes.',
            'Probably.',
            'Yeah sure.',
            'Yeah.',
            'I forgor.',
            'Reply hazy, try again immediately.',
            'Ask me again immediately.',
            'I really, REALLY shouldn\'t tell you...',
            'No idea dude.',
            'Concentrate harder and ask me nicely.',
            'Don\'t put money on that one, champ.',
            'I\'m gonna say no.',
            'My sources say : nahhh.',
            'Outlook isn\'t great, is it...',
            'Absolutely not.',
        ]

        if question:
            await ctx.send(f"My Answer: {random.choice(responses)}")
        else:
            await ctx.send(
                "You gotta ask a question for the mediocre 8-ball to answer you! (missing second arg 'question'"
            )

    # !giveram
    @commands.command()
    async def giveram(self, ctx: commands.Context):
        await ctx.send(
            f' MrDestructoid BathyBot has been fed {db["give_ram_counter"]} sticks of delicious and nutritious RAM total. Thank you for your patronage MrDestructoid CPU is at {random.randrange(0,100)} %'
        )
        increment_RAM_counter()

    # !givewam
    @commands.command()
    async def givewam(self, ctx: commands.Context):
        await ctx.send(
            f' MrDestructoid BathyBot has been fed {db["give_ram_counter"]} sticks of delicious and nutritious RAM total uwu Thank you for your patronage uwu MrDestructoid CPU is at {random.randrange(0,100)} % uwu'
        )
        increment_RAM_counter()

    # !gorngle
    @commands.command()
    async def gorngle(self, ctx: commands.Context):
        await ctx.send(f'˙ ͜ʟ˙')

    # !hi
    @commands.command()
    async def hi(self, ctx: commands.Context):
        await ctx.send(f'Hiya {ctx.author.name}!')

    # !creator
    @commands.command()
    async def creator(self, ctx: commands.Context):
        await ctx.send(
            'Bath is a game dev, pixel / 3D artist, (shitty) programmer, musician, speedrunner, and writer. I was created from their hubris. Check out their works at https://twitter.com/bathinjan_ !'
        )

    # !guessgame
    @commands.command()
    async def guessgame(self, ctx: commands.Context):

        reset_guesses()
        # tokenize user input using split()
        # so you can work with an args array essentially
        # in this instance I use just 1 arg after the command
        # but theoretically (hopefully) you could layer this
        # to make more complex things happen
        # idk if this is clunky but it works
        message_contents = ctx.message.content
        token = message_contents.split()
        if not (db["guess_game_initiated"]):
            if (len(token)) == 1:
                # pick a default parameter
                set_random_number(1000)
                await ctx.send(
                    f'Number set to default value 1000. Try to guess the number between 1 and 1000 using !guess'
                )

            elif token[1].isdigit() == True:
                # start the guess game by setting the random number
                set_random_number(int(token[1]))
                await ctx.send(
                    f'Number set. Try to guess the number between 1 and {token[1]} using !guess'
                )

        else:
            await ctx.send("A guess game has already been started!")

    @commands.command()
    async def guess(self, ctx: commands.Context):

        # tokenize user input
        message_contents = ctx.message.content
        token = message_contents.split()

        # check if a game was started
        if db["random_number"] != 0:

            if int(token[1]) == db["random_number"]:
                reset_random_number()

                # check db for author entry (create one if empty)
                check_db_key(str(ctx.author.name))
                # increment db entry by 1 / points
                increment_db(str(ctx.author.name))

                await ctx.send(
                    f'PogBones YOU DID IT!! YOU GUESSED THE NUMBER {ctx.author.name}!!! You were awarded {round(db["initial_guess_number"] / ((db["number_of_guesses"] + 1) * 2))} points! {ctx.author.name} has won the guessing game {db[ctx.author.name + "Guesses"]} times, and the total number of guesses in this game was {db["number_of_guesses"] + 1}, wow!'
                )

            elif int(token[1]) < db["random_number"]:
                increment_guesses()
                await ctx.send(f'You guessed too low, {ctx.author.name}.')

            elif int(token[1]) > db["random_number"]:
                increment_guesses()
                await ctx.send(f'You guessed too high, {ctx.author.name}.')

        # game has not been initialized yet
        else:
            await ctx.send(
                "Guessing game hasn't been started! Please use !guessgame to start the game."
            )

    # !banan
    @commands.command()
    async def banan(self, ctx: commands.Context):
        await ctx.send("🍌🍌🍌 bunungo 🍌🍌🍌")

    # !mypoints
    @commands.command()
    async def mypoints(self, ctx: commands.Context):
        try:
            db[ctx.author.name + "Points"]
            await ctx.send(
                f'{ctx.author.name}\'s correct points are: {db[ctx.author.name + "Points"]}'
            )
        except:
            await ctx.send(f'{ctx.author.name}\'s correct points are: 0')

    # !myguesses
    @commands.command()
    async def myguesses(self, ctx: commands.Context):
        try:
            db[ctx.author.name + "Guesses"]
            await ctx.send(
                f'{ctx.author.name}\'s correct guesses are: {db[ctx.author.name + "Guesses"]}'
            )
        except:
            await ctx.send(f'{ctx.author.name}\'s correct guesses are: 0')

    # !resetmyguesses
    @commands.command()
    async def resetmyguesses(self, ctx: commands.Context):
        try:
            db[ctx.author.name + "Guesses"] = 0
            await ctx.send(f'{ctx.author.name}\'s guesses reset to 0.')
        except:
            await ctx.send(
                f'{ctx.author.name} does not have an entry in the db!')

    # !resetmypoints
    @commands.command()
    async def resetmypoints(self, ctx: commands.Context):
        try:
          db[ctx.author.name + "Points"] = 0
          await ctx.send(f'{ctx.author.name}\'s points reset to 0.')
        except:
          await ctx.send(
            f'{ctx.author.name} does not have an entry in the db!')

    # !huge
    @commands.command()
    async def huge(self, ctx: commands.Context):
      await ctx.send(f'Absolutely massive, {ctx.author.name}.')

    # !pundetected
    # This is for my mod, EdIsEverywhere
    # Making the worst puns known to man
    @commands.command()
    async def pundetected(self, ctx: commands.Context):
      await ctx.send(f'@EdIsEverywhere you better knock it off, buddy.')

    # !setlist next
    # set up so that only my mod or I can trigger this command
    # used for TwitchLib / Unity integrated project
    @commands.command()
    async def setlistnext(self, ctx: commands.Context):
      if ctx.author.name == "bathinjan" or ctx.author.name == 'ediseverywhere':
        global setListIndex
        setListIndex += 1
        await ctx.send(f'Track was set to : {setlist[setListIndex]}.')
      else:
        await ctx.send(f'You do not have the permissions to use this command.')

    # !song
    # used for TwitchLib / Unity integrated project
    @commands.command()
    async def song(self, ctx: commands.Context):
      await ctx.send(f'Current Song : {setlist[setListIndex]}.')

bot = Bot()
# client = Client()

# webserver
keep_awake()

bot.run()
# client.run()