# Usa una imagen de Node.js como base
FROM node:14

# Instala Angular CLI de manera global
RUN npm install -g @angular/cli

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia el archivo package.json e instalador de dependencias
COPY package*.json ./
RUN npm install

# Copia el resto de la aplicación
COPY . .

# Expone el puerto 4200 (puerto predeterminado de Angular CLI)
EXPOSE 4200

# Comando para iniciar el servidor de desarrollo de Angular
CMD ["ng", "serve", "--host", "0.0.0.0"]
