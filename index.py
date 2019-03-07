
# -*- coding: utf8 -*-

import json
import getApi
import getItem


inputInfo = '{"province": "11", "city": "560", "dong": "110", "companyNum": "107878", "name": "호연"}'

comInfo = json.loads(inputInfo) # JSON Decoding 

seq_result = getApi.getSeq(comInfo['province'], comInfo['city'], comInfo['dong'], comInfo['companyNum'], comInfo['name'])
seq_list = getItem.xmlToSeq(seq_result)


for i in range(len(seq_list)):
    each_seq = seq_list[i]
    details = getApi.getDetails(each_seq)

    detail_result = getItem.xmlToDetail(details)

    result_json = json.dumps(detail_result) # JSON Encoding 

    print(detail_result)

