from functions import *
async def getinfo(connection):
    summoner = await connection.request('get', '/lol-summoner/v1/current-summoner')
    if summoner.status != 200:
        print(warning("[!] ") + "Login into your account!")
    else:
        resJson = await summoner.json()
        DisplayName = resJson['displayName']
        Level = resJson['summonerLevel']
        print(inputcolor("Username: ") + DisplayName)
        print(inputcolor("Level: ") + Level)
        print("")