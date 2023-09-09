'''
根据bp规则，我方被分配到蓝方和红方是随机的，而红方和蓝方的pb顺序是相反的
该部分为模拟我方为蓝方时，bp过后选择最合适的队伍
'''
from ban import ban

'''
function:当我方为蓝方时，实现ban英雄
input:
    OurSpareHero:我方英雄备选池
    WholeChart:excel数据表单中提取的list字典集
output:
    BannedHero:被ban掉的英雄
'''
def blue_ban_function(OurSpareHero, WholeChart):
    BlueBannedHero=[]
    RedBannedHero=[]

    #蓝方一ban
    print('**********************')
    print('蓝方一ban')
    ##根据已有信息调用ban函数，返回建议ban掉的英雄，同时用户也可根据自己的想法更换ban掉的英雄
    RecommandBanHero1 = ban(OurSpareHero, BlueBannedHero, RedBannedHero, WholeChart)
    print('RecommandBanHero1: ', RecommandBanHero1)
    print('请输入我方一ban英雄：')
    BlueBannedHero.append(RecommandBanHero1)
    print('我方已ban英雄：', BlueBannedHero)
    print('敌方已ban英雄：', RedBannedHero)


    #蓝方二ban
    print('**********************')
    print('蓝方二ban')
    RecommandBanHero2 = ban(OurSpareHero, BlueBannedHero, RedBannedHero, WholeChart)
    BlueBannedHero.append(RecommandBanHero2)
    RecommandBanHero3 = ban(OurSpareHero, BlueBannedHero, RedBannedHero, WholeChart)
    print('RecommandBanHero2: ', RecommandBanHero2)
    print('请输入我方二ban英雄：')
    BlueBannedHero.append(RecommandBanHero3)
    print('我方已ban英雄：', BlueBannedHero)
    print('敌方已ban英雄：', RedBannedHero)

    #蓝方二ban
    print('**********************')
    print('蓝方二ban')
    RecommandBanHero4 = ban(OurSpareHero, BlueBannedHero, RedBannedHero, WholeChart)
    BlueBannedHero.append(RecommandBanHero4)
    RecommandBanHero5 = ban(OurSpareHero, BlueBannedHero, RedBannedHero, WholeChart)
    print('RecommandBanHero2: ', RecommandBanHero4)
    print('请输入我方二ban英雄：')
    BlueBannedHero.append(RecommandBanHero5)
    print('我方已ban英雄：', BlueBannedHero)
    print('敌方已ban英雄：', RedBannedHero)
    
    return BlueBannedHero



    