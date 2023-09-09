from data_process import *
from person_first import ban_person_first_function
import index


async def start_person(oursparehero, enemyhero):

    WholeChart, ref = index.get_data('LOL英雄数据表.xlsx', 0)


    # ban
    BannedHero = ban_person_first_function(oursparehero, WholeChart)
    if enemyhero=="无":
        counter = []
    else:
        Herodata = get_data_from_name(WholeChart, enemyhero)
        counter = []
        counter.append(Herodata['被克制英雄1'])
        counter.append(Herodata['被克制英雄2'])
        counter.append(Herodata['被克制英雄3'])
    return BannedHero, counter

    # print('**********************')
    # print('玩家禁用英雄：', BannedHero)

    # #决定先后手
    # print('请输入我方是先手选取还是后手选取')
    # order = "先手"
    # print('我方是先手选取还是后手选取？', order)

    #pick 进行选取

    # if order == '先手':
    #     OurChosenHero, EnemyChosenHero = first_pick_fucntion(OurSpareHero, BannedHero, WholeChart, ref)    #先手选取没有对位的考虑因素，因此只需要检查预选英雄有无被BAN即可进行选取，若全部被BAN则进行重新输入
    # elif order == '后手':
    #     OurChosenHero, EnemyChosenHero = last_pick_fucntion(OurSpareHero, BannedHero, WholeChart, ref)    #后手选取需要考虑对位因素，因此需要检查预选英雄和对方对位英雄的建议ban位。
