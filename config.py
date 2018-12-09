#################
#Configurations
#################
outPutPath = 'output/'
stopWords = ['数据挖掘','教育','NoKeyword']
minFreq = 9
numOfFreqWord = None
numOfClusters = 8
thesaurus = {
    #非规范词:规范词
    '教育领域':'教育',
    '教育资源库':'教育资源',
    '教学质量':'教学评估',
    '教学评价':'教学评估',
    '教育评价':'教学评估',
    'Web数据挖掘':'Web挖掘',
    'Web日志挖掘':'Web挖掘',
    'Web日志':'Web挖掘',
    '高校':'高校教育',
    '高职教育':'职业教育',
    '高职院校':'职业教育',
    '高校管理':'教育管理',
    '教学管理':'教育管理',
    '大数据时代': '大数据',
    '大数据技术': '大数据',
    '大数据挖掘': '大数据',
    'OLAP':'联机分析处理',
    '教育决策支持系统': '决策支持',
    '决策支持系统': '决策支持',
    '决策树算法':'决策树',
    '关联规则挖掘':'关联规则',
    '数据可视化':'可视化',
    '网络学习行为分析':'学习行为',
     '学习行为分析' :'学习行为',
     '网络学习行为':'学习行为',
     '自适应':'自适应学习',
    '自适应学习系统':'自适应学习',
    '数据挖掘技术':'数据挖掘',
    '学习分析技术':'学习分析',
    '现代远程教育':'远程教育',
     '聚类': '聚类分析'
}