from flask import Flask, render_template, url_for
import random
import time
# import pdfkit
from flask_weasyprint import HTML, render_pdf, CSS
# from weasyprint import HTML as weasyHTML

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World!"

def str_time_prop(start, end, format, prop):
    stime = time.mktime(time.strptime(start, format))
    etime = time.mktime(time.strptime(end, format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(format, time.localtime(ptime))
def random_date(start, end, prop):
    return str_time_prop(start, end, '%m/%d/%Y %I:%M %p', prop)

def generateSalesTable():
    products = [
    "Mobile Phone",
    "TV Set",
    "4WD Car",
    "Motorbike",
    "Bicycle",
    "Text Book",
    "DVD player",
    "Face Masks",
    "Microwave",
    "Mug"
]
    sales = {
        "products":[],
        "orderIds": [],
        "dates":[]
    }
    for item in products:
        sales["products"].append(item)
        sales["dates"].append(random_date("1/1/2020 1:30 PM", "1/1/2021 4:50 AM", random.random()))
        sales["orderIds"].append(random.randint(0,20))

    colnames = ['products', 'dates', 'orderIds']
    rows = zip(*[sales[c] for c in colnames])
    return dict(rows=rows, colnames=colnames)

# Example 1. WeasyPrint

@app.route("/weasyprint")
def makepdf():
    # Make a PDF from another view
    html_doc = HTML(string=hello_html())
    # doc = html.render(stylesheets=[CSS(url_for('static', filename="document_style.css"))])
    return render_pdf(html_doc)


@app.route('/sales')
def hello_html():

    doc = render_template('sales.html', sales=generateSalesTable())
    # pdf = pdfkit.from_string(doc, "test.pdf")
    return doc

# @app.route('/hello_<name>.pdf')
# def hello_pdf(name):
#     # Make a PDF from another view
#     return render_pdf(url_for('hello_html', name=name))

# # Alternatively, if the PDF does not have a matching HTML page:

# @app.route('/hello_<name>.pdf')
# def hello_pdf(name):
#     # Make a PDF straight from HTML in a string.
#     html = render_template('hello.html', name=name)
#     return render_pdf(HTML(string=html))