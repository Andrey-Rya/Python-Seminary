import csv
from re import S


def csv_data_open():      # opening a file csv
    with open("csv_data.csv", encoding='utf-8') as file:
        file_csv = csv.reader(file, delimiter=";")
        res = list(file_csv)
    return res


def txt_data_open():     # opening a file txt
    with open("txt_data.txt", "rt", encoding='utf-8') as file:
        file_txt = file.read()
    return file_txt


def export_txt_txt(file_txt):    # export from txt in txt
    with open("txt-txt_data_out.txt", "w", encoding='utf-8') as txt_txt_data_out:
        txt_txt_data_out.write(file_txt)


def export_txt_csv(file_txt):    # export from txt in csv
    file_txt = file_txt.replace(' ', ';')
    with open("txt-csv_data_out.csv", "w", encoding='utf-8') as txt_csv_data_out:
        txt_csv_data_out.write(file_txt)


def export_csv_csv():     # export from csv in csv
    with open('csv_data.csv', encoding="utf8") as csvfile, open('csv-csv_data_out.csv', 'w', encoding="utf8", newline='') as f:
        reader = csv.reader(csvfile, delimiter=';')
        writer = csv.writer(f, delimiter=';')
        for row in reader:
            writer.writerow(row)


def export_csv_txt():     # export from csv in txt
    list_csv = csv_data_open()
    for i in list_csv:
        s = ' '.join(i)
        with open("csv-txt_data_out.txt", "w", encoding='utf-8') as f:
            f.writelines(s + '\n')
