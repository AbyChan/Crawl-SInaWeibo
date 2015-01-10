import sae
import tyanweibodata
from tyanweibodata import wsgi

application = sae.create_wsgi_app(wsgi.application)
