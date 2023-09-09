from functions import *

##改变段位，输入要使用官方名称如砖石为Diamond 等等
async def set_rank(connection, rank, division):
    print(inputcolor("[-] ") + "段位 ")
    print(rank)
    rank = rank.upper()
    print(inputcolor("[-] ") + "几: ")
    print(division)
    divison = division.upper()
    response = await connection.request('PUT', '/lol-chat/v1/me',
                                        data={"lol": {"大段位": rank, "多少数字": divison}})
    if response.status == 201:
        print(success("[+] ") + "段位 {0} {1} 已被设置".format(rank, divison))
    else:
        print(warning("[!] ") + "未知错误")