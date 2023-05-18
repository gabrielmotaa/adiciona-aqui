set -o errexit

pip install requirements/prod.txt

python manage.py collectstatic --no-input
python manage.py migrate
python manage.py populate_categories
