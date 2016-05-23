question = raw_input("What would you like to do?")
day = raw_input("What day?")
days_of_week = {
    "Monday":[],
    "Tuesday":[],
    "Wednesday":[],
    "Thursday":[],
    "Friday":[],
    "Saturday":[],
    "Sunday":[]
}
def add():
    days_of_week[day].append(question)
add()
print days_of_week
