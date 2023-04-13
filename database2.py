import psycopg2

class Job:
    def __init__(self, emp_name, id_company, date_start, salary, job, date_end):
        self.id = 0
        self.emp_name = emp_name
        self.id_company = id_company
        self.date_start = date_start
        self.salary = salary
        self.job = job
        self.date_end = date_end


class Employee:
    def __init__(self, name, age, specialization, list_of_jobs):
        self.name = name
        self.age = age
        self.specialization = specialization
        self.list_of_jobs = list_of_jobs


class Registry:
    def __init__(self, connection):
        self.db = connection
        cur = connection.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS job_registry  
                 (ID INT PRIMARY KEY AUTOINCREMENT,
                 EMP_NAME TEXT NOT NULL,
                 ID_COMPANY INT NOT NULL,
                 DATE_START DATE,
                 SALARY INT,
                 JOB TEXT,
                 DATE_END DATE);''')
        cur.execute('''CREATE TABLE IF NOT EXISTS company
                        (ID INT PRIMARY KEY AUTOINCREMENT,
                        NAME TEXT,
                        DESCRIPTION TEXT
                    );''')
        connection.commit()

    def add_job(self, job):
        cur = self.db.cursor()
        cur.execute('''SELECT MAX(ID) FROM job_registry''')
        max_id = cur.fetchone()
        print(max_id)
        if not max_id:
            max_id = 0
        cur.execute(f'''INSERT INTO job_registry (EMP_NAME, ID_COMPANY, DATE_START, SALARY, JOB, DATE_END) VALUES 
        ({job.emp_name}, {job.id_company}, {job.date_start}, {job.salary}, {job.date_end});''')
        self.db.commit()
        return max_id + 1

    def add_employee(self, employee):
        for j, i in employee.list_of_jobs:
            employee.list_of_jobs[i].id = self.add_job(j)

    def show_employees(self, company):
        cur = self.db.cursor()
        cur.execute(f'''SELECT DISTINCT(EMP_NAME) FROM job_registry WHERE ID_COMPANY = {company}''')


def main():
    connection = psycopg2.connect(
        database="postgres",
        user="postgres",
        password="12345",
        host="127.0.0.1",
        port="5432"
    )
    print("Database opened successfully")

    connection.close()


if __name__ == "__main__":
    main()
