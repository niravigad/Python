import csv
import json
import operator

from typing import Union, List
# A python class which implements the following API on top_linux.csv file:
    #1.Dump file to json
    #2.Print all users
    #3.Print all commands of user (provide username)
    #4.Get command name by pid
    #5.Print top 5 commands sorted by MEM usage

class ProcessParser:
   
    json_file_name: str = "covert.json"

    def __init__(self, csv_file_name, json_file_name=json_file_name):
        self.csv_file_name: str = csv_file_name
        self.json_file_name: str = json_file_name

    def build_json(self) -> bool:
        data = {}
        try:
            with open(self.csv_file_name, encoding='utf-8') as csvf:
                csvReader = csv.DictReader(csvf)
                for rows in csvReader:
                    key = rows['PID']
                    data[key] = rows
            with open(self.json_file_name, 'w', encoding='utf-8') as jsonf:
                jsonf.write(json.dumps(data, indent=4))
                print("Success to build json file !")
                return True
        except Exception as err:
            print(f"Got an error when trying to build json - error - {err}")
            return False

            # print content of CSV file

    # Complexity - O(n*m)
    def print_users(self) -> bool:
        """
        :return: True
        """
        try:
            with open(self.csv_file_name, "r") as file:
                r_reader = csv.reader(file)
                included_cols: List = [1]
                for row in r_reader:
                    content: List = list(row[i] for i in included_cols)
                    for users in content:
                        print(users)
                return True
        except Exception as err:
            print(f"Got an error when trying to print rows - error - {err}")
        return False

    # Complexity - O(n*m)
    def print_user_commands(self, user_name: str) -> bool:
        """
        :param user_name:
        :return:True
        """
        try:
            with open(self.csv_file_name, "r") as file:
                r_reader = csv.reader(file)
                for row in r_reader:
                    if user_name == row[1]:
                        print(row[11])
                return True
        except Exception as err:
            print(f"Got an exception when trying to print user command - error - {err}")
        return False

    # Complexity - O(nlogn)
    def get_command(self, pid: str) -> Union[bool, str]:
        """
        :param pid:
        :return command:
        """
        try:
            with open(self.csv_file_name, "r") as file:
                r_reader = csv.reader(file)
                for row in r_reader:
                    if pid == row[0]:
                        return row[11]
        except Exception as err:
            print(f"Got an exception when trying to get user command - error - {err}")
        return False

    # Complexity - O(nlogn)
    def top_commands_sorted(self) -> bool:
        """
        :return True:
        """
        try:
            with open(self.csv_file_name, "r") as file:
                r_reader = csv.reader(file)
                sortedlist: List = sorted(r_reader, key=operator.itemgetter(9), reverse=True)
                for i, row in enumerate(sortedlist):
                    print(row)
                    i += 1
                    if i == 5:
                        break
                return True
        except Exception as err:
            print(f"Got an exception when trying to print top commands sorted - error - {err}")
        return False


if __name__ == '__main__':
    # Create class
    process_parser: ProcessParser = ProcessParser("top_linux.csv")
    # Dump file to json - Done
    process_parser.build_json()
    # Print all users
    process_parser.print_users()
    # Print all commands by user - Done
    user_name = input("Enter the user name  you would like to get his commands:")
    process_parser.print_user_commands(user_name)

    # Get command name by pid
    pid = input("Enter the pid you would like to get his commands:")
    result: str = process_parser.get_command(pid)
    print(result)
    # Print top 5 commands sorted by MEM usage
    process_parser.top_commands_sorted()

