
# -*- coding: utf8 -*-

import json
from get_api import getSeq, getDetails
from get_item import find_seq_from_xml, xmlToDetail

# 테스트 인풋 JSON
input_info = '{"province": "11", "city": "560", "dong": "110", "company_number": "107878", "name": "호연"}'

company_info = json.loads(input_info) # JSON -> Dictionary

province = company_info['province']
city = company_info['city']
dong = company_info['dong']
company_number = company_info['company_number']
name = company_info['name']

api_result = getSeq(province, city, dong, company_number, name)
seq_list = find_seq_from_xml(api_result)


for each_seq in seq_list:

    details = getDetails(each_seq)

    detail_result = xmlToDetail(details)

    result_json = json.dumps(detail_result) # Dictionary -> JSON

    print(detail_result)

