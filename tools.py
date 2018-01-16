import os, sys, glob

start_path = os.getcwd()
proj_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "projectar.settings")
sys.path.append(proj_path)
os.chdir(proj_path)

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

### scripts ###
from tools.Cleaner import Cleaner
from tools.Sensitives import Sensitives

if sys.argv[1] == 'cleanmigrations':
    c = Cleaner(start_path)
    c.clean_migrations()
    db = start_path + '/db.sqlite3'
    if os.path.exists(db):
        os.remove(db)
        print('Removed database')

elif sys.argv[1] == 'sensitives':
    s = Sensitives(start_path)
    if sys.argv[2] == 'setup':
        s.setup()
    elif sys.argv[2] == 'check':
        s.check()
    elif sys.argv[2] == 'set':
        s.set(sys.argv[3], sys.argv[4])
        s.save()
