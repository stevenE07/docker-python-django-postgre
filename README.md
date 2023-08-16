Descarguen docker hub
ejectuar:

docker build -t django .

docker compose up

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


## ANGULAR ##
para el caso de angular no parece factible realizar un contenedor, ya lo intenté pero termina siendo mucho mas lento usar
angular cli dentro de un contenedor que intalarse la propia herramienta de desarrollo, ademas angular ya cuenta con 
control de versiones asi que no sería de mucho problema en este caso.
Lo que si hay que controlar es que tengamos la misma versión de node instalada, ya que angular cli requiere de dicha instalacion.

Una vez instalado node:

-npm install -g @angular/cli  -> instala angular cli
-ir a la carpeta del proyecto correspondiente a angular
-ejecutar npm install 
-ng serve -> levanta el servidor local, se accede por localhost:4200
