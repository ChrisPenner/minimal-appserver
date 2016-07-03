from webapp2 import Route


ROUTES = [
    Route('/', handler='app.views.Index', name='index'),
]
