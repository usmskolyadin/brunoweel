"""WSGI entry point for Apache/mod_wsgi on Timeweb shared hosting.

Not used locally or on other platforms — manage.py and doghotel/wsgi.py
handle that. This file only runs under Timeweb's Apache + mod_wsgi, which
looks for a wsgi.py at the site root per its .htaccess rewrite rule.
"""

import os
import sys

SITE_DIR = os.path.dirname(os.path.abspath(__file__))

activate_this = os.path.expanduser("~/venv/bin/activate_this.py")
with open(activate_this) as f:
    exec(f.read(), {"__file__": activate_this})

sys.path.insert(1, SITE_DIR)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "doghotel.settings")

from django.core.wsgi import get_wsgi_application  # noqa: E402

application = get_wsgi_application()
