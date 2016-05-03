"""
Contains route handlers.
"""
import webapp2
from handler import Handler


class Index(Handler):
    """
    Index handler
    """
    def get(self):
        self.render("index.html")

app = webapp2.WSGIApplication([
    ('/', Index),
], debug=False)
