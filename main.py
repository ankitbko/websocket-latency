from tornado import web, ioloop
import frame_handler

class IndexHandler(web.RequestHandler):
    """Handler for the root endpoint for the application running on
    Tornado Web Server. Not used to handle requests

    Args:
        web (_type_): Request handler
    """
    def get(self):
        self.render('index.html')

app = web.Application([
    (r'/', IndexHandler),
    (r'/ws/frame', frame_handler.FrameHandler),
])


if __name__ == '__main__':
    app.listen(7001)
    ioloop.IOLoop.instance().start()