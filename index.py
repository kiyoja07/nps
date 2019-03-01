
# -*- coding: utf8 -*-


import getApi
import getItem

seq_result = getApi.getSeq('11', '560', '110', '107878', '호연')
seq_list = getItem.xmlToSeq(seq_result)


for i in range(len(seq_list)):
    each_seq = seq_list[i]
    details = getApi.getDetails(each_seq)

    detail_result = getItem.xmlToDetail(details)

    print(detail_result)



