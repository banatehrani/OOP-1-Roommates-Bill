import webbrowser
import os

from fpdf import FPDF


class PdfReport:
    """
    Creates an output file that contains information about
    the roommates such as their names, their due amounts
    and the period of the bill.
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, roommate1, roommate2, bill):
        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        # Add image
        pdf.image("files/house.png", w=30, h=30)

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

        # Create the report
        pdf.output(f"pdfreports/{self.filename}")

        # Change directory to pdfreports adn open the pdf
        os.chdir("pdfreports")
        webbrowser.open(self.filename)  # Convert it to absolute path for Mac and Linux
