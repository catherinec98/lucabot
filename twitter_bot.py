#!/usr/bin/env python
# coding: utf-8
import random
import time
import sys
import tweepy
import credentials
#import urllib.request
import copy
from os import environ
#import gc

'''
CONSUMER_KEY = credentials.CONSUMER_KEY
CONSUMER_SECRET = credentials.CONSUMER_SECRET
ACCESS_KEY = credentials.ACCESS_KEY
ACCESS_SECRET = credentials.ACCESS_SECRET
'''


CONSUMER_KEY = environ['CONSUMER_KEY']
CONSUMER_SECRET = environ['CONSUMER_SECRET']
ACCESS_KEY = environ['ACCESS_KEY']
ACCESS_SECRET = environ['ACCESS_SECRET']


'''

def get_quotes():
    with open('quotes.json') as f:
        quotes_json = json.load(f)
    return quotes_json['quotes']

def get_random_quote():
    quotes = get_quotes()
    random_quote = random.choice(quotes)
    return random_quote

def create_quote():
    quote = get_random_quote()
    quote = """
            {}
            ~{}
            """.format(quote['quote'], quote['author'])
    return quote

def get_weather():
    req = urllib.request.Request(url=f'https://api.openweathermap.org/data/2.5/weather?q=Atlanta&units=imperial&appid='+FORECAST_APIKEY)

    with urllib.request.urlopen(req) as resp:
        data = json.loads(resp.read().decode("utf-8"))
        gc.collect()
    return data

def create_tweet():
        
    data=get_weather()
    temperature = str(int(round(data['main']['temp'])))
    degree_sign = u'\N{DEGREE SIGN}'
    description = data['weather'][0]['description']
    #description = data['current']['weather'][0]['description']

    tweet = "Rise Up ATL Runners! It's currently " + temperature + degree_sign + "F and " + str(description) +". Time for a run!" + create_quote()+"\n #morningmotivation #running #atlanta #atlantatrackclub"

    if len(tweet) > 280:
        tweet = "Rise Up ATL Runners! It's currently " + temperature + degree_sign + "F and " + str(description)+". Time for a run! \n #morningmotivation #running #atlanta #atlantatrackclub"
    
    return tweet

def tweet_quote():
    #interval = 60 * 60 * 12 # tweet every 12 hours

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)

    tweet = create_tweet()
    api.update_status(tweet)

    #while True:
     #   print('getting a random quote...')        
      #  tweet = create_tweet()
       # api.update_status(tweet)
        #time.sleep(interval) 
    
if __name__ == "__main__":
    tweet_quote()

'''



quotes = '''Luca Balsa was once a world-renowned inventor. He never gave up his deepest aspiration even when he was in jail. Now that he's free, nothing is stopping him from completing his greatest invention",
"Luca Balsa used to be considered friendly and too trusting by most people. No one knows where he came from or has seen his family, but clearly, he's well educated. He has a tremendous sense of pride and he is curious about all sorts of scientific inventions.",
"There is no turning back for Luca",
"Nevertheless, Luca is still determined to complete his initial invention",
"I can't remember how long I've been working this humble job. I can't seem to remember anything.",
"I do have vague memories of that invention. As soon as I first saw it, I knew that I'd never be able to love anything else.",
"But yet, why did he always oppose my ideas? I never found the answer, not even when the electric current struck his brain. He's already dead, But, is there any way to prevent me from being next...?",
"I was acquitted with someone else's help after, but being spared from the noose was perhaps even worse as I was free but still unable to finish the great invention.",
"Arc Light: An illusion that is transient, dangerous and bright like the sun.",
"A diary: I found 3 drafts in my father's bookcase. They are the work of a genius, but there seem to be some pages missing. It doesn't matter anyway. I'll finish it one day.",
"A shredded admission notice: Luca Balsa, we're very honored to welcome such a prestigious character as yourself to our school. We trust that you will soon make your family proud",
"Medium: Energy must collide in order to transmit.",
"An anecdote: An aristocrat in town lost his entire fortune on failed investments in emerging industries. He had to auction off his wife's dowry to pay off his debts. His wife died of anger. His son couldn't forgive him and left.",
"Coupling: There will only be a resonance of wisdom when the souls are comparable",
"A diary: I've finally become a student of Lorenz with a manuscript as consideration. But one day he'll realize that I'm worth much more than those manuscripts.",
"Mutual Feelings: Time can't change everything.",
"Test Record No. 1: Despite the different experimental procedures, all of the experiments failed. The early experiments were signed off on by Lorenz. The ones later on were signed off on by Lorenz and Balsa. Those towards the end were signed off on by Balsa only.",
"A lunatic, or a thief?",
"All you need is an opportunity.",
"The Record No. 2: The experiment was signed off on by Balsa. All of the experimental procedures were exactly the same. The experiment's results were omitted.",
"Overshoot: The smallest change, the greatest deviation.",
"He lost everything when he immersed himself in Rashomon. Is all this really worth it?",
"I may be in a prison uniform, but I'm not imprisoned",
"It's no easy task connecting the circuits, but it's what I do best!",
"When will I create my great invention?",
"It's ironic. I should thank my teacher for instilling me with these principles.",
"There's no fairness in this world, only wins and losses.",
"Life is too short and regrets are more terrifying than failures. That's why I'd rather give it a try.",
"My name is Luca Balsa, and I am the student you spoke with at the Laiden Art and Industry Exhibit the other day. I could hardly restrain my excitement and admiration after meeting you, and so I decided to write you a letter.",
"Likes: Books, music, science experiments \n Dislikes: Loud noises, instruments of torture",
"To speak candidly, the moment I laid eyes on your masterpiece at the exhibition, I knew that it would become my lifelong work!",
"I refuse to give up; after all, my family and I know full well the price of dedicating ourselves to science.",
"What I mean to say is that I do not believe this line of research to be a waste of tools, time, or talent—how could it be?",
"such obsession also weakens the Prisoner's perception of his surroundings",
"An incident changed the Prisoner's body composition and made him a 'Conductor' capable of accumulating electric charges",
"To play it safe, the 'Prisoner' set up a connection between the two Exit Gates in advance",
"He made use of the delicate relationship between science and alchemy to complete the performance of ‘turning stone into gold,’ yet he has no idea that the real Philosopher’s Stone is nothing but a glorified lie",
"It's time we call it quits, be it this journey or the chill that's been harassing me my entire life. My guide would do anything to get me out of here, yet 'she' forced me to make a choice - perform my pledge or remedy my destiny",
"Perhaps all shadows love darkness; that's why I like sunset more than sunrise. I've seen the sixth sunset in this forest today. I hope that we... at least I... still have the chance to see the seventh.",
"The Energy Corporation has taken resources from the snowy ruins and has infiltrated into each of the logistics departments. Yet he's one of the few exceptions",
"The crowd takes to the street for the festivities, laughing and enjoying themselves.",
"Small, silver shellfish live beneath the gravel bed of the shallow sea. Unless prying their shell open, none would expect to find bright, red flesh hidden within.",
"If you're lucky, touching it with your bare hands it will make you itch all over. If not, you might die.",
"Is moldy bread edible? That's not a question for the people in prison.",
"In my days of imprisonment, all I did was stare at the walls.",
"Destiny is an irreversible formula, and no exceptional science can determine its value.",
"A shadow among the trees awaits on the throne in the forest. Truth is much more attractive than treasure.",
"To the Viper, the truth buried here is more fascinating than the treasure in the forest",
"There's something called Certainty Effect, where the probability that people perceive subjectively changes with their impressions and doesn't match the objective probability. (`⊗﹁◓´) just think of it as a lottery and take it easy (TL: @/fc_idv)",
"I will forget... not only inventions... also important encounters... (`⊗﹁◓´) A man like that deserves to be alone, doesn't he? (TL: @/fc_idv)",
"In fact, I forgot my own birthday. I was only reminded by all the celebration (TL: @/fc_idv)",
"When you've prepared so much, I can't just say thank you, can I? (`⊗﹁◓´) How can I thank you for this? (TL: @/fc_idv)",
"Just because I can play the piano doesn't mean I'm any good. (`⊗﹁◓´) It's just a hobby. You have your own hobbies too don't you? (TL: @/fc_idv)",
"What on earth is going on that I'm the winner? (`⊗﹁◓´) On the contrary, what did they like about me..? (TL: @/fc_idv)",
"I see... That's right, if I do this- No, that can't be it... Then I'll use this formula... Come to think of it, I've seen these numerics before......Nnm? My bad, didn't notice you. (`⊗﹁◓´) ＜ You need something? (TL: @/dapporock",
"Heheh, heh… Your concern and suchlike are futile, unneeded. I know my own body best. It’s just that I can’t stop myself, even in spite of knowing better. (TL: @/mayousailor)",
"(`⊗﹁◓´)＜ Nothing to lose from studying AC sinusoidal waveforms. (TL: @/mayousailor)",
"Y’know… Y’know… I get really happy about that sorta thing. When somebody like you… gets all worried about how my body’s holding up. (`⊗﹁◓´)＜ Thanks. You look out for yourself too. (TL: @/mayousailor)",
"(`⊗﹁◓´)＜Well, I’m just speaking without thinking, so take it with a grain of salt, yeah? (TL: @/mayousailor)",
"Only from a submissive soul can flowers bloom eternal",
"Now that’s a nifty little idea. Whether a failure or a success, That pumpkin pie of yours is something I’d really like to see. (TL: @/mayousailor)",
"He seemed like a well-educated fellow, but his attire was enough to tell me he was anything but a good person",
"But as I was preparing to disassemble an old clock on the wall, he suddenly appeared behind me, asking for the time. I told his it was 3:21 PM. When I turned to look at him, he was gazing at me, apparently lost in thought.",
"Furthermore, he mentioned that there were far more permanent solutions than conventional batteries or oscillating, analog parts.",
"The man seemed to take interest after I finished my explanations, and began muttering himself, almost disdainfully, repeating my words 'battery' and 'rewinding.'",
"Perplexed, I questioned the person about his behavior, to which he responded with his honest feelings, that the word invention should not be used to describe parts that extend the life of a pre-existing device.",
"Oh… I’m not sure what you’re talking about, though… You mean you’re feeling better because of me, right? Uh… What should I say… (`⊗﹁◓´)＜…You’re welcome? (TL: @/fc_idv)",
"Hey, whats the point of watching me? It took a long time to repair the telescope, you know? (TL: @/fc_idv)",
"I want you to observe and enjoy the stars, if only as a tribute to my efforts. And you don't need to look through the telescope to see me, you can just look directly at me right? (`⊗﹁◓´)＜When you look at me through the lens, I feel kind of lonely (TL: @/fc_idv)",
"When your body is destroyed, only a part of you is lost. When your spirit is broken, all of you is lost",
"The joy of others is surprisingly pleasing to the eye you know? (`⊗﹁◓´)＜ So you don't need to worry about me, okay? (TL: @/fc_idv)",
"I hate absurdity, you know? (TL: @/fc_idv)",
"It won't come back to me... It's all gone, wiped clean from my head! All of it, all of it, my precious formulae, my precious measurements! Nothing but the simplest things left in this head of mine...! I have to... I have to remember... (TL @/mayousailor)",
"Wait, hey, are you sure? If thinking too much about the interests of others destroys your own, that’s putting the cart before the horse. I would much prefer to see you unbankrupted, (`⊗﹁◓´)＜I don't ask for anything more than that. (TL @/fc_idv)",
"(Emma about Luca) He was so concentrated in invention that I could not talk to him.... But Emma heard him saying to himself, 'It would be interesting to be able to fly...'! (((；°Д°))) (TL: @/fc_idv)'''

images = '''Sweets Paradise: Winter Cafe merchandise https://t.co/4XWIOe0SYK",
"Victor's birthday art 2020 https://t.co/5osDBVpKog",
"Luca standard artwork https://t.co/ikov9mmGPM",
"Luca's release video https://t.co/9MuEXcgf1X",
"Season 13 Essence 1 video https://t.co/3af5Fs3Km6",
"Season 13 Essence 1 video https://t.co/x0V1aAw6gr",
"Season 13 Essence 1 video https://t.co/kOeazxFqxg",
"Season 13 Essence 1 poster https://t.co/x5MJ0xz41v",
"Sweets Paradise: Winter Cafe merchandise preview https://t.co/NjnCUGXuCI",
"Luca's release video https://t.co/SAwV8v30uF",
"Luca's release video https://t.co/CFa7uQ1WMQ",
"Luca's colorful memory portrait https://t.co/4drooGp5eq",
"Sweets Paradise: Winter Cafe promotional art https://t.co/kiCBnTCTwX",
"Luca's birthday art 2021 - global server https://t.co/1BtvZKkmSf",
"Luca's birthday portrait https://t.co/dVlGaiCSO0",
"Lawson collaboration comic https://t.co/Ib7FokweSZ",
"Lawson collaboration comic https://t.co/Asv0Wmwje0",
"Luca's birthday announcement 2021 https://t.co/yu3c9OvYE2",
"Lawson collaboration promotional art https://t.co/r2WdVgR1C8",
"Primaniacs collaboration promotional art https://t.co/BChctKz7gX",
"Luca's concept art https://t.co/Y2fkSCbdpi",
"Banpresto merchandise https://t.co/82PF4Ku2wj",
"Rascal collaboration art https://t.co/MTwkovmE0O",
"Ichiban Kuji merchandise preview https://t.co/XVKBTWsfcy",
"Ichiban Kuji merchandise promotional art https://t.co/YwDV64knlb",
"Omanju Niginigi merchandise preview https://t.co/7CRhrjNgzh",
"Luca's birthday art 2021 - Chinese server https://t.co/qVm28EAk6s",
"Meteor shower event graffiti https://t.co/WsgRtn9yPf",
"Season 10 Essence 2 poster https://t.co/PrI8FPAUA2",
"Sunshine City Prince Hotel collaboration artwork https://t.co/yFKRciNIpV",
"Official website merchandise tab https://t.co/sbSbTjNLHs",
"Follower milestone artwork https://t.co/PjMK07Kj0J",
"William's birthday art 2021 https://t.co/fZUBTepEun",
"Season 16 Essence 3 video https://t.co/hbyZZrSTql",
"Season 16 Essence 3 video https://t.co/wamuQzrL5G",
"Season 16 Essence 3 video https://t.co/hrzydAGFR2",
"Butler cafe artwork https://t.co/YckjfBd4Bx",
"Butler cafe artwork https://t.co/FWOnWjBILR",
"Sweets Paradise: Autumn Cafe artwork https://t.co/XmnmSKQfKu",
"Butler Cafe - best butler award artwork https://t.co/Y0ulBIGMxO",
"COMICUP 28 artwork https://t.co/ii865k2nTE",
"Stageplay merchandise https://t.co/DwYLwqkqw6",
"Luca's release artwork https://t.co/WfZKUSuAOH",
"Official art posted on weibo https://t.co/eUQFUKyQoL",
"Winter solstice artwork https://t.co/DZPojQxMIr",
"Autumn Appetite official art https://t.co/McKTi6UEsL",
"Tanabata art 2021 https://t.co/EgwKSTCyYQ",
"General official artwork https://t.co/K3uMLPvYvJ",
"3rd Anniversary artwork https://t.co/nIlE1DtZrp",
"Birthday merchandise artwork https://t.co/obMlrjwuL8",
"3rd Anniversary artwork https://t.co/D4MIQPIlNj",
"Athletic games 2020 artwork https://t.co/KzHsuWbUok",
"General official artwork https://t.co/96yn1IoWs1",
"3rd Anniversary artwork https://t.co/ft3pGg3Mhy",
"2nd Anniversary artwork https://t.co/HQMbD6EoqE",
"The Promised Neverland collaboration artwork https://t.co/oc9AF5lusE",
"General official artwork https://t.co/6Tfhce25Ti",
"Mother's Day artwork 2021 https://t.co/6VsbGQkxbY",
"Youth Day artwork https://t.co/e7f8OWjdnA",
"3rd Anniversary artwork https://t.co/H3HS05f0NI",
"Chang Thai Day artwork https://t.co/bEpvABRsyB",
"Christmas 2020 video https://t.co/nSP1MH7MSm",
"Christmas 2020 video https://t.co/JuNIQC7mis",
"Christmas 2020 artwork https://t.co/zT34UGHYW1",
"General official artwork https://t.co/KfYGnYMPoR",
"100k followers artwork https://t.co/oOc0JIc4IB",
"New Years video https://t.co/wkJ4pQHyZ1",
"New Years video https://t.co/0GKo8MqeMb",
"New Years video https://t.co/ceAW6pGgjM",
"New Years video https://t.co/fzqink9UEn",
"General official artwork https://t.co/OM0MVIiXEx",
"School entrance ceremony artwork https://t.co/9k0so0fiLW",
"800k followers artwork https://t.co/KDWvnyd33I",
"Sweets Paradise collaboration artwork https://t.co/gHzz9Y5tfL",
"Spring Equinox artwork https://t.co/FmS4HGt4ye",
"GaoKao artwork https://t.co/Ykw0izTdbu",
"Official merchandise artwork https://t.co/TRofwNOn7R",
"IDV mobile battery artwork https://t.co/oea1v0RmmV",
"Ensky collaboration artwork https://t.co/t1OyMvBTNC",
"Auldey collaboration artwork https://t.co/sjwSiaNNjT",
"April Fools artwork https://t.co/DNjTdh2cce",
"Watermelon Day artwork https://t.co/AZC4owwY6i",
"Summer 2021 artwork https://t.co/QPvb3UwaTt",
"Christmas video 2020 https://t.co/GBh0f8PFNL",
"Electrolysis beta designs https://t.co/8zfoXmIWTL",
"IVL 2020 artwork https://t.co/vbsUbLj4kP",
"Typhoon season artwork Sept. 2020 https://t.co/aXvx151Dnm",
"The Promised Neverland collab quiz https://t.co/0VSr2GlleG",
"2nd Anniversary artwork https://t.co/DgTeVbqrbq",
"2nd Anniversary artwork https://t.co/Wh1QruvHvg",
"Weibo school comic 2021 https://t.co/FjU5hMzHrA",
"Season 17 Essence 3 video https://t.co/lGmBkX2uHx",
"Season 17 Essence 3 video https://t.co/XvY976LLml",
"Summer sleepover artwork August 2021 https://t.co/68SfoFPmis",
"Luca's black and white portrait https://t.co/UcQNdTloAh",
"Identity V in Namjatown collaboration artwork https://t.co/sFdK7cHtr9",
"Classical music day 2021 https://t.co/DtKgloez0q",
"White Day reply art 2021 https://t.co/5qBSgjocYh",
"Tracy's birthday art 2021 https://t.co/0HnOaanvVX",
"Tokyo Tower collaboration artwork https://t.co/7PqiOrNops",
"Tokyo Tower collab merchandise preview https://t.co/2ODSHxs63l",
"Tokyo Tower collab artwork https://t.co/a4XOjJXEhW",
"Identity V in Namjatown collab artwork https://t.co/ty6rX7azaM",
"Identity V DarkxPOP Trading Cards Vol. 2 https://t.co/VRgRqy7stI",
"Prince Hotels Collab artwork https://t.co/sJJ3JxMRMU",
"Mid-Autumn Festival 2021 https://t.co/j0E4F8XgR4",
"2022 Calendar official merchandise https://t.co/iAhQVvPw4P",
"Tokyo Tower collaboration cutout https://t.co/CK6uuuIpXD",
"'Moonbound' event skin preview https://t.co/6HSRjGJqpY",
"Death Note pre-collab event https://t.co/86orA3SPDa",
"Death Note pre-collab 'Find Kira' video https://t.co/LeSRn0cAbM",
"Luca's room - Death Note pre-collab event https://t.co/vXvF1UnBWi",
"Official merchandise - Nokkari rubber clip https://t.co/39XpfLpHhr",
"Meteor shower art 2021 https://t.co/C3V0pcjVww",
"Identity V x Simeji collab https://t.co/yJE5OP5HUp",
"Identity V Ensky merchandise https://t.co/KH0GP7f4j7",
"Ensky merchandise preview art https://t.co/QUNLX3CXYN",
"Identity V Ensky merchandise preview https://t.co/3aVJv7T34O",
"IDV x SANSAN personality quiz https://t.co/s1yF7mPq7J",
"Halloween 2021 Twitter DM event https://t.co/Qh06sl0Jek",
"Luca's 'stand' showroom animation https://t.co/IJBwymls7U",
"Luca's dance emote https://t.co/tWhofioaCc",
"Default Luca's showroom animation 1 https://t.co/APGBx4ldN7",
"Electrolysis showroom animation 2 https://t.co/sfExd50WtA",
"Luca's shout emote https://t.co/LP4oDFevsM",
"Default Luca's showroom idle animation https://t.co/QzqH4J072O",
"Luca's dice roll emote https://t.co/pLpk6qF10k",
"Viper showroom idle animation https://t.co/IeX9nGZdqV",
"Electrolysis showroom idle animation https://t.co/MGu7qFfKPj",
"Electrolysis showroom animation 1 https://t.co/5TG1QTHxLr",
"Viper showroom entrance animation https://t.co/SLjTHxnf63",
"Viper showroom animation 1 https://t.co/0Lm31vdgJS",
"Racing mechanic/COA IV promo art https://t.co/TYoDabanOn",
"Sweets Paradise: Winter Cafe chibi art https://t.co/IxXPEvtsj3",
"900k Twitter follower artwork https://t.co/XD9mpyDBCc",
"Electrolysis acrylic stand artwork https://t.co/OXeHv1q9lM",
"Identity V digital booth artwork https://t.co/Pi1PK4RA80",
"Luca full character reference sheet https://t.co/AinbkQdok4",
"Identity V pixel art merchandise preview https://t.co/2d8QNAIStL",
"Identity V character tin plate merchandise https://t.co/6EYevFBWTT",
"Luca's release video 1 https://t.co/LXXgasMFhf",
"Luca's release video 2 https://t.co/DnX6H5kMlr",
"Luca's release video 3 https://t.co/chLdVgBDhV",
"Luca's release video 4 https://t.co/l4X7jaZTma",
"Luca's release video 5 https://t.co/9vQz3h7HNg",
"Luca's release video 6 https://t.co/P6G9zYFQvu",
"Luca's release video 7 https://t.co/ou7IxtYu6e",
"Luca's release video 8 https://t.co/rBFUI1pU62",
"Luca's release video 9 https://t.co/xvKIIxh11e",
"COA V character reveal artwork https://t.co/oKOMq4GhKS",
"IDV 3rd Anniversary artwork https://t.co/FxcrnGGK7Z",
"Viper skin reference sheet https://t.co/6Z4YpZRBcU",
"Viper pin https://t.co/hck8PLxh15",
"COA V teaser art https://t.co/oKOMq4GhKS",
"Luca's cheer emote https://t.co/bLz2C9BNLB",
"Auditorium skin reference sheet https://t.co/hWt0SIJTzs",
"IVC 2021 broadcast bumper animation https://t.co/xhiQdtGCtb",
"Winter solstice 2021 art https://t.co/6j6zVbeISy",
"COA V trailer appearance 1 https://t.co/8jJnWpECZA",
"COA V trailer appearance 2 https://t.co/jzdWZ88tGW",
"COA V trailer appearance 3 https://t.co/tLRbuKt7Ji",
"COA V trailer appearance 4 https://t.co/VINBhAd5n8",
"COA V trailer appearance 5 https://t.co/XOmmP0BU8m",
"COA V trailer final scene https://t.co/EJmSWZpUp2",
"Auditorium showroom entrance animation https://t.co/MhY1fHRSoP",
"COA V poster https://t.co/4VOd0kAyYy",
"Auditorium showroom animation https://t.co/Oz1T8DuKIP",
"Auditorium showroom idle animation https://t.co/V4G4xzpPlq",
"Luca's shame emote https://t.co/ZAYDi9N9aZ",
"Identity V in Namjatown collab merch preview https://t.co/SNw77mWzzC",
"COA V graffiti https://t.co/FTJtdDrjrS",
"Taobao stackable figures preview https://t.co/mYUmEjTq07",
"New Years 2022 art https://t.co/COKXmLaASo",
"Deduction star poster https://t.co/mg4kkmREeC'''



class g(object):
    pass
    
g = g()

g.quoteMasterList = quotes.split('",\n"')
g.imageMasterList = images.split('",\n"')

g.quoteQueue = copy.copy(g.quoteMasterList)
g.imageQueue = copy.copy(g.imageMasterList)

g.latestTweet = ""

g.order = 0

def selectQuote(quoteQueue, latestTweet):
    if len(quoteQueue) == 0:
        quoteQueue = copy.copy(g.quoteMasterList)
    q = random.randint(0,len(quoteQueue)-1)
    if quoteQueue[q] == latestTweet:
        quoteQueue.pop(q)
        q = random.randint(0, len(quoteQueue)-1)
    latestTweet = quoteQueue[q]
    return quoteQueue.pop(q)
    
def selectImg(imageQueue, latestTweet):
    if len(imageQueue) == 0:
        imageQueue = copy.copy(g.imageMasterList)
    q = random.randint(0,len(imageQueue)-1)
    if imageQueue[q] == latestTweet:
        imageQueue.pop(q)
        q = random.randint(0, len(imageQueue)-1)
    latestTweet = imageQueue[q]
    return imageQueue.pop(q)
    
def selectTweet(order):
    if order%3 == 0:
        g.order+=1
        return selectQuote(g.quoteQueue, g.latestTweet)
    else:
        g.order+=1
        return selectImg(g.imageQueue, g.latestTweet)
        
client = tweepy.Client(consumer_key=CONSUMER_KEY,
                       consumer_secret=CONSUMER_SECRET,
                       access_token=ACCESS_KEY,
                       access_token_secret=ACCESS_SECRET)

while True:     
    print('generating tweet....')
    response = client.create_tweet(text=selectTweet(g.order))
    print(response)
    #print('sleep')
    time.sleep(3600) 


#response = client.create_tweet(text=selectTweet(g.order))

#print(response)

#time.sleep(10)

#response = client.create_tweet(text=selectTweet(g.order))

#print(response)





