from flask import Flask, render_template, request, redirect, url_for
from Gaslah import saveResult, takeNTP, links
import json

app = Flask(__name__, template_folder='template')


@app.route('/')
def root():
    return """
    <h1>Simulasi Swagger UI hehe:)</h1>
<a href="/e-booksdirectory" >GASSS</a>"""


@app.route('/api')
def api():
    return redirect(url_for('root'))


@app.route('/api/e-booksdirectory')
def home():
    return render_template('index.html')


@app.route('/api/e-booksdirectory/search')
def search():
    filters = request.args.get('filters')
    match filters:
        case 'cat':
            value = request.args.get('cat')
            saveResult(links[int(value)-1], value)
            with open(f'Results/detail_category_{value}.json', 'r') as file:
                datas = json.load(file)

            return datas
        case 'new' | 'top' | 'popular':
            countpage = request.args.get('countpage')
            urls = takeNTP(int(countpage), filters)
            saveResult(urls, filters)
            with open(f'Results/detail_category_{filters}.json', 'r') as file:
                datas = json.load(file)

            return datas


app.run(debug=True, host='10.1.22.0')
