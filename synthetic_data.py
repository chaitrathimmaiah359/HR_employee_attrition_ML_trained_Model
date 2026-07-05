import random
import pandas as pd

random.seed(42)

departments = [
    "Engineering",
    "Sales",
    "HR",
    "Finance",
    "Marketing"
]

data = []

for emp_id in range(1001, 1501):

    age = random.randint(22, 60)

    department = random.choices(
        departments,
        weights=[45,25,10,10,10]
    )[0]

    years = random.randint(0, min(age-21,25))

    salary = random.randint(400000,3000000)

    overtime = random.randint(0,60)

    wfh = random.randint(0,5)

    satisfaction = random.randint(1,5)

    performance = random.randint(1,5)

    promotion = random.choice(["Yes","No"])

    training = random.randint(0,60)

    manager = random.randint(1,5)

    risk = 0

    if satisfaction <= 2:
        risk += 40

    if overtime > 40:
        risk += 25

    if promotion == "No":
        risk += 15

    if salary < 600000:
        risk += 10

    if performance == 1:
        risk += 20

    if years < 2:
        risk += 10

    leave = "Yes" if random.randint(1,100) <= risk else "No"

    data.append([
        emp_id,
        age,
        department,
        salary,
        years,
        overtime,
        wfh,
        satisfaction,
        performance,
        promotion,
        training,
        manager,
        leave
    ])

df = pd.DataFrame(data, columns=[
    "employee_id",
    "age",
    "department",
    "salary",
    "years_at_company",
    "overtime_hours",
    "work_from_home_days",
    "satisfaction_score",
    "performance_rating",
    "promotion_last_2_years",
    "training_hours",
    "manager_rating",
    "left_company"
])

df.to_csv("data/employees.csv", index=False)

print(df.head())