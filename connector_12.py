from lcu_driver import Connector

from Start import start_team
from Start_person import start_person
from autoaccept import *
from getinfo import getinfo
from set_icon import set_icon
from set_rank import set_rank


def connector_12(oursparehero):
    connector = Connector()
    global menuoption
    lolrunning()
    @connector.ready
    async def connect(connection):
        Menu()
        await getinfo(connection)
        menuoption = 12
        if menuoption == 1:
            await set_icon(connection)
        elif menuoption == 3:
            await set_rank(connection)
        elif menuoption == 5:
            await autoaccept(connection)
        elif menuoption == 12:
            global consequence
            consequence = await start_team(oursparehero)
            print(consequence)
        elif menuoption == 13:
            await start_person()

    @connector.close
    async def disconnect(connection):
        print(inputcolor("[-] ") + "退出进程")

#    asyncio.set_event_loop(asyncio.new_event_loop())
    connector.start()
    print(consequence)
    return consequence

###返还内容值好像有点占空间，附上json。text文件
