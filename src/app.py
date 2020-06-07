from sanic import Sanic, response

app = Sanic(__name__)


@app.route('/')
async def route(request):
    return response.text('hi~')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8070)


