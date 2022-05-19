import csv
from datetime import datetime
import os

def display_failed_messages(log_file_name):
    file_read_log = open(log_file_name,'r')
    csv_file_reader = csv.reader(file_read_log, delimiter=',')
    header = next(csv_file_reader)
    resp_code_index = header.index("responseCode")
    label_index = header.index("label")
    response_message_index = header.index("responseMessage")
    failure_message_index = header.index("failureMessage")
    timestamp_index = header.index("timeStamp")
    for row_data in csv_file_reader:
        if row_data[resp_code_index] != "200":
            time_stamp_data = row_data[timestamp_index]
            if len(str(time_stamp_data)) == 13:
                time_stamp_data = float(time_stamp_data) / 1000.0
            time_stamp_data1 = datetime.fromtimestamp(time_stamp_data)
            print("The record is non-200 response and details are :: {},{},{},{},{}".format(time_stamp_data1,
                                                                                            row_data[label_index],
                                                                                            row_data[resp_code_index],
                                                                                            row_data[
                                                                                                response_message_index],
                                                                                            row_data[
                                                                                                failure_message_index]))

if __name__=="__main__":
    file_folder = "data_Files"
    input_file_name = "Jmeter_log1.jtl"
    log_file_name_path = os.path.join(os.path.dirname(__file__), file_folder, input_file_name)
    display_failed_messages(log_file_name_path)