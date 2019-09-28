from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
import app

http_server = HTTPServer(WSGIContainer(app.app))
http_server.listen(6015)
IOLoop.instance().start()