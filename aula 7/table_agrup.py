from mysql.connector import Error
import os
import mysql.connector

# Function to connect to the MySQL database
def connect_db():
    try:
        conn = mysql.connector.connect(
            user='root',
            password='ceub123456',
            host='localhost'
        )
        return conn
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

# Function to create the database if it does not exist
def create_database_sql():
    sql_create = "CREATE DATABASE IF NOT EXISTS db_registration"
    cursor.execute(sql_create)
    sql_use = "USE db_registration"
    cursor.execute(sql_use)

# Function to create the tables tb_job and tb_employee
def create_table_sql():
    try:
        # Create the job table
        sql_create_job = '''
        CREATE TABLE IF NOT EXISTS tb_job (
            id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
            job_name VARCHAR(50) UNIQUE NOT NULL
        )'''
        cursor.execute(sql_create_job)

        # Create the employee table
        sql_create_employee = '''
        CREATE TABLE IF NOT EXISTS tb_employee (
            id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
            employee_name VARCHAR(50) NOT NULL,
            birth_date DATE NOT NULL,
            gender ENUM('M', 'F', 'O') NOT NULL,
            salary DECIMAL(10, 2) NOT NULL,
            job_id INT,
            FOREIGN KEY (job_id) REFERENCES tb_job(id)
        )'''
        cursor.execute(sql_create_employee)
    except Error as e:
        print(f"Error executing MySQL: {e}")
        return None

# Function to insert data into the tables
def insert_into_table():
    print("Choose what you want to insert:")
    print("1 - Job")
    print("2 - Employee")
    option = input("Enter the option (1 or 2): ")

    if option == "1":
        # Insert job
        job_name = input("Enter the job name: ")
        sql_insert_job = '''INSERT INTO tb_job (job_name) VALUES (%s)'''
        try:
            cursor.execute(sql_insert_job, (job_name,))
            conn.commit()
            print("Job inserted successfully!")
        except Error as e:
            print(f"Error inserting job: {e}")

    elif option == "2":
        # Insert employee
        employee_name = input("Enter the employee name: ")
        birth_date = input("Enter the birth date (YYYY-MM-DD): ")
        gender = input("Enter the gender (M/F/O): ")
        salary = input("Enter the salary: ")
        job_id = input("Enter the job ID: ")
        sql_insert_employee = '''
            INSERT INTO tb_employee (employee_name, birth_date, gender, salary, job_id)
            VALUES (%s, %s, %s, %s, %s)
        '''
        try:
            cursor.execute(sql_insert_employee, (employee_name, birth_date, gender, salary, job_id))
            conn.commit()
            print("Employee inserted successfully!")
        except Error as e:
            print(f"Error inserting employee: {e}")
    else:
        print("Invalid option!")

# Function to list data from the tables
def list_table():
    print("Choose the table to query:")
    print("1 - tb_job")
    print("2 - tb_employee")
    option = input("Enter the option (1 or 2): ")

    if option == "1":
        # Query jobs
        job_id = input("Enter the job ID to query (or press Enter to list all): ")
        if job_id.strip() == "":
            sql_select = '''SELECT * FROM tb_job'''
            cursor.execute(sql_select)
        else:
            sql_select = '''SELECT * FROM tb_job WHERE id = %s'''
            cursor.execute(sql_select, (job_id,))
        result = cursor.fetchall()
        print("Jobs:")
        for row in result:
            # row: (id, job_name)
            print(row)
        print("Job query completed successfully!")
    elif option == "2":
        # Query employees
        employee_id = input("Enter the employee ID to query (or press Enter to list all): ")
        if employee_id.strip() == "":
            sql_select = '''SELECT * FROM tb_employee'''
            cursor.execute(sql_select)
        else:
            sql_select = '''SELECT * FROM tb_employee WHERE id = %s'''
            cursor.execute(sql_select, (employee_id,))
        result = cursor.fetchall()
        print("Employees:")
        for row in result:
            # row: (id, employee_name, birth_date, gender, salary, job_id)
            id_, name, birth_date, gender, salary, job_id = row
            print((id_, name, birth_date.strftime("%Y-%m-%d"), gender, float(salary), job_id))
        print("Employee query completed successfully!")
    else:
        print("Invalid option!")

# Function to list employees with their job names using JOIN
def list_employees_with_jobs():
    sql = '''
        SELECT e.id, e.employee_name, e.birth_date, e.gender, e.salary, j.job_name
        FROM tb_employee e
        LEFT JOIN tb_job j ON e.job_id = j.id
    '''
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        print("Employees with their jobs:")
        for row in results:
            # row: (id, employee_name, birth_date, gender, salary, job_name)
            id_, name, birth_date, gender, salary, job_name = row
            print((id_, name, birth_date.strftime("%Y-%m-%d"), gender, float(salary), job_name))
        print("Listing completed successfully!")
    except Error as e:
        print(f"Error listing employees with jobs: {e}")

def delete_table():
    print("Choose the table to delete:")
    print("1 - tb_job")
    print("2 - tb_employee")
    option = input("Enter the option (1 or 2): ")

    if option == "1":
        # Delete the job table
        sql_delete = '''DROP TABLE IF EXISTS tb_job'''
        try:
            cursor.execute(sql_delete)
            print("Table tb_job deleted successfully!")
        except Error as e:
            print(f"Error deleting table tb_job: {e}")
    elif option == "2":
        # Delete the employee table
        sql_delete = '''DROP TABLE IF EXISTS tb_employee'''
        try:
            cursor.execute(sql_delete)
            print("Table tb_employee deleted successfully!")
        except Error as e:
            print(f"Error deleting table tb_employee: {e}")
    else:
        print("Invalid option!")

# Function to update a product (example, not used in current tables)
def update_table():
    print("Choose what you want to update:")
    print("1 - Job (cargo)")
    print("2 - Employee (empregado)")
    option = input("Enter the option (1 or 2): ")

    if option == "1":
        # Update job
        job_id = input("Enter the job ID to update: ")
        new_job_name = input("Enter the new job name: ")
        sql_update_job = '''UPDATE tb_job SET job_name = %s WHERE id = %s'''
        try:
            cursor.execute(sql_update_job, (new_job_name, job_id))
            conn.commit()
            print("Job updated successfully!")
        except Error as e:
            print(f"Error updating job: {e}")

    elif option == "2":
        # Update employee
        employee_id = input("Enter the employee ID to update: ")
        new_name = input("Enter the new employee name: ")
        new_birth_date = input("Enter the new birth date (YYYY-MM-DD): ")
        new_gender = input("Enter the new gender (M/F/O): ")
        new_salary = input("Enter the new salary: ")
        new_job_id = input("Enter the new job ID: ")
        sql_update_employee = '''
            UPDATE tb_employee
            SET employee_name = %s, birth_date = %s, gender = %s, salary = %s, job_id = %s
            WHERE id = %s
        '''
        try:
            cursor.execute(sql_update_employee, (new_name, new_birth_date, new_gender, new_salary, new_job_id, employee_id))
            conn.commit()
            print("Employee updated successfully!")
        except Error as e:
            print(f"Error updating employee: {e}")
    else:
        print("Invalid option!")

# Function to delete records from the tables
def delete_record():
    print("Choose the table to delete data from:")
    print("1 - tb_job")
    print("2 - tb_employee")
    option = input("Enter the option (1 or 2): ")

    if option == "1":
        # Delete records from the job table
        job_id = input("Enter the job ID to delete (or press Enter to delete all): ")
        try:
            if job_id.strip() == "":
                cursor.execute("DELETE FROM tb_job")
                print("All jobs deleted successfully!")
            else:
                cursor.execute("DELETE FROM tb_job WHERE id = %s", (job_id,))
                print("Job deleted successfully!")
            conn.commit()
        except Error as e:
            print(f"Error deleting job: {e}")
    elif option == "2":
        # Delete records from the employee table
        employee_id = input("Enter the employee ID to delete (or press Enter to delete all): ")
        try:
            if employee_id.strip() == "":
                cursor.execute("DELETE FROM tb_employee")
                print("All employees deleted successfully!")
            else:
                cursor.execute("DELETE FROM tb_employee WHERE id = %s", (employee_id,))
                print("Employee deleted successfully!")
            conn.commit()
        except Error as e:
            print(f"Error deleting employee: {e}")
    else:
        print("Invalid option!")

# Function to list tables ordered by name
def list_table_ordered():
    print("Choose the table to list ordered:")
    print("1 - tb_job")
    print("2 - tb_employee")
    option = input("Enter the option (1 or 2): ")

    if option == "1":
        # List jobs ordered by name
        sql_select = '''SELECT * FROM tb_job ORDER BY job_name'''
        cursor.execute(sql_select)
        result = cursor.fetchall()
        print("Jobs ordered:")
        for row in result:
            print(row)
        print("Jobs listed successfully!")
    elif option == "2":
        # List employees ordered by name
        sql_select = '''SELECT * FROM tb_employee ORDER BY employee_name'''
        cursor.execute(sql_select)
        result = cursor.fetchall()
        print("Employees ordered:")
        for row in result:
            print(row)
        print("Employees listed successfully!")
    else:
        print("Invalid option!")

# Main function of the program
def main():
    if conn is None:
        return
    print("Connected to the database!")
    while True:
        print("\nMenu:")
        print("c - Create table")
        print("r - List table")
        print("lej - List employees with their jobs (JOIN)")
        print("u - Update (product - exemplo, não implementado para cargo/empregado)")
        print("ij - Insert job (cargo)")
        print("ie - Insert employee (empregado)")
        print("dr - Delete record (cargo/empregado)")
        print("d - Delete table")
        print("e - Exit")
        

        choice = input("Choose an option: ")

        if choice == "c":
            create_table_sql()
        elif choice == "r":
            list_table()
        elif choice == "lej":
            list_employees_with_jobs()
        elif choice == "u":
            update_table()
        elif choice == "ij":
            # Inserir cargo
            original_input = input
            def job_input(prompt):
                if "option" in prompt:
                    return "1"
                return original_input(prompt)
            input_backup = __builtins__.input
            __builtins__.input = job_input
            insert_into_table()
            __builtins__.input = input_backup
        elif choice == "ie":
            # Inserir empregado
            original_input = input
            def emp_input(prompt):
                if "option" in prompt:
                    return "2"
                return original_input(prompt)
            input_backup = __builtins__.input
            __builtins__.input = emp_input
            insert_into_table()
            __builtins__.input = input_backup
        elif choice == "dr":
            delete_record()
        elif choice == "d":
            delete_table()
        elif choice == "e":
            os.system("cls")
            break
        else:
            print("Invalid option!")

        print("\nProgram ended.")

# Program execution
if __name__ == "__main__":
    conn = connect_db()
    if conn is not None:
        cursor = conn.cursor()
        create_database_sql()
        main()
        conn.close()
    else:
        print("Failed to connect to the database.")
