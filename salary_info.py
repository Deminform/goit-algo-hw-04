# Module 4 / Task 1 /  Calculate total and average salary from file
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
