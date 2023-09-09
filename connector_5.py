from lcu_driver import Connector

from Start import start_team
from Start_person import start_person
from autoaccept import *
from getinfo import getinfo
from set_icon import set_icon
from set_rank import set_rank


def connector_5():
    connector = Connector()
    global menuoption
    lolrunning()
    outsparehero = 0
    @connector.ready
    async def connect(connection):
        Menu()
        await getinfo(connection)
        menuoption = 5
        if menuoption == 1:
            await set_icon(connection)
        elif menuoption == 3:
            await set_rank(connection)
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
    print(consequence)
    return idname, consequence