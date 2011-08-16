import os, sys

apache_configuration= os.path.dirname(__file__)
project = os.path.dirname(apache_configuration)
workspace = os.path.dirname(project)
sys.path.append(workspace)

sys.path.insert(0, '/usr/share/virtualenvs/newfies-dialer/lib/python2.6/site-packages')
sys.path.append('/usr/share')
sys.path.append('/usr/share/newfies')

os.environ['DJANGO_SETTINGS_MODULE'] = 'newfies.settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
