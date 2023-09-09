import json
from functions import *

async def morebotspractice(connection):
    with open("practicetool.json", "r") as read_file:
        data = json.load(read_file)
    # print(data)
    response = await connection.request('post', '/lol-lobby/v2/lobby', data=data)
    if response.status == 200:
        print(success("[+] ") + "完成")
    else:
        print(warning("[!] ") + " 未知错误")