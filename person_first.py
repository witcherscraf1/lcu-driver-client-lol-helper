from ban import ban
from core_algorithm import evaluate_function, update
from data_process import process_data


def ban_person_first_function(OurSpareHero, WholeChart):
    BannedHero = []
    BlueBannedHero = []
    RedBannedHero = []

    # 玩家进行ban
    print('**********************')
    print('玩家进行ban')
    # 根据已有信息调用ban函数，返回建议ban掉的英雄，同时用户也可根据自己的想法更换ban掉的英雄
    RecommandBanHero1 = ban(OurSpareHero, BlueBannedHero, RedBannedHero, WholeChart)
    BannedHero.append(RecommandBanHero1)

    return BannedHero


#    print('敌方已ban英雄：',RedBannedHero)

#
# def first_pick_fucntion(OurSpareHero, BannedHero, WholeChart, ref):
#     # 首先进行数据总表的初始化
#     ########
#     WholeChart = process_data(WholeChart)
#     i = 0
#     while i < len(BannedHero):
#         del WholeChart[ref[BannedHero[i]]]
#         i = i + 1
#
#     while i < len(OurSpareHero):
#         if OurSpareHero[i] in BannedHero:
#             del OurSpareHero[i]
#         else:
#             i = i + 1
#
#     ########
#     # 初始我方已选英雄与敌方已选英雄都是空表
#     ########
#     OurChosenHero = []
#     EnemyChosenHero = []
#
#     ######
#     # 蓝方一选
#     ######
#     print('**********************')
#     print('玩家进行选取')
#     RecommandHero1, OurSpareHero = evaluate_function(OurSpareHero, OurChosenHero, EnemyChosenHero, WholeChart)
#     print('RecommandHero1: ', RecommandHero1)
#     print('请输入我方一选英雄：')
#     BlueChosenHero1 = input()
#     OurSpareHero, OurChosenHero = update(BlueChosenHero1, OurSpareHero, OurChosenHero, WholeChart)
#     print('我方已选英雄：', OurChosenHero)
#     return OurChosenHero,EnemyChosenHero
