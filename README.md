```shell
# Create virtual environment
python -m venv .venv

# Activate virtual environment
source .venv/bin/activate

# Install dependencies
python -m pip install -r requirements.txt

# Run server to check that install worked
python manage.py runserver

# Navigate to http://localhost:8000/ and check for landing page
curl http://localhost:8000/
```
