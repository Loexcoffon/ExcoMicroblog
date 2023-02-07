from app import app

@app.route('/')
@app.route('/index')
def index():
    return "<b><i><u>sup world<u><i><b>"
