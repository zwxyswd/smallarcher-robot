from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.api import xmpp

class MainPage(webapp.RequestHandler):
    
    
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write('Hello, webapp World!')

class XMPPHandler(webapp.RequestHandler):
    def post(self):
        message = xmpp.Message(self.request.POST)
        message.reply(message.body)

application = webapp.WSGIApplication([('/', MainPage),
                                      ('/_ah/xmpp/message/chat/', XMPPHandler)], debug=True)


def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
