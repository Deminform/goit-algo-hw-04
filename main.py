

# Calculate total ane average salary
def total_salary(path) -> set:
    with open(path, 'r', encoding='utf-8') as file:
        salaries_list = [int(line.split(',')[1]) for line in file]
        sum_salary = sum(salaries_list)
        average_salary = int(sum_salary/len(salaries_list))
    return {sum_salary, average_salary}
