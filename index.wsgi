import sae
from Myblog import wsgi

application = sae.create_wsgi_app(wsgi.application)
