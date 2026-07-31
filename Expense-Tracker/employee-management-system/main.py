print("       Employee Management System")
employee_list={}
while True:
    try:
        menu = int(input("""
            1.Add Employee
            2.Search Employee
            3.Update Salary
            4.Delete Employee
            5.Check list
            6. Exit
            Enter option """))
        if menu <1  or menu > 6:
            raise TypeError("enter only 1 to 6")
        if menu == 1:  
            name = input("Enter emloyee name ").lower()
            salary = int(input(f"Enter salary of {name} "))
            if not name.isalpha():
                raise ValueError("Enter only Letters")
            elif name not in employee_list:
                employee_list [name]=salary
            elif name in employee_list:
                raise ValueError("Name is already Exsit")
        elif menu == 2:
            id_name = input("Enter employe name ").lower()
            if id_name in employee_list:
                print(id_name)
            elif id_name not in employee_list:
                print("Employee not found")
        elif menu == 3:
            employee_name = str(input("Enter employee name")).lower()
            update_salary = int(input("Enter upadate salary"))
            if employee_name not in employee_list:
                raise ValueError("Employee not exist")
            elif employee_name in employee_list:
                    employee_list[employee_name]=update_salary
                    print("salary update successfully")
            else:
                print("Employee not resister")
        elif menu == 4:
            employee_del = input("Enter employee name").lower()
            if employee_del in employee_list:
                employee_list.pop(employee_del)
                print(employee_list)
        elif menu == 5:
            print(employee_list)
        elif menu == 6:
           break
    except ValueError as e:
        print(e)
    except TypeError as e:
        print(e)
    except Exception as e:
        print("Error",e)
print(employee_list)
