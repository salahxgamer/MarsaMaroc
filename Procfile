web: gunicorn ResourceManager.wsgi --log-file -


release: python manage.py && python manage.py loaddata admin_interface_theme_marsamaroc_red.json && python manage.py loaddata manager_resource_sample_data.json