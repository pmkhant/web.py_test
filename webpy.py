""" CI testing with web.py """

import web

urls = ('/', 'index')

class index:
    def GET(self):
        return "Hello, testing CI!"

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()

