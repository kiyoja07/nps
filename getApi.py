
"""
공공 데이터 포털 - 국민연금 가입 사업장 내역
"""
import urllib.request
import config

API_URL = 'http://apis.data.go.kr/B552015/NpsBplcInfoInqireService/getBassInfoSearch'
API_KEY = config.apiKey()


def preQuerySender(province, city, dong, companyNum):
    url = API_URL
    service_key = API_KEY
    call_info = '&ldong_addr_mgpl_dg_cd=' + province + '&ldong_addr_mgpl_sggu_cd=' + city + '&ldong_addr_mgpl_sggu_emd_cd=' + dong + '&bzowr_rgst_no=' + companyNum

    request = urllib.request.Request(url + '?serviceKey=' + service_key + call_info)
    request.get_method = lambda: 'GET'
    response_body = urllib.request.urlopen(request).read()

    preResponseResult = str(response_body, "utf-8")
    return preResponseResult

print(preQuerySender('41', '117', '101', '124815'))
