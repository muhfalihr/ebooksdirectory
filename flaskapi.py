from flask import Flask, render_template, request, redirect, url_for
from Gaslah import returnSuccess, returnError, takeNTP
import json

app = Flask(__name__, template_folder='template')


@app.route('/')
def root():
    return """
    <h1>Simulasi Swagger UI hehe:)</h1>
<a href="/api/e-booksdirectory" >KLIK INI BANG</a>"""


@app.route('/api')
def api():
    return redirect(url_for('root'))


@app.route('/api/e-booksdirectory')
def home():
    return render_template('index.html')


@app.route('/api/e-booksdirectory/search')
def search():
    filters = request.args.get('filters')
    with open('Links/listLinks.json', 'r') as file:
        links = json.load(file)
    match filters:
        case 'cat':
            value = request.args.get('cat')
            try:
                results = returnSuccess(links[int(value)-1])
            except:
                results = returnError()
            return """
<html>
<body style="background-color: black;">
    <pre style="color: white; font-family: monospace; ">{}</pre>
</body>
</html>""".format(results)

        case 'new' | 'top' | 'popular':
            countpage = request.args.get('countpage')
            try:
                urls = takeNTP(int(countpage), filters)
                results = returnSuccess(urls)
            except:
                results = returnError()
            return """
<html>
<body style="background-color: black;">
    <pre style="color: white; font-family: monospace; ">{}</pre>
</body>
</html>""".format(results)


app.run(debug=True, host='10.1.22.0')
