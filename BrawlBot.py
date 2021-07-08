import discord
import random
import json
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix="-", intents=intents)

searchChannel = 854427760389652490
miscChannel = 854428093459202099
modChannel = 854428188746580059
matchChannel = 854428351800016907
channelList = [searchChannel, miscChannel, modChannel, matchChannel]

modkey = '🔑'
stay = '☑'
challenge = '⚔'
abort = '🔴'
accept = '✅'
cancel = '❌'
versus = '<:vs:843364613986189342>'
BF = '<:Battlefield:837907213627686943>'
FD = '<:FinalDestination:837907213695057950>'
SV = '<:Smashville:837907213678542863>'
netpColor = 4312575  # light blue
wifiColor = 16613797  # light pink
defaultColor = 15174967  # orange
netpSymbol = '<:netplay:849372987173371925>'
wifiSymbol = '<:wifi:849372254789828618>'
attributes = {"WIFI": {'symbol': wifiSymbol, 'color': wifiColor}, "NETP": {'symbol': netpSymbol, 'color': netpColor}}

brawlChara = {"mario": '<:mario:838822011412676708>', "donkey kong": '<:donkeykong:838822011114356760>',
              "dk": '<:donkeykong:838822011114356760>',
              "link": '<:link:838822011286716486>', "samus": '<:samus:838822011009499147>',
              "kirby": '<:kirby:838822010968735796>', "fox": '<:fox:838822011408613396>',
              "pikachu": '<:pikachu:838822011341111346>', "marth": '<:marth:838822011122745376>',
              "mr. game & watch": '<:mrgameandwatch:838822011441774642>',
              "mr.game & watch": '<:mrgameandwatch:838822011441774642>',
              "mr.g&w": '<:mrgameandwatch:838822011441774642>', "mr game and watch": '<:mrgameandwatch:838822011441774642>',
              "game n watch": '<:mrgameandwatch:838822011441774642>', "mr game n watch":'<:mrgameandwatch:838822011441774642>',
              "gnw": '<:mrgameandwatch:838822011441774642>', "mr gnw": '<:mrgameandwatch:838822011441774642>',
              "gandw": '<:mrgameandwatch:838822011441774642>', "mr game & watch": '<:mrgameandwatch:838822011441774642>',
              "game & watch": '<:mrgameandwatch:838822011441774642>',
              "gw": '<:mrgameandwatch:838822011441774642>', "mr.game and watch": '<:mrgameandwatch:838822011441774642>',
              "g&w": '<:mrgameandwatch:838822011441774642>', "luigi": '<:luigi:838822011421196358>',
              "diddy": '<:diddykong:838822011337572394>',
              "diddy kong": '<:diddykong:838822011337572394>', "zelda": '<:zelda:838822011304280164>',
              "sheik": '<:sheik:838822011308212274>', "pit": '<:pit:838822011084996639>',
              "meta knight": '<:metaknight:838822011248967700>',
              "metaknight": '<:metaknight:838822011248967700>', "mk": '<:metaknight:838822011248967700>',
              "falco": '<:falco:838822011366408302>', "pokemon trainer": '<:pokemontrainer:838822010884194325>',
              "pt": '<:pokemontrainer:838822010884194325>',
              "pokemon": '<:pokemontrainer:838822010884194325>', "trainer": '<:pokemontrainer:838822010884194325>',
              "squirtle": '<:squirtle:838822011202437201>', "ivysaur": '<:ivysaur:838822011420803073>',
              "charizard": '<:charizard:838822011223539752>',
              "ike": '<:ike:838822010921943102>', "snake": '<:snake:838822011328659536>',
              "peach": '<:peach:838822011030863874>', "yoshi": '<:yoshi:838822011164950582>',
              "ganondorf": '<:ganondorf:838822011324203088>', "ganon": '<:ganondorf:838822011324203088>',
              "ice climbers": '<:iceclimbers:838822010992984117>',
              "ics": '<:iceclimbers:838822010992984117>', "ic": '<:iceclimbers:838822010992984117>',
              "king dedede": '<:kingdedede:838822011224195082>', "king ddd": '<:kingdedede:838822011224195082>',
              "ddd": '<:kingdedede:838822011224195082>', "d3": '<:kingdedede:838822011224195082>',
              "wolf": '<:wolf:838822011215413268>', "lucario": '<:lucario:838822011349893181>',
              "ness": '<:ness:838822011031519314>', "sonic": '<:sonic:838822011202961499>',
              "zero suit samus": '<:zerosuitsamus:838822011299037234>',
              "zero suit": '<:zerosuitsamus:838822011299037234>', "zss": '<:zerosuitsamus:838822011299037234>',
              "bowser": '<:bowser:838822011371257918>', "wario": '<:wario:838822011240448051>',
              "toon link": '<:toonlink:838822011181727774>', "tink": '<:toonlink:838822011181727774>',
              "tl": '<:toonlink:838822011181727774>',
              "rob": '<:rob:838822011375452170>', "r.o.b.": '<:rob:838822011375452170>',
              "olimar": '<:olimar:838822011303362610>', "captain falcon": '<:captainfalcon:838822011370340362>',
              "cf": '<:captainfalcon:838822011370340362>',
              "falcon": '<:captainfalcon:838822011370340362>', "jigglypuff": '<:jigglypuff:838822010929807401>',
              "puff": '<:jigglypuff:838822010929807401>', "lucas": '<:lucas:838822011248836668>',
              "random": '<:random:838822010795589673>'}

opponents = {}
players2matches = {}
matches = {}
searching = {"NETP": {"bo3": [], "bo5": []}, "WIFI": {"bo3": [], "bo5": []}}
searchMessages = {}
challengeMessages = {}

banned = []
with open("banlistsave.json") as f:
    loadbanned = json.load(f)
    fixbanned = []
    for userID in loadbanned:
        fixbanned.append(int(userID))
    banned = fixbanned
    #print(banned)


preranked = {"NETP": {}, "WIFI": {}}
with open("prerankingsave.json") as f:
  loadprerankings = json.load(f)
  fixedprerankingsN = {int(key): value for key, value in loadprerankings["NETP"].items()}
  fixedprerankingsW = {int(key): value for key, value in loadprerankings["WIFI"].items()}
  preranked["NETP"] = fixedprerankingsN
  preranked["WIFI"] = fixedprerankingsW

rankings = {"NETP": {},"WIFI": {}}
with open("rankingsave.json") as f:
  loadRankings = json.load(f)
  fixedRankingsN = {int(key): value for key, value in loadRankings["NETP"].items()}
  fixedRankingsW = {int(key): value for key, value in loadRankings["WIFI"].items()}
  rankings["NETP"] = fixedRankingsN
  rankings["WIFI"] = fixedRankingsW
#print(rankings)

searchIcons = [abort, challenge]
searchSelection = [accept, cancel]
stages = [BF, FD, SV]
winloss = ["<:win:844045482237886465>", "<:loss:844045492798750761>"]
win = "<:win:844045482237886465>"
loss = "<:loss:844045492798750761>"
emotes2stage = {'<:Battlefield:837907213627686943>': "Battlefield",
                '<:FinalDestination:837907213695057950>': "Final Destination",
                '<:Smashville:837907213678542863>': "Smashville"}

def banCheck(userID):
    if userID in banned:
        return True
    else:
        return False

def saveBanList(banlist):
    with open("banlistsave.json", "w") as f:
        json.dump(banlist, f)

def saveRankings(dictionary):
    with open("rankingsave.json", "w") as f:
        json.dump(dictionary, f)


def savePreRanked(dictionary):
    with open("prerankingsave.json", "w") as f:
        json.dump(dictionary, f)

def ELOCapCheck(playerID, matchType):
    if rankings[matchType][playerID] < 1:
        rankings[matchType][playerID] = 1
    elif rankings[matchType][playerID] > 9999:
        rankings[matchType][playerID] == 9999


def showELOChange(newELO, oldELO):
    sign = "+"
    if newELO < oldELO:
        sign = "-"
    changeValue = str(round(abs(newELO - oldELO)))
    showChange = sign + changeValue
    return showChange


def editPreranked(playerID, matchType):
    if playerID in preranked[matchType].keys():
        preranked[matchType][playerID] -= 1
        if preranked[matchType][playerID] == 0:
            preranked[matchType].pop(playerID)
        savePreRanked(preranked)


def displayELO(playerID, matchType):
    elo = rankings[matchType][playerID]
    questionmark = ""
    if playerID in preranked[matchType].keys():
        questionmark = "(?)"
    showELO = str(round(elo)) + questionmark
    return showELO


def findPlayer(LBType, standing):
    rankingList = rankings[LBType]
    strRankingList = {str(key): value for key, value in rankingList.items()}
    sortedRankingList = dict(sorted(strRankingList.items(), key=lambda x: x[1], reverse=True))
    playerList = list(sortedRankingList.keys())
    playerID = standing
    strPreranked = {str(key): value for key, value in preranked[LBType].items()}
    prerankedList = list(strPreranked.keys())
    for player in prerankedList:
        playerList.remove(player)
    if playerID > len(playerList):
        playerID = 0
    else:
        playerID = int(playerList[standing - 1])
    return playerID


def buildLBoard(rankingList, listType, page, matchType):
    strRankingList = {str(key): value for key, value in rankingList.items()}
    sortedRankingList = dict(sorted(strRankingList.items(), key=lambda x: x[1], reverse=True))
    playerList = list(sortedRankingList.keys())
    strPreranked = {str(key): value for key, value in preranked[matchType].items()}
    prerankedList = list(strPreranked.keys())
    for player in prerankedList:
        playerList.remove(player)

    LBContent = "```\n"

    part = 10
    max = part * page

    #if there is no one in the leaderboard
    if len(playerList) == 0:
        LBContent += "No players made it to the leaderboard yet..."
        max = len(playerList)
        begin = len(playerList)
        part = len(playerList)

    # if there are less than 10 players in the leaderboard
    elif max > len(playerList) and len(playerList) < 10:
        max = len(playerList)
        begin = len(playerList)
        part = len(playerList)
    # else if there are fewer players than what the user requests to see
    elif max > len(playerList):
        max = len(playerList)
        begin = 10
    # otherwise the leaderboard is created normally
    else:
        max = 10 * page
        begin = 10

    startindex = max - begin
    #print("start index: ", startindex)
    for index in range(part):
        #("index:", index)
        #print("current index:", startindex + index)
        strPlayerID = playerList[startindex + index]
        intPlayerID = int(strPlayerID)
        playerName = client.get_user(intPlayerID)
        if playerName == None:
            playerName = f"UserID: {strPlayerID}"
        ELO = round(rankings[listType][intPlayerID])
        standing = startindex + index + 1
        player_block = f"{standing}) {playerName}".ljust(41)  # max name length is 32 + room for the #) part
        elo_block = f"[{ELO}]".rjust(6)  # ensure its spaced right
        LBContent += f"{player_block} {elo_block}\n\n"
    return LBContent + "```"


def getPlacement(rankingList, playerID, matchType):
    strPlayerID = str(playerID)
    strRankingList = {str(key): value for key, value in rankingList.items()}
    # print("strRankingList: ", strRankingList)
    sortedRankingList = dict(sorted(strRankingList.items(), key=lambda x: x[1], reverse=True))
    # print("sortedRankingList: ", sortedRankingList)
    playerList = list(sortedRankingList.keys())
    #print("playersList:", playerList)

    strPreranked = {str(key): value for key, value in preranked[matchType].items()}
    prerankedList = list(strPreranked.keys())
    for player in prerankedList:
        playerList.remove(player)

    standing = playerList.index(strPlayerID) + 1
    numOfPlayers = len(playerList)
    return standing, numOfPlayers


def forgetSearch(messageID):
    for messID in searchMessages[messageID]["challenges"]:
        challengeMessages.pop(messID)
    setType = searchMessages[messageID]["setType"]
    matchType = searchMessages[messageID]["matchType"]
    player = searchMessages[messageID]["player"]
    searching[matchType][setType].remove(player)
    searchMessages.pop(messageID)


def forgetMatch(messageID):
    for messID in matches[messageID]["players"].keys():
        opponents.pop(messID)
        players2matches.pop(messID)
    matches.pop(messageID)


def forgetMessage(messageID):
    # if the message is a match window
    if messageID in matches.keys():
        forgetMatch(messageID)
    # if the message is a search message
    elif messageID in searchMessages.keys():
        forgetSearch(messageID)


def addPlayer(player, matchType):
    '''
    adds players to the ranking system
    :param player_id:
    :return:
    '''
    rankings[matchType][player] = 1500
    preranked[matchType][player] = 3
    saveRankings(rankings)
    savePreRanked(preranked)


def calculateELO(winnerID, loserID, matchType, endCheck, modCheck, wNeeded):
    '''
    Calculates new elos for 2 players after a given game
    :param winnerID:
    winner's rating
    :param loserID:
    losers rating
    :param gameCount
    game count of the set
    :return:
    returns reward points
    '''
    endMultiplier = 1
    if endCheck == True:
        if wNeeded == 2:
            endMultiplier = 0.85
        elif wNeeded == 3:
            endMultiplier = 0.7
    elif modCheck ==True:
        endMultiplier = 0.5
    winnerRating = rankings[matchType][winnerID]
    loserRating = rankings[matchType][loserID]
    setMultiplier = 1
    wMultiplier = 1
    lMultiplier = 1
    if winnerID in preranked[matchType].keys():
        wMultiplier = 1.5
    if loserID in preranked[matchType].keys():
        lMultiplier = 1.5

    # calculates the likely-hood of the result not occurring
    score = 1 - (1 / (1 + 10 ** ((loserRating - winnerRating) / 400)))
    multiplier = 21

    if endCheck == True or modCheck ==True:
        wRewardPoints = round(multiplier * score * wMultiplier * endMultiplier)
        lRewardPoints = round(multiplier * score * lMultiplier * endMultiplier)

    elif endCheck == False:
        wRewardPoints = round(multiplier * score * wMultiplier * endMultiplier, 2)
        lRewardPoints = round(multiplier * score * lMultiplier * endMultiplier, 2)


    rankings[matchType][winnerID] += wRewardPoints
    rankings[matchType][loserID] -= lRewardPoints
    rankings[matchType][winnerID] = round(rankings[matchType][winnerID])
    rankings[matchType][loserID] = round(rankings[matchType][loserID])

    ELOCapCheck(winnerID, matchType)
    ELOCapCheck(loserID, matchType)

    saveRankings(rankings)

    newWinnerELO = rankings[matchType][winnerID]
    newLoserELO = rankings[matchType][loserID]
    #print("updated winner elo: ", newWinnerELO)
    #print("updated loser elo: ", newLoserELO)

    return newWinnerELO, newLoserELO


def createCharaList():
    charaList = "Here's a list of all the character inputs I can recognize:\n"
    charaList += "```"
    charaInputs = list(brawlChara.keys())
    sortedCharaInputs = sorted(charaInputs)
    for input in sortedCharaInputs:
        charaEmote = brawlChara[input]
        charaList += f"{input}\n"
    charaList += "```"
    return charaList


@client.event
async def on_ready():
    helpactivity = discord.Activity(name="-helpme", type= 1)
    await client.change_presence(activity= helpactivity)
    print("Bot is ready")
    print(client.user.id)


@client.command()
async def helpme(ctx):
    #fetch change
    user = client.get_user(ctx.message.author.id)
    dm = await user.create_dm()
    await dm.send(f"**command prefix: ``-``**\n"
                  f"(begin every command with ``-`` in order for BrawlBot to recognize your command.)\n"
                  f"\n"
                  f"**__ranked__** ``(Online Type)`` ``(Set Type)``\n"
                  f"> This command begins a search queue for a ranked set. (Only usable in <#{searchChannel}>)\n"
                  f"> Online Type = ``netp`` (if you use netplay) or ``wifi`` (if you use wiimmfi)\n"
                  f"> Set Type = ``bo3`` (best of 3) or ``bo5`` (best of 5)\n"
                  f"> \n"
                  f"> examples:\n"
                  f"> ``-ranked netp bo3``\n"
                  f"> ``-ranked wifi bo5``\n"
                  f"**__rank__**\n"
                  f"> This command allows you to view your own rank and standing in all ladders you're participating in. (Only usable in <#{miscChannel}>)\n"
                  f"> \n"
                  f"> You can look up another player's ranking info by @'ing them after the command.\n"
                  f"> \n"
                  f"> example: ``-rank @APR Financing``\n"
                  f"> \n"
                  f"> You can also look up a specific player based on standing within a specific ladder.\n"
                  f"> \n"
                  f"> exmaples:\n"
                  f"> ``-rank netp 3`` (retrieves the player who is top 3 in the netplay ladder)\n"
                  f"> ``-rank wifi 5`` (retrieves the player who is top 5 in the wiimmfi ladder)\n"
                  f"**__top__** ``(Online Type)`` ``(Page Number)``\n"
                  f"> Displays a leaderboard of the top 10 players for the specified ladder type. (Only usable in <#{miscChannel}>)\n"
                  f"> Online Type = ``netp`` (if you use netplay) or ``wifi`` (if you use wiimmfi)\n"
                  f"> Page Number = input a number to view a specific page of the leaderboard.\n"
                  f"> If no number is given, default page will be 1.\n"
                  f"> \n"
                  f"> examples:\n"
                  f"> ``-top netp`` (Shows the top 1-10 players in the netplay ladder)\n"
                  f"> ``-top wifi 2`` (Shows the top 11-20 players in the wifi ladder)\n"
                  f"> ``-top wifi 3`` (Shows the top 21-30 players in the wifi ladder)\n"
                  f"**__characters__**\n"
                  f"> This command sends a DM with a list containing all character inputs BrawlBot can recognize.\n"
                  f"> This is only relevant during character selections when in a ranked match.\n")
    await ctx.send("I sent you a DM with a list of my commands.")


@client.command()
async def characters(ctx):
    userID = ctx.message.author.id
    #checks if user is banned
    if banCheck(userID) == True:
        return
    channelOrigin = ctx.message.channel.id
    #fetch change
    discordUser = client.get_user(userID)
    dm = await discordUser.create_dm()
    charaList = createCharaList()
    if channelOrigin in channelList:
        await ctx.send("I've sent you a DM with all character inputs I can currently recognize.")
    await dm.send(content=charaList)



@client.command()
async def ban(ctx):
    #checks if command is from the mod channel
    if ctx.message.channel.id != modChannel:
        return

    playerID = int(ctx.message.content[8:-1])
    #print(playerID)

    # checks if player in question is a real person
    if client.get_user(playerID) == None:
        #print("found no one")
        return

    if playerID in banned:
        await ctx.send("That player is already banned.")
        return

    if playerID in rankings["NETP"].keys():
        rankings["NETP"].pop(playerID)
        #print(rankings["NETP"])

    if playerID in rankings["WIFI"].keys():
        rankings["WIFI"].pop(playerID)
        #print(rankings["WIFI"])

    #print("banning: ", playerID)
    banned.append(int(playerID))
    #print(banned)

    saveBanList(banned)
    await ctx.send(f"<@{playerID}> was successfully banned.")


@client.command()
async def unban(ctx):
    # checks if command is from the mod channel
    if ctx.message.channel.id != modChannel:
        return
    playerID = int(ctx.message.content[10:-1])

    #checks if player in question is a real person
    if client.get_user(playerID) == None:
        return

    #checks if player in question is currently banned, otherwise it returns
    if playerID not in banned:
        return

    banned.remove(playerID)
    #print("removed player: ", banned)

    saveBanList(banned)

    await ctx.send(f"<@{playerID}> was successfully unbanned.")


@client.command()
async def changerank(ctx):
    ladderType = ctx.message.content[12:16].upper()

    if ladderType != "NETP" and ladderType != "WIFI":
        await ctx.send("Please specify what ladder you want to change rankings from.")
        return

    ladderColor = attributes[ladderType]["color"]
    winnerID = int(ctx.message.content[20:38].upper())
    loserID = int(ctx.message.content[43:61].upper())
    winnerName = client.get_user(winnerID)
    loserName = client.get_user(loserID)

    if winnerID not in rankings[ladderType].keys() or loserID not in rankings[ladderType].keys():
        await ctx.send(f"One or both of the users are not in the {ladderType} ladder.")
        return

    #print(ctx.message.content)
    #print("ladderType: ", ladderType)
    #print("winnerID: ", winnerID)
    #print("loserID: ", loserID)

    oldWinnerELO = rankings[ladderType][winnerID]
    oldLoserELO = rankings[ladderType][loserID]
    calculateELO(winnerID, loserID, ladderType, endCheck=False, modCheck=True, wNeeded= 2)
    newWinnerELO = displayELO(winnerID, ladderType)
    newLoserELO = displayELO(loserID, ladderType)
    # winnerChange = showELOChange(rankings[ladderType][winnerID], oldWinnerELO)
    # loserChange = showELOChange(rankings[ladderType][loserID], oldLoserELO)
    embed = discord.Embed(
        title=f"Updated ELOs for {winnerName} and {loserName}",
        color=ladderColor,
        description = f"{winnerName} [{newWinnerELO}]\n"
                      f"{loserName} [{newLoserELO}]"
    )
    await ctx.send(embed=embed)


@client.command()
async def top(ctx):
    #checks if command is coming from it's designated channel
    if ctx.message.channel.id != miscChannel:
        await ctx.message.delete()
        await ctx.send(f"This command can only be used in <#{miscChannel}>", delete_after=10)
        return

    #checks if the user is banned
    if banCheck(ctx.message.author.id) == True:
        return

    topType = ctx.message.content[4:9].upper().strip()
    page = ctx.message.content[9:].strip()
    if page == "":
        page = 1
    page = int(page)
    if topType == "WIFI" or topType == "NETP":
        symbol = attributes[topType]["symbol"]
        embed = discord.Embed(
            title=f"{symbol} {topType} Leaderboard",
            color=attributes[topType]["color"],
            description=buildLBoard(rankings[topType], topType, page, topType)
        )
        await ctx.send(embed=embed)
        #print("recognized")
    else:
        await ctx.send("Please specify what type of leaderboard you'd like to view. (NETP or WIFI)", delete_after=10)


@client.command()
async def rank(ctx):
    #checks if command is coming from it's designated channel
    if ctx.message.channel.id != miscChannel:
        await ctx.message.delete()
        await ctx.send(f"This command can only be used in <#{miscChannel}>", delete_after=10)
        return

    authorID = ctx.message.author.id

    if banCheck(authorID) == True:
        return

    if ctx.message.content[6:10].upper() == "NETP" or ctx.message.content[6:10].upper() == "WIFI":
        boardType = ctx.message.content[6:10].upper()
        standing = ctx.message.content[11:]
        if standing == "":
            await ctx.send("Please specify what player standing you'd like to search for \n (ie. ``-rank wifi 3``)",
                           delete_after=8)
            return
        standing = int(standing)
        #print("boardType: ", boardType)
        #print("standing: ", standing)
        playerID = findPlayer(boardType, standing)


    else:
        playerID = ctx.message.content[9:-1]
        #print("ctx:", ctx.message.content)
        #print("playerID:", playerID)
        if playerID == "":
            playerID = authorID
        else:
            playerID = int(playerID)

    playerInfo = client.get_user(playerID)

    # checks if the user is in the rankings

    if playerID == 0:
        await ctx.send("No user with such standing found...")
        return
    elif playerID not in rankings["NETP"] and playerID not in rankings["WIFI"]:
        await ctx.send("No rankings found...")
        return

    embed = discord.Embed(
        title=f"{playerInfo}",
        colour=discord.Colour(defaultColor)
    )
    embed.set_thumbnail(url=playerInfo.avatar_url)

    if playerID in rankings["NETP"]:
        showNetpELO = displayELO(playerID, 'NETP')
        if playerID in preranked["NETP"].keys():
            gamesNeeded = preranked["NETP"][playerID]
            plural = ""
            if gamesNeeded > 1:
                plural = "s"
            valueContentNetp = f"Player currently unranked. \n{gamesNeeded} more game{plural} needed to be ranked."
        else:
            results = getPlacement(rankings["NETP"], playerID, "NETP")
            netpPlacement = results[0]
            netpNumOfPlayers = results[1]
            valueContentNetp = f"(Top {netpPlacement} out of {netpNumOfPlayers})"
        embed.add_field(name=f"{netpSymbol} NETP ELO: {showNetpELO}",
                        value=valueContentNetp,
                        inline=False)

    if playerID in rankings["WIFI"]:
        showWifiELO = displayELO(playerID, 'WIFI')

        if playerID in preranked["WIFI"].keys():
            gamesNeeded = preranked["WIFI"][playerID]
            plural = ""
            if gamesNeeded > 1:
                plural = "s"
            valueContentWifi = f"Player currently unranked. \n{gamesNeeded} more game{plural} needed to be ranked."

        else:
            results = getPlacement(rankings["WIFI"], playerID, "WIFI")
            wifiPlacement = results[0]
            wifiNumOfPlayers = results[1]
            valueContentWifi = f"(Top {wifiPlacement} out of {wifiNumOfPlayers})"
        embed.add_field(name=f"{wifiSymbol} WIFI ELO: {showWifiELO}",
                        value=valueContentWifi,
                        inline=False)
    await ctx.send(embed=embed)


@client.command()
async def ranked(ctx):
    #checks if search message is from the search channel
    if ctx.message.channel.id != searchChannel:
        await ctx.message.delete()
        await ctx.send(f"This command can only be used in <#{searchChannel}>", delete_after=10)
        return
    if banCheck(ctx.message.author.id) == True:
        return
    # if user is already in a match, they will be unable to queue up a search
    if ctx.message.author.id in players2matches.keys():
        await ctx.message.delete()
        await ctx.send("‼ You're currently in a match. ‼", delete_after=4)
        return

    matchType = ctx.message.content[8:12].upper()
    setType = ctx.message.content[13:16]
    if matchType != "NETP" and matchType != "WIFI":
        return
    if setType != "bo3" and setType != "bo5":
        return

    if ctx.message.author.id in searching[matchType][setType]:
        await ctx.send("‼ You're already searching for that. ‼", delete_after=4)
        await ctx.message.delete()
        return

    if matchType == "NETP":
        embedColor = netpColor
        icon = attributes["NETP"]['symbol']
    else:
        embedColor = wifiColor
        icon = attributes["WIFI"]['symbol']

    playerID = ctx.message.author.id

    # if the player isn't already in the ranking system, they get added
    if playerID not in rankings[matchType].keys():
        addPlayer(playerID, matchType)
    #print(rankings)

    showELO = displayELO(playerID, matchType)
    embed = discord.Embed(
        title=f"{ctx.message.author} [{showELO}] is searching for a match... \n"
              f"( {icon} {matchType} || {setType} )",
        description=f"({abort} = cancel search)\n(Search will be deleted after 1 hour)\nClick on {challenge} to challenge them!\n"
                    f"Or unreact to withdraw your challenge.",
        color=discord.Colour(embedColor))
    embed.set_thumbnail(url=f"{ctx.message.author.avatar_url}")
    matchSearch = await ctx.send(embed=embed, delete_after=3600)
    searching[matchType][setType].append(playerID)
    searchMessages[matchSearch.id] = {"player": playerID,
                                      "matchType": matchType,
                                      "setType": setType,
                                      "challenges": [],
                                      "challengers": [],
                                      "color": embedColor,
                                      "messageObj": matchSearch,
                                      "queue": ctx}
    # Keeps track of the player who sent the search, type of match, and type of set. and distinguishes search messages

    #print("searching: ", searching)
    #print("searchMessages:", searchMessages)

    for icon in searchIcons:
        await matchSearch.add_reaction(icon)


@client.event
async def on_message_delete(message):
    messageID = message.id
    if messageID not in searchMessages.keys():
        return
    commandmessage = searchMessages[messageID]["queue"]
    forgetMessage(messageID)
    await commandmessage.message.delete()
    #print("searchMessages should be empty: ", searchMessages)
    #print("challengeMessages should be empty: ", challengeMessages)
    #print("searching should be empty: ", searching)


@client.event
async def on_reaction_add(reaction, user):
    #print("emote:", reaction.emoji)

    if banCheck(user.id) == True:
        return

    messageID = reaction.message.id
    challengerID = user.id
    botID = client.user.id
    if challengerID == botID:  # client.user.id is the bot's ID. This prevents the bot from triggering any of the events when it sets up the emotes
        return

    if reaction.message.author.id != botID:  # Checks if reaction to message is not Brawlbot's
        return

    if messageID in searchMessages.keys() or messageID in matches.keys():  # Checks if this message is one that expects reactions on

        if messageID in searchMessages.keys():
            playerID = searchMessages[messageID]["player"]

        # event the player wants to cancel the search
        if reaction.emoji == abort and challengerID == playerID:  # only the person that queues up can cancel the search
            commandmessage = searchMessages[messageID]["queue"]
            forgetMessage(messageID)
            await reaction.message.delete()
            await commandmessage.message.delete()
            #print("searching should be gone: ", searching)
            #print("searchMessages should have deleted", searchMessages)
            #print("should have deleted challenges", challengeMessages)
        # event when someone clicks on challenge
        elif reaction.emoji == challenge:
            if challengerID == playerID:  # prevents you from challenging yourself
                return
            if user.id in players2matches.keys():
                return
            setType = searchMessages[messageID]["setType"]
            matchType = searchMessages[messageID]["matchType"]
            embedColor = searchMessages[messageID]["color"]
            icon = attributes[matchType]['symbol']
            if challengerID not in rankings[matchType].keys():
                addPlayer(challengerID, matchType)
                #print(rankings)
            showELO = displayELO(challengerID, matchType)
            embed = discord.Embed(
                title=f"{user} [{showELO}] would like to challenge you! \n"
                      f"( {icon} {matchType} || {setType} )",
                description=f"{accept} = accept challenge!",
                color=discord.Colour(embedColor))
            embed.set_thumbnail(url=user.avatar_url)  # shows the challenger's pfp
            #fetch change
            player = client.get_user(playerID)
            dm = await player.create_dm()

            dmChallenge = await dm.send(embed=embed)
            await dmChallenge.add_reaction(accept)

            challengeMessages[dmChallenge.id] = {"challenger": challengerID,
                                                     "searchMessage": reaction.message.id,
                                                     "messageObj": dmChallenge}
            searchMessages[messageID]["challenges"].append(dmChallenge.id)
            searchMessages[messageID]["challengers"].append(user.id)
            #print("challengers: ", searchMessages[messageID]["challengers"])
            #print("challengeMessages: ", challengeMessages)  # testing
            #print("searchMessages:", searchMessages)  # testing

        # event when players are in a match and want to cancel
        elif reaction.emoji == cancel and user.id in matches[messageID]["players"].keys():
            matches[messageID]["cancel"][user.id] = True
            #print("matches:", matches)
            if len(matches[messageID]["cancel"].keys()) == 2:
                matchType = matches[messageID]["matchType"]
                opponent = opponents[user.id]
                rankings[matchType][user.id] = matches[messageID]['players'][user.id]['elo']
                rankings[matchType][opponent] = matches[messageID]['players'][opponent]['elo']
                saveRankings(rankings)

                for plyrs in matches[messageID]["players"].keys():
                    players2matches.pop(plyrs)
                    opponents.pop(plyrs)
                #print("opponents should be empty: ", opponents)
                #print("players should be empty: ", players2matches)
                await matches[messageID]["messageObj"].delete()
                await matches[messageID]["pings"].delete()
                matches.pop(messageID)
                #print("matches should now be gone: ", matches)

        # event when players click on a reaction of a stage
        elif str(reaction.emoji) in matches[messageID]["stages"]:

            # game 1 procedures
            if matches[messageID]["gameCount"] == 1:
                if user.id == matches[messageID]["banning"]:

                    if len(matches[messageID]["stages"]) == 3:
                        matches[messageID]["banning"] = opponents[user.id]
                        matches[messageID]["stages"].remove(str(reaction.emoji))
                        #print("remaining stages: ", matches[messageID]["stages"])  # testing
                        #print("banning: ", matches[messageID]["banning"])  # testing

                        matchWindowObj = matches[messageID]['messageObj']
                        newEmbed = matchWindowObj.embeds[0]
                        nextStrike = opponents[user.id]
                        newEmbed.set_field_at(0, name=f"Game 1",
                                              value=f"{matches[messageID]['heading']}"
                                                    f"\n"
                                                    f"Waiting for <@{nextStrike}> to strike. (click on the reactions):\n"
                                                    f"{matches[messageID]['stages'][0]} {emotes2stage[matches[messageID]['stages'][0]]} \n"
                                                    f"{matches[messageID]['stages'][1]} {emotes2stage[matches[messageID]['stages'][1]]} \n",
                                              inline=False)
                        await reaction.clear()
                        await matchWindowObj.edit(embed=newEmbed)

                    elif len(matches[messageID]["stages"]) == 2:
                        matches[messageID]["banning"] = "N/A"
                        matches[messageID]["stages"].remove(str(reaction.emoji))
                        matchWindowObj = matches[messageID]['messageObj']
                        newEmbed = matchWindowObj.embeds[0]
                        newEmbed.set_field_at(0, name=f"Game 1",
                                              value=f"{matches[messageID]['heading']}"
                                                    f"Stage:\n"
                                                    f"{matches[messageID]['stages'][0]} {emotes2stage[matches[messageID]['stages'][0]]} \n"
                                                    f"\n"
                                                    f"(winner reports by clicking <:win:844045482237886465> / "
                                                    f"loser reports by clicking <:loss:844045492798750761>)",
                                              inline=False)
                        await reaction.clear()
                        await matchWindowObj.clear_reaction(matches[messageID]['stages'][0])
                        await matchWindowObj.edit(embed=newEmbed)
                        for icon in winloss:
                            await matchWindowObj.add_reaction(icon)

            # game 2 and onwards procedures
            elif matches[messageID]["gameCount"] >= 2:
                if user.id == matches[messageID]["banning"]:
                    matchWindowObj = matches[messageID]['messageObj']
                    newEmbed = matchWindowObj.embeds[0]
                    gameCount = matches[messageID]["gameCount"]
                    selecting = opponents[user.id]
                    if len(matches[messageID]["stages"]) == 3:
                        matches[messageID]["banning"] = opponents[user.id]
                        matches[messageID]["stages"].remove(str(reaction.emoji))
                        newEmbed.set_field_at(gameCount - 1, name=f"Game {gameCount}",
                                              value=f""
                                                    f"\n"
                                                    f"Waiting for <@{selecting}> to select their counterpick. (click on the reactions):\n"
                                                    f"{matches[messageID]['stages'][0]} {emotes2stage[matches[messageID]['stages'][0]]} \n"
                                                    f"{matches[messageID]['stages'][1]} {emotes2stage[matches[messageID]['stages'][1]]} \n",
                                              inline=False)
                        await reaction.clear()
                        await matchWindowObj.edit(embed=newEmbed)

                    elif len(matches[messageID]["stages"]) == 2:
                        matches[messageID]["banning"] = "N/A"
                        stage = f"<:{reaction.emoji.name}:{reaction.emoji.id}>"
                        newEmbed.set_field_at(gameCount - 1, name=f"Game {gameCount}",
                                              value=f"(Waiting for character selections...)\n"
                                                    f"Stage:\n"
                                                    f"{stage} {emotes2stage[stage]} \n"
                                                    f"\n",
                                              inline=False)
                        matches[messageID]["heading"] = "N/A"
                        for icon in matches[messageID]['stages']:
                            await matchWindowObj.clear_reaction(icon)
                        matches[messageID]["stages"] = [f"{stage}"]
                        await matchWindowObj.edit(embed=newEmbed)

                        dm = await (client.get_user(selecting)).create_dm()
                        charaSelect = discord.Embed(title=f"[Game {gameCount} | {stage} {emotes2stage[stage]}]",
                                                    description=f"Choose your character for Game {gameCount}! \n Type out what character you will use.\n"
                                                                f"If you're staying on the same character, type ''stay''\n"
                                                                f"\n"
                                                                f"If you're having trouble selecting a character, type ``-characters``"
                                                                 " to see a list of all character inputs I can recognize.",
                                                    color=defaultColor)
                        charaSelect.set_thumbnail(
                            url="https://media.discordapp.net/attachments/405387786036707329/843029286961414144/coinhand2.png")
                        await dm.send(embed=charaSelect)

        # event when win or loss is clicked
        elif str(reaction.emoji) in winloss and user.id in matches[reaction.message.id]["players"]:
            messageID = reaction.message.id
            if str(reaction.emoji) == win:
                matches[messageID]["winner"] = user.id
                #print("checking for winner: ", matches[messageID]["winner"])  # testing
            elif str(reaction.emoji) == loss:
                matches[messageID]["loser"] = user.id
                #print("checking for loser: ", matches[messageID]["loser"])  # testing

            # checks if opponent reported, otherwise it returns
            if str(reaction.emoji) == win and opponents[user.id] != matches[messageID]["loser"]:
                return

            elif str(reaction.emoji) == loss and opponents[user.id] != matches[messageID]["winner"]:
                return

            calculateELO(matches[messageID]["winner"], matches[messageID]["loser"], matches[messageID]["matchType"], endCheck=False, modCheck=False, wNeeded= 2)

            matches[messageID]["selections"][matches[messageID]["winner"]] = True
            matches[messageID]["selections"][matches[messageID]["loser"]] = False
            #print("both win and loss were selected")
            #print("winner should be selecting ", matches[messageID]["selections"][matches[messageID]["winner"]])
            #print("loser should not be selecting ", matches[messageID]["selections"][matches[messageID]["loser"]])
            winner = matches[messageID]['winner']
            loser = matches[messageID]['loser']
            matches[messageID]["players"][winner]["wins"] += 1
            winnerChara = matches[messageID]['players'][winner]['character']
            matchWindowObj = matches[messageID]["messageObj"]
            embedCount = matches[messageID]["gameCount"] - 1
            newEmbed = matchWindowObj.embeds[0]
            newEmbed.set_field_at(embedCount,
                                  name=f"Game {matches[messageID]['gameCount']} (Winner: {winnerChara} {client.get_user(winner)})",
                                  value=f"{matches[messageID]['heading']}"
                                        f"Stage:\n"
                                        f"{matches[messageID]['stages'][0]} {emotes2stage[matches[messageID]['stages'][0]]} \n",
                                  inline=False
                                  )
            await matchWindowObj.edit(embed=newEmbed)
            matches[messageID]["gameCount"] += 1
            matches[messageID]["stages"] = ['<:Battlefield:837907213627686943>',
                                            '<:FinalDestination:837907213695057950>',
                                            '<:Smashville:837907213678542863>']
            matches[messageID]["banning"] = matches[messageID]["winner"]
            matches[messageID]["winner"] = "N/A"
            matches[messageID]["loser"] = "N/A"
            #print("winner should be blank: ", matches[messageID]["winner"])
            #print("loser should be blank: ", matches[messageID]["loser"])
            matches[messageID]["heading"] = "N/A"
            #print("checking for updated game count: ", matches[messageID]["gameCount"])

            # if set is over
            if matches[messageID]["players"][user.id]["wins"] == matches[messageID]["winsNeeded"] or \
                    matches[messageID]["players"][opponents[user.id]]["wins"] == matches[messageID]["winsNeeded"]:
                winsNeed = matches[messageID]["winsNeeded"]
                calculateELO(winner, loser, matches[messageID]["matchType"], endCheck=True, modCheck=False, wNeeded= winsNeed)
                matchType = matches[messageID]['matchType']
                newWinnerELO = rankings[matchType][winner]
                newLoserELO = rankings[matchType][loser]
                oldWinnerELO = matches[messageID]['players'][winner]['elo']
                oldLoserELO = matches[messageID]['players'][loser]['elo']
                winnerChange = showELOChange(newWinnerELO, oldWinnerELO)
                loserChange = showELOChange(newLoserELO, oldLoserELO)
                editPreranked(winner, matchType)
                editPreranked(loser, matchType)
                showWinnerELO = displayELO(winner, matchType)
                showLoserELO = displayELO(loser, matchType)
                forgetMessage(messageID)
                #print("players2matches should be empty: ", players2matches)
                #print("opponents should be empty: ", opponents)
                #print("matches should be forgotten: ", matches)
                embed = matchWindowObj.embeds[0]
                embed.add_field(name=f"Results",
                                value=f"{win} {client.get_user(winner)} [{showWinnerELO}] {winnerChange}\n"
                                      f"{loss} {client.get_user(loser)} [{showLoserELO}] {loserChange}",
                                inline=False)
                await matchWindowObj.edit(embed=embed)
                await matchWindowObj.clear_reactions()
                await matchWindowObj.unpin()

            else:
                banning = matches[messageID]["banning"]
                embed = matchWindowObj.embeds[0]
                embed.add_field(name=f"Game {matches[messageID]['gameCount']}",
                                value=f""
                                      f"\n"
                                      f"Waiting for <@{banning}> to ban. (click on the reactions):\n"
                                      f"{BF} Battlefield \n"
                                      f"{FD} Final Destination \n"
                                      f"{SV} Smashville\n",
                                inline=False)
                await matchWindowObj.edit(embed=embed)
                for icon in winloss:
                    await matchWindowObj.clear_reaction(icon)
                for icon in stages:
                    await matchWindowObj.add_reaction(icon)

        #if the reaction is coming from a mod
        elif reaction.emoji == modkey:
            messageID = reaction.message.id

            #checks if key emote is on a match
            if messageID not in matches.keys():
                return

            matchWindowObj = matches[messageID]["messageObj"]
            embed = matchWindowObj.embeds[0]
            embed.add_field(name="Match was ended by mod.", value="🔨", inline=False)
            forgetMessage(messageID)
            await matchWindowObj.edit(embed=embed)
            await matchWindowObj.clear_reactions()


@client.event
async def on_reaction_remove(reaction, user):
    if banCheck(user.id) == True:
        return

    messageID = reaction.message.id
    userID = user.id
    #print("messageID: ", messageID)
    #print("reaction revoker id: ", userID)
    botID = client.user.id

    # client.user.id is the bot's ID. This prevents the bot from triggering any of the events when it sets up the emotes
    if userID == botID:
        return

    if reaction.emoji == challenge:
        if messageID not in searchMessages.keys():
            return
        searchMessages[messageID]["challengers"].remove(userID)
        #print("user should be removed: ", searchMessages[messageID]["challengers"])
        #print("challenger successfully removed")


@client.event
async def on_raw_reaction_add(payload):
    channel = client.get_channel(matchChannel)
    playerID = payload.user_id
    botID = client.user.id
    #print("payload: ", payload)

    if banCheck(playerID) == True:
        return

    # checks if reaction is on a challenge message
    if payload.message_id not in challengeMessages.keys():
        #print("not in there")
        return

    # event for when accept is clicked on
    elif payload.emoji.name == accept and playerID != botID:
        challengerID = challengeMessages[payload.message_id]['challenger']
        #print("payload: ", payload)
        challengemes = payload.message_id
        searchmes = challengeMessages[challengemes]["searchMessage"]
        #fetch change
        playerName = client.get_user(playerID)
        # fetch change
        challengerName = client.get_user(challengerID)

        #if the challenger withdrew their challenge, the bot deletes the challenge message and notifies the user
        if challengerID not in searchMessages[searchmes]["challengers"]:
            challengeObj = challengeMessages[challengemes]["messageObj"]
            await challengeObj.delete()
            withdrewDM = await playerName.create_dm()
            await withdrewDM.send(f"{challengerName} has withdrawn their challenge.")
            return

        #the the challenger is playing someone else, the bot deletes the challenge message and notifies the user
        if challengerID in players2matches.keys():
            challengeObj = challengeMessages[challengemes]["messageObj"]
            await challengeObj.delete()
            inMatchDM = await playerName.create_dm()
            await inMatchDM.send(f"{challengerName} is currently in a match.")
            return

        matchType = searchMessages[searchmes]["matchType"]
        setType = searchMessages[searchmes]["setType"]
        icon = attributes[matchType]['symbol']
        embedColor = searchMessages[searchmes]["color"]
        if setType == "bo3":
            winsNeeded = 2
        else:
            winsNeeded = 3

        # bot now stops keeping track of the search and corresponding challenge messages
        await searchMessages[searchmes]["queue"].message.delete()
        await searchMessages[searchmes]["messageObj"].delete()
        forgetMessage(searchmes)

        pings = await channel.send(f"<@{playerID}> <@{challengerID}>")

        playerELO = displayELO(playerID, matchType)
        challengerELO = displayELO(challengerID, matchType)
        embed = discord.Embed(
            title=f"{playerName} [{playerELO}] vs {challengerName} [{challengerELO}] \n"
                  f"( {icon} {matchType} || {setType} )",
            description=f"(Both players can agree to cancel the set by clicking: {cancel}.)",
            color=discord.Colour(embedColor))
        embed.add_field(name="Game 1", value="(double blind in progress...)\n")
        matchWindow = await channel.send(embed=embed)
        await matchWindow.pin()
        matches[matchWindow.id] = {
            "players": {playerID: {"character": "N/A", "wins": 0, "elo": rankings[matchType][playerID]},
                        challengerID: {"character": "N/A", "wins": 0, "elo": rankings[matchType][challengerID]}},
            "winsNeeded": winsNeeded,
            "cancel": {},
            "heading": "N/A",
            "gameCount": 1,
            "stages": ['<:Battlefield:837907213627686943>', '<:FinalDestination:837907213695057950>',
                       '<:Smashville:837907213678542863>'],
            "banning": "N/A",
            "selections": {playerID: True, challengerID: True},
            "winner": "N/A",
            "loser": "N/A",
            "pings": pings,
            "messageObj": matchWindow,
            "matchType": matchType
        }
        #print("matches: ", matches)  # testing

        players2matches[playerID] = matchWindow.id
        players2matches[challengerID] = matchWindow.id
        opponents[playerID] = challengerID
        opponents[challengerID] = playerID
        #print("opponents", opponents)
        #print("players: ", players2matches)

        await matchWindow.add_reaction(cancel)
        dm1 = await playerName.create_dm()
        dm2 = await challengerName.create_dm()
        charaSelect = discord.Embed(title="[Game 1] (double blind)",
                                    description="Choose your character! \n Type out what character you will use.\n"
                                                "\n"
                                                "If you're having trouble selecting a character, type ``-characters``"
                                                " to see a list of all character inputs I can recognize.",
                                    color=defaultColor)
        charaSelect.set_thumbnail(
            url="https://media.discordapp.net/attachments/405387786036707329/843029286961414144/coinhand2.png")
        await dm1.send(embed=charaSelect)
        await dm2.send(embed=charaSelect)

        #print("searches should be deleted: ", searchMessages)  # testing
        #print("challenges should be deleted: ", challengeMessages)

    #elif payload.emoji.name == stay and playerID != client.user.id:
        #print("will work on this later")


@client.event
async def on_message(message):
    await client.process_commands(message)
    authorID = message.author.id
    botID = 837093793722662942
    content = str(message.content.lower().strip())

    if banCheck(authorID) ==  True:
        return

    # bot ignores it's own messages
    if authorID == botID:
        return
    # bot ignores non-command based messages if it's not in a DM
    if message.guild in client.guilds:
        return

    # checks if the message author is in a match
    if authorID not in players2matches.keys():
        return

    matchWindowID = players2matches[authorID]

    if matches[matchWindowID]["selections"][authorID] == False:
        return

    if content != "stay" and content not in brawlChara.keys():
        return

    opponent = opponents[authorID]
    matchchannel = f"<#{matchChannel}>"

    # character selection event for game 1
    if matches[matchWindowID]['gameCount'] == 1:
        character = str(message.content.lower().strip())
        if character not in brawlChara.keys():
            return

        matches[matchWindowID]["players"][authorID]["character"] = brawlChara[character]
        selectedDM = await message.author.create_dm()
        selectedChara = discord.Embed(title=f"{matches[matchWindowID]['players'][authorID]['character']} selected!",
                                      description=f"Return to matchmaking: Click here -> {matchchannel}",
                                      color=defaultColor)
        selectedChara.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/845292400440377374/845292550889406494/R2F_smaller.png")
        await selectedDM.send(embed=selectedChara)
        #print("matches for double blinds:", matches)

        # checks if opponent has their character locked in
        if matches[matchWindowID]["players"][opponent]["character"] != "N/A":
            matches[matchWindowID]["selections"][authorID] = False
            matches[matchWindowID]["selections"][opponents[authorID]] = False
            matchWindowObj = matches[matchWindowID]["messageObj"]
            p1ID = authorID
            p1name = client.get_user(authorID)
            p2ID = opponents[authorID]
            p2name = client.get_user(p2ID)
            chara1 = matches[matchWindowID]["players"][p1ID]["character"]
            chara2 = matches[matchWindowID]["players"][p2ID]["character"]
            firstStrike = random.choice([p1ID, p2ID])
            matches[matchWindowID]["banning"] = firstStrike
            newEmbed = matchWindowObj.embeds[0]
            heading = f"({p1name}) {chara1} {versus} {chara2} ({p2name})\n"
            matches[matchWindowID]["heading"] = heading
            newEmbed.set_field_at(0, name=f"Game 1",
                                  value=f"{heading}"
                                        f"\n"
                                        f"Waiting for <@{firstStrike}> to strike. (click on the reactions):\n"
                                        f"{BF} Battlefield \n"
                                        f"{FD} Final Destination \n"
                                        f"{SV} Smashville\n",
                                  inline=False)
            await matchWindowObj.edit(embed=newEmbed)
            for icon in stages:
                await matchWindowObj.add_reaction(icon)

            #print("checking for who's banning: ", matches[matchWindowID])

    # event for character selections game 2 and onwards
    elif matches[matchWindowID]['gameCount'] >= 2:
        selection = str(message.content.lower().strip())

        if selection in brawlChara.keys():
            matches[matchWindowID]['players'][authorID]['character'] = brawlChara[selection]

        # elif selection == "stay":
        # print("nothing changes")

        playerDM = client.get_user(authorID)
        opponentDM = client.get_user(opponents[authorID])
        selectedDM = await playerDM.create_dm()
        selectedChara = discord.Embed(title=f"{matches[matchWindowID]['players'][authorID]['character']} selected!",
                                      description=f"Return to matchmaking: Click here -> {matchchannel}",
                                      color=defaultColor)
        selectedChara.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/845292400440377374/845292550889406494/R2F_smaller.png"
        )
        await selectedDM.send(embed=selectedChara)

        # if the winner is selecting their character
        if matches[matchWindowID]["heading"] == "N/A":
            matches[matchWindowID]["selections"][authorID] = False
            matches[matchWindowID]["selections"][opponents[authorID]] = True
            p1name = client.get_user(authorID)
            chara1 = matches[matchWindowID]['players'][authorID]['character']
            matches[matchWindowID]["heading"] = f"({p1name}) {chara1} {versus} "
            #print(matches[matchWindowID]["heading"])  # testing
            stage = matches[matchWindowID]["stages"][0]
            stageName = emotes2stage[stage]

            playerCharacter = matches[matchWindowID]['players'][authorID]['character']
            gameCount = matches[matchWindowID]['gameCount']
            selectDM = await opponentDM.create_dm()
            charaSelect = discord.Embed(title=f"[Game {gameCount} | {stage} {stageName}]",
                                        description=f"{playerDM} is going {playerCharacter}.\n"
                                                    f"Choose your character for Game {gameCount}! \n Type out what character you will use.\n"
                                                    f"If you're staying on the same character, type ''stay''.\n"
                                                    f"\n"
                                                    f"If you're having trouble selecting a character, type ``-characters``"
                                                     " to see a list of all character inputs I can recognize.",
                                        color=defaultColor)
            charaSelect.set_thumbnail(
                url="https://media.discordapp.net/attachments/405387786036707329/843029286961414144/coinhand2.png")
            await selectDM.send(embed=charaSelect)

        # if the loser is selecting their character
        elif matches[matchWindowID]["heading"] != "N/A":
            matches[matchWindowID]["selections"][authorID] = False
            p2name = client.get_user(authorID)
            chara2 = matches[matchWindowID]['players'][authorID]['character']
            matches[matchWindowID]["heading"] += f"{chara2} ({p2name})\n"
            #print(matches[matchWindowID]["heading"])  # testing

            matchWindowObj = matches[matchWindowID]["messageObj"]
            embedCount = matches[matchWindowID]["gameCount"] - 1
            newEmbed = matchWindowObj.embeds[0]
            newEmbed.set_field_at(embedCount,
                                  name=f"Game {matches[matchWindowID]['gameCount']}",
                                  value=f"{matches[matchWindowID]['heading']}"
                                        f"Stage:\n"
                                        f"{matches[matchWindowID]['stages'][0]} {emotes2stage[matches[matchWindowID]['stages'][0]]} \n",
                                  inline=False
                                  )
            await matchWindowObj.edit(embed=newEmbed)
            for icon in winloss:
                await matchWindowObj.add_reaction(icon)


# last worked on 6/20/2021

client.run("ODM3MDkzNzkzNzIyNjYyOTQy.YIniWA.sU-O0Umesjj1tiKCioFGIm5elA8")
