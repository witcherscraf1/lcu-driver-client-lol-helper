import time
from functions import *


class GPS:
    pass


myteam = [GPS()] * 5
# Data[0]
myteam[0].id = '00'
myteam[0].name = 1.1
myteam[0].py = 1.2
myteam[0].vx = 1.3
myteam[0].vy = 1.4

# Data[1]
myteam[1].id = '01'
myteam[1].nama = 2.1
myteam[1].py = 2.2
myteam[1].vx = 2.3
myteam[1].vy = 2.4


async def autoaccept(connection):

    data = await connection.request('GET',
                                    '/lol-lobby/v2/lobby')  # await connection.request('GET', '/lol-lobby/v2/lobby/members')
    resJosn = await  data.json()
    idname = []
    consequence = []
    print(resJosn)

    global idlist
    i = 0
    RANGE = [19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9]
    members = resJosn['members']
    print('获取到的members数据有', members)
    for each in members:
        name = each['summonerName']

        idlist = each['puuid']
        print(f'玩家名字{name}的id是{idlist}')  # 循环打印id与名字
        myteam[i].id = [each['puuid']]
        print(myteam[0].id)
        i = i + 1

        history = await connection.request('GET', f"/lol-match-history/v1/products/lol/{each['puuid']}/matches")
        history = await history.json()
        print(history)
        kill = []
        assist = []
        death = []

        for x in RANGE:
            death.append(history['games']['games'][x]['participants'][0]['stats']['deaths'])
            assist.append(history['games']['games'][x]['participants'][0]['stats']['assists'])
            kill.append(history['games']['games'][x]['participants'][0]['stats']['kills'])
        #                      print (f"死亡数是{death}")
        #                      print (f"击杀是{kill}")
        #                      print (f"助攻数是{assist}")
        #                 myteam[i].horse = tect(kill,assist,death)
        print('击杀数据', kill)
        print('死亡数据', death)
        print('助攻数据', assist)
        kills = sum(kill)
        deaths = sum(death)
        assists = sum(assist)
        myteam[i].horse = tect(kills, deaths, assists)
        print(myteam[i].horse)
        consequence.append(myteam[i].horse)
        idname.append(name)
        i = i + 1

    time.sleep(2)
    return idname, consequence
