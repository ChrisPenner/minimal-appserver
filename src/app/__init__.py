"""
Creates App
"""
import webapp2
from app import config
from app.views.routes import ROUTES


app = webapp2.WSGIApplication(
    ROUTES,
    debug=config.DEBUG
)
