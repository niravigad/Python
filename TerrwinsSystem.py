import hashlib
import os
import csv
import xlsxwriter

global path

_test_string = "Sys_Call_Test => TestType="
_result_string = "Sys_Call_Test- Finished, "


def csv_insert(data):
    """
    :param data:
    :return:
    """
    with open(csvfilename, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(header)
        writer.writerows(data)


# iterate through all lines and search for tests name and results
def get_tests(file_name, _sn, _datetime):
    """
    :param _datetime:
    :param file_name:
    :param _sn:
    :return:
    """
    flag = False
    with open(file_name, "r") as f:
        lines = f.readlines()
        for line in lines:
            if _test_string in line:
                _test_Type = line[line.find("TestType=")+9:line.find("!")]
                flag = True
            if _result_string in line and _result_string[0].isupper() and flag:
                _result = line[line.rfind(_result_string)+30:]
                data_line = _sn, _datetime, _test_Type, _result,
                # add line to the data structure
                data.append(data_line)
                flag = False


# iterate through all file
def open_files(path):
    """
    :param path:
    :return:
    """
    for file in os.listdir(path):
        if file.startswith("P19800I600000678"):
            _sn = file[:file.find("_")]
            _datetime = file[file.find("_") + 1:file.find(".txt")]
            if file.endswith(".txt"):
                file_path = f"{path}\{file}"
                # call read test file function
                get_tests(file_path, _sn, _datetime)
        else:
            continue



if __name__ == '__main__':
    csvfilename = 'Terrawin reports.csv'
    header = ("SN", "Date", "Test name", "Result")
    data = []
    path = r'R:\Operations\Test_Stations\TerrawinSystem\Reports\Logs\Station 11'
    open_files(path)
    csv_insert(data)


