Descarguen docker hub
ejectuar:

Iniciar docker en wsl2:
    sudo service docker start

docker build -t django .

docker-compose up

Si la base de datos da error:
- docker-compose exec web python manage.py makemigrations
- docker-compose exec web python manage.py migrate

Las carpetas que quedaron fueron generadas por este tutorial de django
https://docs.djangoproject.com/en/4.2/intro/tutorial01/#creating-a-project

ya deberian de poder acceder a la ruta:
localhost:8000/pulls (web creada)
localhost:5050/browser/ (pgAdmin con la base ya asociada)

### COMO GUARDAR LA BASE DE DATOS ###
docker-compose exec db pg_dump -h db -U postgres postgres > backupDB.sql
