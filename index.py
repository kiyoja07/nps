
# -*- coding: utf8 -*-

import json
from getApi import getSeq, getDetails
from getItem import xmlToSeq, xmlToDetail

# 테스트 인풋 JSON
inputInfo = '{"province": "11", "city": "560", "dong": "110", "company_number": "107878", "name": "호연"}'

company_info = json.loads(inputInfo) # JSON -> Dictionary

province = company_info['province']
city = company_info['city']
dong = company_info['dong']
company_number = company_info['company_number']
name = company_info['name']

seq_result = getSeq(province, city, dong, company_number, name)
seq_list = xmlToSeq(seq_result)


for i in range(len(seq_list)):
    each_seq = seq_list[i]
    details = getDetails(each_seq)

    detail_result = xmlToDetail(details)

    result_json = json.dumps(detail_result) # Dictionary -> JSON

    print(detail_result)

