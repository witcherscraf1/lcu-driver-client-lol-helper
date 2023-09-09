from functions import *


#设置头像


async def set_icon(connection, id):
    print(inputcolor("[-] ") + "Icon ID: ")
    print(id)
    id = int(id)
#    id = int(input(inputcolor("[-] ") + "Icon ID: "))
    if id < 78:
        icon = await connection.request('put', '/lol-summoner/v1/current-summoner/icon', data={'profileIconId': id})
        if icon.status == 201:
            print(success("[+] ") + "设置{0} 成功!".format(id))
        else:
            print(warning("[!] ") + "错误")
    else:
        icon = await connection.request('put', '/lol-chat/v1/me', data={"icon": id})
        if icon.status == 201:
            print("[+] 设置头像代号 {0} 成功".format(id))
        else:
            print(warning("[!] ") + "未知错误")