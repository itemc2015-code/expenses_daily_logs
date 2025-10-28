import json
import datetime

class Expenses:
    def __init__(self,description,amount):
        self.description = description
        self.amount = amount

        self.logs = 'expenses.json'
        self.temp_logs = []
        self.datetoday = str(datetime.date.today())

    def display(self):
        print('======= DAILY EXPENSES LOG =======')
        print('1. Income\n2. Expenses\n3. View logs')

    def user_input(self):
            selected_number = {'1':'Income','2':'Expense'}
            self.user_select = input('> ')
            #print(f'{"Income" if self.user_select == "1" else "Expense"} selected')

            if self.user_select == "1":
                print(f'{selected_number["1"]} selected')
                self.user_description = input('Description: ')
                while True:
                    try:
                        self.user_amount = input('Amount: $')
                        self.user_amount = int(self.user_amount)
                        self.store()
                        self.try_again()
                        break
                    except ValueError:
                        print('Invalid amount')
            elif self.user_select == "2":
                print(f'{selected_number["2"]} selected')
                self.user_description = input('Description: ')
                while True:
                    try:
                        self.user_amount = input('Amount: $')
                        self.user_amount = int(self.user_amount)
                        self.store()
                        self.try_again()
                        break
                    except ValueError:
                        print('Invalid amount')
            elif self.user_select == "3":
                if hasattr(self,"view_total"):
                    self.view_total()
                else:
                    print('No such a method')
            else:
                print('Invalid selected')
                self.display()
                self.user_input()
                print()

    def store(self):
        self.type_choosen = "income" if self.user_select == "1" else "expense"

        try:
            with open(self.logs, 'r') as f:
                self.temp_logs = json.load(f)

            new_entry = {"No":len(self.temp_logs)+1, "type":self.type_choosen ,"Description":self.user_description, "Amount":self.user_amount, "Date":self.datetoday}
            self.temp_logs.append(new_entry)

            with open(self.logs,'w') as f:
                json.dump(self.temp_logs,f,indent=4)

        except (json.JSONDecodeError, FileNotFoundError):
            data = [{"No":len(self.temp_logs)+1, "type":self.type_choosen, "Description":self.user_description, "Amount":self.user_amount, "Date":self.datetoday}]
            with open(self.logs,'w') as f:
                json.dump(data,f,indent=4)

    def try_again(self):
            print()
            again = input('Add another? "y" or any key to quit: ')
            is_running = True
            print()
            if again.lower() == 'y':
                self.display()
                self.user_input()
            else:
                print('Exiting....')

class Calculate(Expenses):
    def view_total(self):
        with open(self.logs, 'r') as f:
            self.temp_logs = json.load(f)

        total_income = sum(l['Amount'] for l in self.temp_logs if l['type'] == 'income' )
        total_expenses = sum(l['Amount'] for l in self.temp_logs if l['type'] == 'expense')

        print(f'Total Income: ${total_income}')
        print(f'Total Income: ${total_expenses}')

user = Calculate('description=','amount=')
user.display()
user.user_input()

