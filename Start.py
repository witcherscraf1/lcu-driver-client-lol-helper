import index
from Ban_start import blue_ban_function


async def start_team(oursparehero):
    WholeChart, ref = index.get_data('LOL英雄数据表.xlsx', 0)
    Side = "蓝方"
    print('输入完毕')
    print('我方备选英雄：', oursparehero)

    # ban
    if Side == '蓝方':
        BannedHero = blue_ban_function(oursparehero, WholeChart)
    print('**********************')
    print('双方禁用英雄：', BannedHero)
    return BannedHero


    # # pick
    # if Side == '蓝方':
    #     OurChosenHero, EnemyChosenHero = blue_pick_function(oursparehero, BannedHero, WholeChart, ref)
    # elif Side == '红方':
    #     OurChosenHero, EnemyChosenHero = red_pick_function(oursparehero, BannedHero, WholeChart, ref)
