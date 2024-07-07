

# Module 4 / Task 2 / Get cats info list
def get_cats_info(path) -> list:
    list_of_cats = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                cat_id, cat_name, cat_age = line.split(',')
                list_of_cats.append({"id": cat_id, "name": cat_name, "age": int(cat_age)})
        return list_of_cats

    except FileNotFoundError:
        raise FileNotFoundError('File not found')
    except PermissionError:
        raise PermissionError('Permission denied')
