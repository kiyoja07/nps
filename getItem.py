
import xml.etree.ElementTree as ET
import xmltodict
import json
import getApi


def xmlToSeq(xml_string):

    root = ET.fromstring(xml_string)
    elements = root.findall('body/items/item/seq')

    seq_list = []

    for element in elements:
        seq_list.append(element.text)

    return seq_list

def xmlToDetail(xml_string):
    return 1
