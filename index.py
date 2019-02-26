
import getApi
import getItem

seq_result = getApi.getSeq('41', '117', '101', '124815')

seq_list = getItem.xmlToSeq(seq_result)

for i in seq_list:
    details = getApi.getDetails(i)

    print(details)
