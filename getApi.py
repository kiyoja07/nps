
"""
공공 데이터 포털 - 국민연금 가입 사업장 내역
"""
import urllib.request
import config

API_URL_BASE = 'http://apis.data.go.kr/B552015/NpsBplcInfoInqireService/'
service_key = config.apiKey()


def getSeq(province, city, dong, companyNum):

    url_getSeq = "getBassInfoSearch"
    url = API_URL_BASE + url_getSeq
    call_info = '&ldong_addr_mgpl_dg_cd=' + province + '&ldong_addr_mgpl_sggu_cd=' + city + '&ldong_addr_mgpl_sggu_emd_cd=' + dong + '&bzowr_rgst_no=' + companyNum

    request = urllib.request.Request(url + '?serviceKey=' + service_key + call_info)
    request.get_method = lambda: 'GET'
    response_body = urllib.request.urlopen(request).read()

    response_result = str(response_body, "utf-8")
    return response_result

def getDetails(seq):

    url_getDetails = "getDetailInfoSearch"

    url = API_URL_BASE + url_getDetails
    call_info = '&seq=' + str(seq) # + '&data_crt_ym=' + str(year_month)

    request = urllib.request.Request(url + '?serviceKey=' + service_key + call_info)
    request.get_method = lambda: 'GET'
    response_body = urllib.request.urlopen(request).read()

    response_result = str(response_body, "utf-8")
    return response_result






# print(getDetails(62785249))

# def getPeriod(seq):

#     url_getPeriod = "getPdAcctoSttusInfoSearch"

#     url = API_URL_BASE + url_getPeriod
#     call_info = '&seq=' + str(seq) # + '&data_crt_ym=' + str(year_month)

#     request = urllib.request.Request(url + '?serviceKey=' + service_key + call_info)
#     request.get_method = lambda: 'GET'
#     response_body = urllib.request.urlopen(request).read()

#     preResponseResult = str(response_body, "utf-8")
#     return preResponseResult

# print(getPeriod(62785249))