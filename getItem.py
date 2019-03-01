
import xml.etree.ElementTree as ET
import xmltodict
import json
import getApi


def xmlToSeq(xml_string):

    root = ET.fromstring(xml_string)
    elements = root.findall('body/items/item/seq')

    # dataCrtYm 자료생성년월
    # seq 식별번호

    seq_list = []

    for element in elements:
        seq_list.append(element.text)

    return seq_list

def xmlToDetail(xml_string):

    info_dic = {'wkplNm': 'name', 'bzowrRgstNo': 'number', 'wkplRoadNmDtlAddr': 'address', 'crrmmNtcAmt': 'total_cost',
                'jnngpCnt': 'num_of_employ'}

    root = ET.fromstring(xml_string)
    elements = root.findall('body/item')

    each_info = {}

    for item in elements:
        each_info['name'] = item.find('wkplNm').text # 사업장명
        each_info['number'] = item.find('bzowrRgstNo').text  # 사업자등록번호
        each_info['address'] = item.find('wkplRoadNmDtlAddr').text  # 사업장도로명상세주소
        each_info['nps_cost'] = item.find('crrmmNtcAmt').text  # 사업장도로명상세주소
        each_info['employ'] = item.find('jnngpCnt').text  # 사업장도로명상세주소

        print(each_info)
    return 1
