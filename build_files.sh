echo "BUILD Start"
python 3.8 -m pip install -r requirements.txt
python 3.8 manage.py collectstatic --noinput --clear
echo "BUILD End"
