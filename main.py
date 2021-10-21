class Bill:
    """
    Contains data about a bill such as amount and period.
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Roommate:
    """
    Create a roommate person who lives in a house
    and pays a share of the bill.
    """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, roommate2):
        weight = self.days_in_house / (self.days_in_house + roommate2.days_in_house)
        return weight * bill.amount


class PdfReport:
    """
    Creates a .pdf file that contains information about
    the roommates such as their names, their due amounts
    and the period of the bill.
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, roommate1, roommate2, bill):
        pass


the_bill = Bill(amount=120, period="March 2021")
john = Roommate(name="John", days_in_house=20)
marry = Roommate(name="Marry", days_in_house=25)

print(f"{john.name} pays {round(john.pays(bill=the_bill, roommate2=marry), 2)}.")
print(f"{marry.name} pays {round(marry.pays(bill=the_bill, roommate2=john), 2)}.")
