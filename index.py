import json
def data_output(stars):
        for star in stars:
            print(f"ID: {star['id']}, Название: {star['name']}, Созвездие: {star['constellation']}, видна с невооруженным глазом: {star['is_visible']}, радиус: {star['radius']}")
def data_output_by_field(stars):
        number=int(input("Введите номер записи"))
        found=False
        for star in stars:
            if star['id']==number:
                print("\n =========================== Найдено ===========================")
                print(f"ID: {star['id']}, Название: {star['name']}, Созвездие: {star['constellation']}, видна с невооруженным глазом: {star['is_visible']}, радиус: {star['radius']}")
                found = True
                break
            if not found:
                print("\n =========================== Не найдено ===========================")
def add_star(stars):
        id_list = []
        for star in stars:
            id_list.append(star['id'])
            new_id = max(id_list)+1
            new_name = input("Введите название звезды")
            new_constellation = input("Введите созвездие")
            new_is_visible = bool(input("Видна ли звезда невооруженным глазом"))
            new_radius = int(input("Введите звездный радиус"))
            new_star = {
                "id" : new_id,
                "name" : new_name,
                "constellation" : new_constellation,
                "is_visible" : new_is_visible,
                "radius": new_radius
            }
            with open('stars.json', 'r+', encoding='utf-8') as f:    
                stars = json.load(f)
                stars.append(new_star)
                f.seek(0)
                json.dump(stars, f)
def delete_star(stars):
        delet_num = int(input("Введите номер записи, которую хотите удалить"))
        found=False
        for star in stars:
            if star['id']==delet_num:
                stars.remove(star)
                found=True
                break
            if not found:
                print("\n =========================== Не найдено ===========================")
def main():
    operation_count=0
    is_open=True
    with open('stars.json', 'r+', encoding='utf-8') as f:     
        data = json.load(f)
        while is_open == True:
            option=int(input("Выберите действие: \n1 - Вывести все записи \n2 - Вывести запись по полю\n3 - Добавить запись\n4 - Удалить запись по полю\n5 - Выйти из программы\n"))
            if option == 1:
                data_output(data)
                operation_count += 1
            elif option == 2:
                data_output_by_field(data)
                operation_count += 1
            elif option == 3:
                add_star(data)
                operation_count += 1
            elif option == 4:
                delete_star(data)
                operation_count += 1
            elif option == 5:
                print(f"Количество операций {operation_count}")
                is_open = False
            else:
                print("Неверное значение попробуйте снова.")
main()
