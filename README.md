# Mfportal

This is the portal for Manufacture 

## Setup

```bash
git clone https://github.com/username/mfportal.git
cd mfportal
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py createsuperuser
python3 manage.py runserver

##Sqlite connection
sqlite3 db.sqlite3
.tables