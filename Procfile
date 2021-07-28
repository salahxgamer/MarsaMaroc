web: gunicorn ResourceManager.wsgi --log-file -


release: python manage.py migrate&& python manage.py loaddata initial_data.json && python manage.py loaddata manager_resource_sample_data.json