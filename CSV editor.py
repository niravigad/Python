import csv


def main():
    filename = 'people list.csv'
    header = ("", "Name", "ID", "IP", "Phone", "Salary")
    data = [
        (1, "Priscilla Matthews", 384525101, "80.119.117.187", +972-523862672, 12000),
        (2, "Benjamin Douglas", 660652470, "104.29.98.222", +972-557712987, 2000),
        (3, "Jordan Porter", 753184050, "1.10.243.200", +972-532509246, 14000),
        (4, "Jacqueline Hughes", 875322869, "103.255.178.143", +972-551448824, 15000),
        (5, "Max Dunn", 338605579, "88.144.81.24", +972-543503816, 100),
        (6, "Christy Neal", 63386055, "62.113.223.73", +972-542202337, 1200),
        (7, "Jessica Rodriquez", 150318228, "12.189.93.218", +972-558975263, 17000),
        (8, "Terri Gordon", 482018827, "212.74.99.171", +972-505375808, 18000),
        (9, "Frank Hamilton", 790979272, "70.32.16.194", +972-541414650, 19000),
        (10, "Felecia Ford", 534268339, "77.139.213.201", +972-559328061, 121000)
    ]

    writer(header, data, filename, "write")
    reader(filename)
    search(filename, "Terri Gordon")
    updater(filename)


def writer(header, data, filename, option):
    with open(filename, "w", newline="") as csvfile:
        if option == "write":

            movies = csv.writer(csvfile)
            movies.writerow(header)
            for x in data:
                movies.writerow(x)
        elif option == "update":
            writer = csv.DictWriter(csvfile, fieldnames=header)
            writer.writeheader()
            writer.writerows(data)
        else:
            print("Option is not known")

# finds word in a row and prints the entire row

def search(filename, word):
    with open(filename, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
            if word in row:
                print(row)

# print content of CSV file

def reader(filename):
    with open(filename, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

# update column in a file


def updater(filename):
    with open(filename, newline="") as file:
        readData = [row for row in csv.DictReader(file)]
        readData[0]['Example'] = '10'
    readHeader = readData[0].keys()
    writer(readHeader, readData, filename, "update")


if __name__ == "__main__":
    main()
