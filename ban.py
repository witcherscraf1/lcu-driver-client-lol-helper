'''
    根据bp规则，禁用英雄环节:蓝方4楼-红方4楼-蓝方5楼-红方5楼
    因此根据已知己方备选英雄，己方已ban英雄和敌方已ban英雄可给出一个建议ban的英雄

    该函数的整体规则如下：
    首先选出克制我方英雄的列表
    接着在该名单中去除我方的备选英雄，己方已ban英雄和敌方已ban英雄，对剩余英雄进行分析
    由胜率、出场率、ban率和被克制指数综合计算，取得分最高的英雄ban掉
'''


import index
from data_process import get_data_from_name,process_data
import data_process
import random

'''
function:该函数根据我方备选池英雄，我方已ban英雄，敌方已ban英雄等信息，选出对我方阵容最不利的英雄ban掉
input：
    ourSpareHero:我方备选池英雄
    ourbanHero:我方已ban英雄
    enenybanHero:敌方已ban英雄
    wholeChart:excel数据表单中提取的list字典集
output:我方选择ban掉的英雄
'''

def ban(ourSpareHero, ourbanHero, enemybanHero, wholeChart):
    ##ban英雄备选名单
    to_ban_list = []                #ban英雄备选名单
    to_ban_list_score = []          #ban英雄克制指数


    ##胜率比重
    winRateFactor = 0.6
    ##出场率比重
    appearFactor = 0.2
    ##ban率比重
    BanFactor = 0.2


    ##ban英雄备选名单中去除我方英雄备选名单，我方已ban名单以及对方已ban名单
    wholeChart = data_process.process_data(wholeChart)
    for i in range(len(ourSpareHero)):
        HeroData = data_process.get_data_from_name(wholeChart, ourSpareHero[i])
        if (HeroData['被克制英雄1'] not in to_ban_list) and (HeroData['被克制英雄1'] not in ourSpareHero):
            to_ban_list.append(HeroData['被克制英雄1'])
            to_ban_list_score.append(HeroData['被克制指数1'])
        if (HeroData['被克制英雄2'] not in to_ban_list) and (HeroData['被克制英雄2'] not in ourSpareHero):
            to_ban_list.append(HeroData['被克制英雄2'])
            to_ban_list_score.append(HeroData['被克制指数2'])
    ##将待ban名单中去除我方已ban名单
    if len(ourbanHero)!=0:
        for i in range(len(ourbanHero)):
            if ourbanHero[i] in to_ban_list:
                del to_ban_list_score[(to_ban_list.index(ourbanHero[i]))]
                del to_ban_list[(to_ban_list.index(ourbanHero[i]))]
    
    ##将待ban名单中去除敌方已ban名单     
    if len(enemybanHero)!=0:
        for i in range(len(enemybanHero)):
            if enemybanHero[i] in to_ban_list:
                del to_ban_list_score[(to_ban_list.index(enemybanHero[i]))]
                del to_ban_list[(to_ban_list.index(enemybanHero[i]))]

    ##to_ban_list中英雄待ban的综合评分
    print(to_ban_list)
    banScore = []

    ##对to_ban_list中的英雄进行综合评价，为最终结果提供参照标准
    for i in range(len(to_ban_list)):
        HeroData = data_process.get_data_from_name(wholeChart, to_ban_list[i])
        winRateScore = HeroData["胜率"]
        appearScore = HeroData["登场率"]
        BanScore = HeroData["ban率"]
        Score1 = winRateScore*winRateFactor + appearScore*appearFactor + BanScore*BanFactor
        Score2 = to_ban_list_score[i]
        banScore.append(0.7*Score1+0.3*Score2)

    max_score = max(banScore)
    print("x")
    loc = banScore.index(max_score)     #根据最大克制指数反向定位到对应的英雄
    return to_ban_list[loc]

