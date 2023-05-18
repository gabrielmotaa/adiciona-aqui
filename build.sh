set -o errexit

pip install pip --upgrade
pip install -r requirements/prod.txt

python manage.py collectstatic --no-input
python manage.py migrate
python manage.py shell -c "from django.contrib.auth import get_user_model;User = get_user_model(); User.objects.filter(is_superuser=True).delete()"
python manage.py createsuperuser --noinput
python manage.py populate_categories
