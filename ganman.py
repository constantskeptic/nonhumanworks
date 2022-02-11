from app import app
from gevent.pywsgi import WSGIServer

if __name__ == '__main__':
    # app.run(debug=True, host = '127.0.0.1', port = 8000)
    app.debug = True 
    http_server = WSGIServer(('', 8000), app)
    http_server.serve_forever()