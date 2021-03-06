
import xml.etree.ElementTree as ET
import xmltodict
import json
import get_api

# seq는 데이터 식별번호

def find_seq_from_xml(xml_string):

    root = ET.fromstring(xml_string)
    elements = root.findall('body/items/item')

    seq_date = []

    for element in elements:
        each_seq_date = {}

        each_seq_date['seq'] = element.find('seq').text # 식별번호
        each_seq_date['date'] = element.find('dataCrtYm').text # 자료생성 년월
        
        seq_date.append(each_seq_date)

    return seq_date # list

def xmlToDetail(seq_xml_string):

    root = ET.fromstring(seq_xml_string['response_result'])
    elements = root.findall('body/item')

    each_info = {}
    each_info['seq'] = seq_xml_string['seq']
    each_info['date'] = seq_xml_string['date']

    for item in elements:
        each_info['name'] = item.find('wkplNm').text # 사업장명
        each_info['number'] = item.find('bzowrRgstNo').text  # 사업자등록번호
        each_info['biz_category'] = item.find('vldtVlKrnNm').text  # 사업장업종코드명
        each_info['company_category'] = item.find('wkplStylDvcd').text  # 사업장형태구분코드, 1:법인, 2:개인
        each_info['address'] = item.find('wkplRoadNmDtlAddr').text  # 사업장도로명상세주소
        each_info['nps_cost'] = item.find('crrmmNtcAmt').text  # 당월고지금액
        each_info['employ'] = item.find('jnngpCnt').text  # 가입자수

    return each_info
