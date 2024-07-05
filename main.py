

# Calculate total and average salary from file
def total_salary(path) -> set:
    try:
        with open(path, 'r', encoding='utf-8') as file:
            salaries_list = [int(line.split(',')[1]) for line in file]
            sum_salary = sum(salaries_list)
            average_salary = int(sum_salary / len(salaries_list))
        return {sum_salary, average_salary}

    except FileNotFoundError:
        raise FileNotFoundError('File not found')
    except PermissionError:
        raise PermissionError('Permission denied')


# Get cats info list
def get_cats_info(path):
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
