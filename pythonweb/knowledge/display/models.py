from neomodel import StructuredNode, StringProperty,RelationshipTo,RelationshipFrom


# 检查
class XCheck(StructuredNode):
    name = StringProperty(unique_index=True)
    bushiyirenqun = StringProperty()
    linchuangyiyi = StringProperty()
    jibenxinxi = StringProperty()
    zhengchangzhi = StringProperty()
    jianchaguocheng = StringProperty()
    definition = StringProperty()
    zhuyishixiang = StringProperty()
    url = StringProperty()
    # 一个检查对应的多个疾病 检查->疾病
    relatedisease = RelationshipTo('XDisease', 'check_relate_disease')
    #一个疾病对应的多个检查 疾病->检查
    commondisease = RelationshipFrom('XDisease','disease_common_check')
    #与某检查相关的检查
    relatecheck = RelationshipTo('XCheck', 'check_relate_check')
    #某症状对应的多个检查 症状->检查
    relatesymptom = RelationshipFrom('XSymptom','symptom_relate_check')

# 疾病
class XDisease(StructuredNode):
    url = StringProperty(unique_index=True)
    name = StringProperty()
    yufang = StringProperty()
    zhiliao = StringProperty()
    changyongyaopin0 = StringProperty()
    changyongyaopin1 = StringProperty()
    bingyin = StringProperty()
    jianjie = StringProperty()
    # 一个检查对应的多个疾病 检查->疾病
    relatecheck = RelationshipFrom(XCheck, 'check_relate_disease')
    # 一个疾病对应的多个检查 疾病->检查
    commoncheck = RelationshipTo(XCheck, 'disease_common_check')
    #与某疾病相关的多个疾病
    relatedisease =RelationshipTo('XDisease','disease_relate_disease')
    #并发疾病
    simudisease = RelationshipTo('XDisease', 'disease_simultaneous_disease')
    #某症状可能的多个疾病  症状->疾病
    probablesymptom = RelationshipFrom('XSymptom', 'symptom_probable_disease')
    #某疾病对应的多个症状 疾病->症状
    commonsymptom = RelationshipTo('XSymptom', 'disease_common_symptom')

#症状库
class XSymptom(StructuredNode):
    name = StringProperty(unique_index=True)
    jiuzhenkeshi = StringProperty()
    jiancha_content = StringProperty()
    zhengzhuang_yufang = StringProperty()
    zhengzhuang_zhenduan = StringProperty()
    zhengzhuang_yuanyin = StringProperty()
    zhengzhuang_jieshao = StringProperty()
    #某症状对应的多个检查 症状->检查
    relatecheck = RelationshipTo(XCheck, 'symptom_relate_check')
    # 某症状可能的多个疾病  症状->疾病
    probabledisease = RelationshipTo(XDisease, 'symptom_probable_disease')
    #与某症状相关的多个症状
    relatesymptom = RelationshipTo('XSymptom','symptom_relate_symptom')
    # 某疾病对应的多个症状 疾病->症状
    commondisease = RelationshipFrom(XDisease, 'disease_common_symptom')








