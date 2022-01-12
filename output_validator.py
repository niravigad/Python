import os
import subprocess


class OutputValidator:
    __file_name: str = "main.c"

    def __init__(self, file_name=__file_name):
        self.__file_name = file_name
        self.__TARGET_VALUE_IN_FILE = "__VALUE__"
        self.__executable_name: str = "executable_name.out"

    def validator(self, value_to_set) -> bool:
        if self.__replace_in_file(value_to_set):
            if self.__compile_file():
                if self.__compile_file():
                    if self.__run_file(value_to_set):
                        print("Process finished with success")
                        return True
        else:
            print("Process finished with success")
            return False

    def __replace_in_file(self, value_to_set) -> bool:
        """
        :param value_to_set:
        :return:
        """
        try:
            print(self.__file_name)
            with open(self.__file_name, "r") as pointer_to_file:
                original_content = pointer_to_file.read()
                if self.__TARGET_VALUE_IN_FILE in original_content:
                    print("Value found in file")
                else:
                    print("Value not found in file")
                    return False
                content_after_replacing = original_content.replace(self.__TARGET_VALUE_IN_FILE, value_to_set)
                if content_after_replacing == original_content:
                    print("unsuccessful to replace the value!")
                    return False
                else:
                    print("Success replacement value!")
            with open(self.__file_name, "w") as pointer_to_file:
                pointer_to_file.write(content_after_replacing)
                return True
        except Exception as err:
            print(f"Got error - {err}")
            return False

    def __compile_file(self) -> bool:
        if os.system(f"gcc {self.__file_name} -o {self.__executable_name}") != 0:
            print("Compilation error!")
            # ToDo add error
            return False
        else:
            return True

    def __run_file(self, target_value) -> bool:
        returned_value = subprocess.call(f"./{self.__executable_name}")
        if str(returned_value) == str(target_value):
            print("Success return our value!")
            return True
        else:
            print("Unsuccessful return our value!")
            return False


    @property
    def file_name(self):
        return self.__file_name

    @property
    def target_value(self):
        return self.__TARGET_VALUE_IN_FILE


if __name__ == '__main__':
    value_to_set = input("Please type the value> \n")
    output_validator_obj: OutputValidator = OutputValidator()
    output_validator_obj.validator(value_to_set)