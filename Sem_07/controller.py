import model
import view


def run():
    point = view.start_menu()
    if point == 1:
        file_txt = model.txt_data_open()
        print(file_txt)
        point_export = view.export_menu()
        if point_export == 1:
            model.export_txt_txt(file_txt)
        elif point_export == 2:
            model.export_txt_csv(file_txt)
    elif point == 2:
        res = model.csv_data_open()
        view.show_res(res)
        point_export = view.export_menu()
        if point_export == 1:
            model.export_csv_txt()
        elif point_export == 2:
            model.export_csv_csv()
