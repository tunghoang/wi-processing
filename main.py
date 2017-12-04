import flask as flk;
app = flk.Flask("Hello");
@app.route('/')
def index():
    return "this is index"

@app.route('/hello')
def hello():
    return "Hello world"

app.run()
