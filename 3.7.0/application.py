from flask import Flask
app = Flask(__name__, static_folder='/home/site/wwwroot')

@app.route('/')
def root():
    return app.send_static_file('hostingstart.html')
