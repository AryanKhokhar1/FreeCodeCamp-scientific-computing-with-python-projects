class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def __str__(self) -> str:
        nameLength = len(self.name)

        startLength = round((30 - nameLength) / 2)
        firstLine = "*" * startLength + self.name + "*" * (30 - startLength -
                                                           nameLength)

        def line(dictionary):
            lenOfDesc = len(dictionary["description"])
            amountStr = str('%.2f' % dictionary["amount"])
            desc = dictionary["description"]

            lenOfAmount = len(amountStr)

            if lenOfAmount > 7:
                amountStr = amountStr[:7]
                lenOfAmount = 7
            if lenOfDesc > 23:
                desc = desc[0:23]
                lenOfDesc = 23

            theLine = desc + " " * (30 - lenOfAmount - lenOfDesc) + amountStr
            return theLine

        totalAmt = '%.2f' % self.get_balance()

        return firstLine + '\n' + '\n'.join(map(
            line, self.ledger)) + '\n' + f'Total: {totalAmt}'

    def deposit(self, amount, description=""):
        object = {"amount": amount, "description": description}
        self.ledger.append(object)

    def get_balance(self):
        current_balance = 0
        for i in range(len(self.ledger)):
            current_balance += self.ledger[i]["amount"]
        return current_balance

    def check_funds(self, amount):
        if self.get_balance() < amount:
            return False
        else:
            return True

    def withdraw(self, amount, description=''):
        if self.check_funds(amount) == True:
            object = {"amount": -amount, "description": description}
            self.ledger.append(object)
            return True
        else:
            return False

    def transfer(self, amount, category):
        if self.withdraw(amount, f'Transfer to {str(category.name)}') == False:
            return False
        else:
            category.deposit(amount,f'Transfer from {str(self.name)}')
        return True  

def create_spend_chart(categories):
    category_list = []
    spend_amount = []
    total_amount = 0
    percent_amount = []
    for category in categories:
        category_list.append(category.name)

        amount = 0
        for i in category.ledger:
            if i["amount"] < 0:

                amount += abs(i["amount"])
        spend_amount.append(amount)
        total_amount += amount
    for i in spend_amount:

        percent_amount= list(map(lambda amount: int((((amount / total_amount) * 10) // 1) * 10), spend_amount))
    Line = "Percentage spent by category\n"

    for value in reversed(range(0, 101, 10)):
        if value == 0:
            string = "  " + str(value) + "|"
        elif value < 100:
            string = " " + str(value) + "|"
        else:
            string = str(value) + "|"
        for i in percent_amount:
            if i >= value :
                string += " o "
            else:
                string += "   "

        Line += string + ' \n'

    dashLength = len(spend_amount) * 3 + 1
    Line += "    " + "-" * dashLength + '\n'

    longestStr = max(category_list, key=len)
    longestStrNum = len(longestStr)
    
    for value in range(0, longestStrNum):
        Line += "    "
        number = 1
        for category in category_list:
            
            if len(category) > value:

                Line += (" " + category[value] + " ")
                if number == len(category_list):
                    Line+=" "
                

            else:
                Line += "   "
              
            number+=1
        Line += "\n"
    Line = Line.rstrip()
    Line += "  "

    return Line

food = Category("Food")
# print(create_spend_chart([food, clothing, auto]))
entertainment = Category("Entertainment")
business = Category("Buinsess")
food.deposit(900, "deposit")
entertainment.deposit(900, "deposit")
business.deposit(900, "deposit")
food.withdraw(105.55)
entertainment.withdraw(33.40)
business.withdraw(10.99)
print(create_spend_chart([business, food,entertainment]))