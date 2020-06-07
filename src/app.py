import os

from sanic import Sanic, response

import plotly.io as pio

from electron_temperature import calc

app = Sanic(__name__)


FILE_TPL = '<option value ="{0}">{1}</option>'
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILES_DIR = os.path.join(BASE_DIR, 'files')
FILES_DICT = {name: os.path.join(FILES_DIR, name) for name in os.listdir(FILES_DIR)}
FILES_HTML = ' '.join(FILE_TPL.format(name, name) for name in os.listdir(FILES_DIR))


with open(os.path.join(BASE_DIR, 'temp.html'), encoding='UTF8') as tpl:
    template = tpl.read()
    template = template.replace('{files}', FILES_HTML)


@app.route('/graph')
def test(request):
    #print(request.args)
    #print(request.files)
    query1 = request.args.get('query1', '')
    query2 = request.args.get('query2', '')
    file_name = request.args.get('file_name', '')
    try:
        fig = calc(FILES_DICT[file_name], query1, query2)
        html = pio.to_html(fig)
        return response.html(html)
    except:
        return response.text('no graph')

@app.route('/', methods=['GET', 'POST'])
async def route(request):
    query1 = request.args.get('query1', '')
    query2 = request.args.get('query2', '')
    file_name = request.args.get('file_name', '')
    temp = template.replace('{query1}', query1)
    temp = temp.replace('{query2}', query2)
    temp = temp.replace('{file_name}', file_name)
    #print(request.args)
    #print(request.files)
    return response.html(temp)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8070)


