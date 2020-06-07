import os

from sanic import Sanic, response

import plotly.express as px
import plotly.io as pio

app = Sanic(__name__)


FILE_TPL = '<option value ="{0}">{1}</option>'
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILES_DIR = os.path.join(BASE_DIR, 'files')
FILES_HTML = ' '.join(FILE_TPL.format(os.path.join(FILES_DIR, name), name) for name in os.listdir(FILES_DIR))

with open(os.path.join(BASE_DIR, 'temp.html')) as tpl:
    template = tpl.read()
    template = template.replace('{files}', FILES_HTML)


@app.route('/graph')
def test(request):
    fig = px.scatter(x=[0, 1, 2, 3, 4], y=[0, 1, 4, 9, 16])
    html = pio.to_html(fig)
    return response.html(html)


@app.route('/', methods=['GET', 'POST'])
async def route(request):
    print(request.args)
    print(request.files)
    return response.html(template)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8070)


