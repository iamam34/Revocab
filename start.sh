# /bin/bash

. venv/bin/activate
FLASK_APP=server.py FLASK_DEBUG=1 flask run
deactivate
