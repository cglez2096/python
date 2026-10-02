
from fpdf import FPDF

pdf = FPDF()

pdf.add_page()
pdf.set_font("helvetica", size=20)
pdf.write(5,"To find out whats new in tutorial, click")
pdf.set_font(style="U")
link = pdf.add_link(page=2)
pdf.write(5," here",link)

#SECOND PAGE

pdf.add_page()
pdf.image("Icon.png",10,10,50,0,"","https://www.google.com")
pdf.set_left_margin(60)
pdf.set_font_size(18)
pdf.write_html(""" YOU CAN ADD ANY HTML CODE HERE <b> This text is BOLD </b>
                    <h1> This is heading</h1>
                    <a href = "https:www.google.com"> Click here to go to google</a>" """)

pdf.output('link.pdf')





