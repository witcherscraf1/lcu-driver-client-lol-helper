from lcu_driver import Connector

from Start import start_team
from Start_person import start_person
from autoaccept import *
from getinfo import getinfo
from set_icon import set_icon
from set_rank import set_rank


def connector_03(rank, division):
    connector = Connector()
    global menuoption
    lolrunning()
    @connector.ready
    async def connect(connection):
        Menu()
        await getinfo(connection)
        menuoption = 3
        if menuoption == 1:
            global id
            id = 0
            await set_icon(connection, id)
        elif menuoption == 3:
            await set_rank(connection, rank, division)
        elif menuoption == 5:
            global consequence
            global idname
            idname, consequence = await autoaccept(connection)
        elif menuoption == 12:
            global oursparehero
            a = await start_team(oursparehero)
        elif menuoption == 13:
            enemyhero = "无"
            consequence, counter = await start_person(oursparehero, enemyhero)

    @connector.close
    async def disconnect(connection):
        print(inputcolor("[-] ") + "退出进程")

#    asyncio.set_event_loop(asyncio.new_event_loop())
    connector.start()