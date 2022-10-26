

def start_menu():
    print('Что Вы хотите сделать?')
    print('\nЕсли Вы хотите открыть файл txt нажмите - 1; а если в файл csv - нажмите 2')
    return int(input('ввод цифры: '))



def export_menu():
    print('\nВыберите необходимое действие!')
    print('Если Вы хотите экспортировать данные в файл txt, нажмите - 1; а если в файл csv - нажмите 2\n для выхода нажмите другую кнопку')
    return int(input('ввод цифры: '))



def show_res(res):
    for i, row in enumerate(res):
        print(i, ' '.join(row))
        
