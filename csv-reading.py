import csv

def open_csv():
    with open('list.csv', newline='') as my_file:
        reader = csv.reader(my_file, delimiter=' ', quotechar='|')
        for row in reader:
            print(', '.join(row))


if __name__ == "__main__":
    open_csv();
