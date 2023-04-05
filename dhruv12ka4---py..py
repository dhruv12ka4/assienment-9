import json

class Employee:

    def employee_details(self):
        file = open('C:/Users/LENOVO/AppData/Local/Programs/Python/Python311/employee.json')
        data = json.load(file)
        data_list = []
        for i in data['Employee']:
            data_list.append(i)
            for i in data_list:
                print('\n',i,'\n')

obj = Employee()
obj.employee_details()
