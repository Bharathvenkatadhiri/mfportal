# Mfportal

This is the portal for Manufacture 

## Setup

```bash
git clone https://github.com/username/mfportal.git
cd mfportal
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver