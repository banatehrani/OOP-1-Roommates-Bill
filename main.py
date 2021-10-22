import webbrowser

from fpdf import FPDF


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
        return round(weight * bill.amount, 2)


class PdfReport:
    """
    Creates a .pdf file that contains information about
    the roommates such as their names, their due amounts
    and the period of the bill.
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, roommate1, roommate2, bill):
        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        # Add image
        pdf.image("house.png", w=30, h=30)

        # Insert title
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt="Roommates Bill", border=0, align="C", ln=1)

        # Insert period label and value
        pdf.set_font(family="Times", size=14, style='B')
        pdf.cell(w=100, h=40, txt="Period:", border=0)
        pdf.cell(w=150, h=40, txt=bill.period, border=0, ln=1)

        # Insert name and due amount of the first roommate
        pdf.set_font(family="Times", size=12)
        pdf.cell(w=100, h=25, txt=roommate1.name, border=0)
        pdf.cell(w=150, h=25, txt=str(roommate1.pays(bill, roommate2)), border=0, ln=1)

        # Insert name and due amount of the second roommate
        pdf.cell(w=100, h=25, txt=roommate2.name, border=0)
        pdf.cell(w=150, h=25, txt=str(roommate2.pays(bill, roommate1)), border=0)

        pdf.output(self.filename)

        webbrowser.open(self.filename)  # Convert it to absolute path for Mac and Linux


amount = float(input("Please enter the bill amount: "))
period = float(input("What is the bill period? e.g December 2020:  "))

name1 = input("What is your name? ")
days_in_house1 = int(input(f"How many days did {name1} stay in the house during the bill period? "))

name2 = input("What is the name of the other roommate? ")
days_in_house2 = int(input(f"How many days did {name2} stay in the house during the bill period? "))

the_bill = Bill(amount, period)
roommate1 = Roommate(name1, days_in_house1)
roommate2 = Roommate(name2, days_in_house2)

print(f"{name1} pays {roommate1.pays(bill=the_bill, roommate2=roommate2)}.")
print(f"{name2} pays {roommate2.pays(bill=the_bill, roommate2=roommate1)}.")

pdf_report = PdfReport(filename="Report1.pdf")
pdf_report.generate(roommate1, roommate2, bill=the_bill)
