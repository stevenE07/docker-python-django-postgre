# Usa una imagen base de Python
FROM python:3.11

# Directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el contenido de tu proyecto al contenedor
COPY . /app/

# Instala las dependencias de Python
RUN pip install -r requirements.txt

# Expone el puerto en el que se ejecutará tu aplicación Django
EXPOSE 8000

# Comando para ejecutar el servidor de desarrollo de Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
