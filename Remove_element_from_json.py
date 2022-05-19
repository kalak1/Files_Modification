import json
import jsonpath
import os

def find(element, JSON):
  if element in JSON:
    del JSON[element]

  for key in JSON:
    if isinstance(JSON[key], dict):
      find(element, JSON[key])
  return JSON

def remove_element_json(remove_element,input_file_path,output_file_path):
    file_path = open(input_file_path,'r')
    jsonf_read = file_path.read()
    # Convert string to Python dict
    json_dict = json.loads(jsonf_read)
    json_dict1=find(remove_element, json_dict)
    json_string=json.dumps(json_dict1,indent=2)
    print(json_string)
    json_file_write=open(output_file_path, 'w')
    json_file_write.write(json_string)


if __name__=="__main__":
    file_folder = "data_Files"
    input_file_name = "test_payload.json"
    output_file_name = "test_payload_output.json"

    input_file_path = os.path.join(os.path.dirname(__file__), file_folder, input_file_name)
    output_file_path = os.path.join(os.path.dirname(__file__), file_folder, output_file_name)
    element_to_remove="outParams"
    remove_element_json(element_to_remove,input_file_path,output_file_path)

