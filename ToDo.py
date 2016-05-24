days_of_week = {
    "Monday":[],
    "Tuesday":[],
    "Wednesday":[],
    "Thursday":[],
    "Friday":[],
    "Saturday":[],
    "Sunday":[]
}
def add(day,question):
    days_of_week[day].append(question)
#add()


def get(day,question):
    days_of_week[day].append(question)
#get()


def choice():
    user_choice = raw_input("How can I help you?")
    while user_choice != "exit":
        if user_choice == "add":
            question = raw_input("What would you like to do?")
            day = raw_input("What day?")
            add(day,question)
choice()
print days_of_week
