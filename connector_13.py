from lcu_driver import Connector

from Start import start_team
from Start_person import start_person
from autoaccept import *
from getinfo import getinfo
from set_icon import set_icon
from set_rank import set_rank


def connector_13(oursparehero, enemyhero):
    connector = Connector()
    global menuoption
    lolrunning()
    @connector.ready
    async def connect(connection):
        await getinfo(connection)
        menuoption = 13
        if menuoption == 1:
            await set_icon(connection)
        elif menuoption == 3:
            await set_rank(connection)
        elif menuoption == 5:
            await autoaccept(connection)
        elif menuoption == 12:
            a = await start_team(oursparehero)
        elif menuoption == 13:
            global consequence, counter
            consequence, counter = await start_person(oursparehero, enemyhero)

    @connector.close
    async def disconnect(connection):
        print(inputcolor("[-] ") + "退出进程")

#    asyncio.set_event_loop(asyncio.new_event_loop())
    connector.start()
    print(consequence)
    return consequence, counter