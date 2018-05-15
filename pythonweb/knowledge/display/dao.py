from __future__ import unicode_literals
from .models import XCheck,XDisease,XSymptom

def getdata(a,type):
    result = []
    relations = []

    # 疾病类型
    if type == 'disease':
        try:
            disease = XDisease.nodes.get(name=a)
        except:
            disease="null"
        # 这里需要判断查询是否为空！直接判空不可行，需要数据库查为空！
        if disease=="null":
            return "null"
        print(disease)
        node = {}
        node['名字'] = disease.name
        node['预防'] = disease.yufang
        node['指导'] = disease.zhiliao
        node['常用药品0'] = disease.changyongyaopin0
        node['常用药品1'] = disease.changyongyaopin1
        node['病因'] = disease.bingyin
        node['检查'] = disease.jianjie
        result.append(node)

        # 疾病对应多个检查
        relation1 = disease.commoncheck.all()
        rela = {}
        rela["checking"] = relation1
        relations.append(rela)

        # 疾病相关的疾病
        relation2 = disease.relatedisease.all()
        rela = {}
        rela["disease"] = relation2
        relations.append(rela)

        # 疾病的并发疾病
        relation3 = disease.simudisease.all()
        rela = {}
        rela["disease"] = relation3
        relations.append(rela)

        # 疾病的常见症状
        relation4 = disease.commonsymptom.all()
        rela = {}
        rela["symptom"] = relation4
        relations.append(rela)

    # 检查类型
    elif type == 'checking':
        try:
            checks = XCheck.nodes.get(name=a)
        except:
            checks="null"
        # 这里需要判断查询是否为空！直接判空不可行，需要数据库查为空！
        if checks=="null":
            return "null"
        # print(checks)
        node = {}
        node['名字：'] = checks.name
        node['基本信息：'] = checks.jibenxinxi
        node['正常值'] = checks.zhengchangzhi
        node['检查过程'] = checks.jianchaguocheng
        node['定义'] = checks.definition
        node['临床意义'] = checks.linchuangyiyi
        node['注意事项'] = checks.zhuyishixiang
        node['不适宜人群'] = checks.bushiyirenqun
        result.append(node)

        # 检查对应多个疾病
        relation1 = checks.relatedisease.all()
        rela = {}
        rela["disease"] = relation1
        relations.append(rela)

        # 检查相关的检查
        relation2 = checks.relatecheck.all()
        rela = {}
        rela["checking"] = relation2
        relations.append(rela)


    # 症状类型
    elif type == 'symptom':
        try:
            symptom = XSymptom.nodes.get(name=a)
        except:
            symptom="null"
        # 这里需要判断查询是否为空！直接判空不可行，需要数据库查为空！
        if symptom=="null":
            return "null"
        # print(symptom)
        node = {}
        node['名字'] = symptom.name
        node['就诊科室'] = symptom.jiuzhenkeshi
        node['检查内容'] = symptom.jiancha_content
        node['症状预防'] = symptom.zhengzhuang_yufang
        node['症状原因'] = symptom.zhengzhuang_yuanyin
        node['症状介绍'] = symptom.zhengzhuang_jieshao
        node['症状诊断'] = symptom.zhengzhuang_zhenduan
        result.append(node)

        # 症状对应多个检查
        relation1 = symptom.relatecheck.all()
        rela = {}
        rela["checking"] = relation1
        relations.append(rela)

        # 症状对应的疾病
        relation2 = symptom.probabledisease.all()
        rela = {}
        rela["disease"] = relation2
        relations.append(rela)

        # 症状相关的症状
        relation3 = symptom.probabledisease.all()
        rela = {}
        rela["symptom"] = relation3
        relations.append(rela)

    elif type == 'drug':
        print("暂时还没有药物哟~")
        return "null"
    else:
        print('error type！')

    for i, r in enumerate(relations):
        for key, value in relations[i].items():
            print(key)
            for i, r in enumerate(value):
                print(r.name)
                dict = {}
                dict["source"] = a
                dict["target"] = r.name
                dict["rela"] = key
                result.append(dict)

    return result