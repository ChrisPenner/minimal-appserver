""" Imports config from environment vars """
import os


environment = os.getenv('SERVER_SOFTWARE')
if environment.startswith('Google App Engine'):  # Prod
    from .prod import *
else: # Dev
    from .dev import *
