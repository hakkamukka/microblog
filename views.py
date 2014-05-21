from app import app


# Create the mappings of both URLs to function index()
@app.route('/')
@app.route('/index')
def index():
    return "Hello World!"
