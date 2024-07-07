from script_path_tree import main
from script_cats_info import get_cats_info
from script_salary_info import total_salary


# Path to files for each task
path_cats_list = 'files_for_test/cats_list/cats.txt'
path_employees_list = 'files_for_test/employees_and_salaries/employees.txt'
test_path = 'files_for_test'


# Module 4 / Task 1 /  Calculate total and average salary from file
total, average = total_salary(path_employees_list)
print(f'Result for Module 4 / Task 1')
print(f'Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}\n\n')


# Module 4 / Task 2 / Get cats info list
test_cats_list = get_cats_info(path_cats_list)
print(f'Result for Module 4 / Task 2')
print(f'{test_cats_list}\n\n')


# Module 4 / Task 3 / Print path tree
print(f'Result for Module 4 / Task 3')
main(test_path)
