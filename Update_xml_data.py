import xml.etree.ElementTree as ET
from datetime import datetime, timedelta
import os


def update_xml_dates(x,y,input_file_path,output_file_path):

    xml_data = ET.ElementTree(file=input_file_path)
    root = xml_data.getroot()

    current_date = datetime.today()
    depart_date = current_date + timedelta(int(x))
    return_date = current_date + timedelta(int(y))

    for depart_tag in root.iter("DEPART"):
        depart_tag.text = depart_date.strftime("%Y%m%d")

    for return_tag in root.iter("RETURN"):
        return_tag.text = return_date.strftime("%Y%m%d")

    xml_data = ET.ElementTree(root)

    with open(output_file_path, 'wb') as fileupdate:
        xml_data.write(fileupdate)

if __name__=="__main__":
    file_folder = "data_Files"
    input_file_name = "test_payload1.xml"
    output_file_name = "test_payload1_output.xml"
    depart_days = 2
    return_days = 3
    input_file_path = os.path.join(os.path.dirname(__file__), file_folder, input_file_name)
    output_file_path = os.path.join(os.path.dirname(__file__), file_folder, output_file_name)
    update_xml_dates(2,4,input_file_path,output_file_path)