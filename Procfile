web: gunicorn ResourceManager.wsgi --log-file -


release : python manage.py migrate
release : python manage.py loaddata admin_interface_theme_marsamaroc_red.json
release : python manage.py loaddata manager_resource_sample_data.json