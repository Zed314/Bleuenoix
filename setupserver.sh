#Installation script for the project

virtualenv --no-site-packages --distribute env && source env/bin/activate && pip3 install -r requirements.txt
python3 manage.py makemigrations && python3 manage.py makemigrations bleuenoix && python3 manage.py migrate 
python3 manage.py shell < addCategory.py

