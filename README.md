# Revocab

web app for reviewing vocabulary (initially designed for Biblical Hebrew)

written in python3 with flask

## local hosting/development

Quickstart: `./start.sh`

Long version:

```python
. venv/bin/activate

# EITHER run the flask server 
FLASK_APP=server.py FLASK_DEBUG=1 flask run
# and go to http:localhost:5000/section/0

# OR generate the static site
python generate_static_site.py
# and go to ./Revocab/static/html/0.html

deactivate
```

## acknowledgements

- vocab file from [Logos](https://www.logos.com/media/VocabLists/Basics%20of%20Biblical%20Hebrew.lbxvl) discovered via [list of vocab lists](https://www.logos.com/training/vocabularylists)
- Hebrew font from [Ezra SIL](http://scripts.sil.org/SILHebrUnic2) (Open Font License permits web distribution)
- [Flask](http://flask.pocoo.org/) python webserver
- [Bootstrap v4](https://getbootstrap.com/) CSS theme and JS components

