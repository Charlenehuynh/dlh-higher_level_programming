#!/usr/bin/python3
"""Serialization and deserialization
using XML as an alternative format to JSON."""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """take dict and file, serialize the dict into XML and save to file

    Args:
        dictionary (_type_)
        filename (_type_)
    """
    root = ET.Element("data")
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = value
    ET.ElementTree(root).write(filename)


def deserialize_from_xml(filename):
    # return dict
    new = {}
    result = ET.parse(filename)
    for i in result.getroot().iter():
        if i.tag == "data":
            continue
        else:
            new[i.tag] = str(i.text)
    return new


# sample_dict = {
#     'name': 'John',
#     'age': '28',
#     'city': 'New York'
# }

# xml_file = "data.xml"
# serialize_to_xml(sample_dict, xml_file)
# print(f"Dictionary serialized to {xml_file}")

# deserialized_data = deserialize_from_xml(xml_file)
# print("\nDeserialized Data:")
# print(deserialized_data)
