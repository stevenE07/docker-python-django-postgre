# Use an appropriate base image for the frontend (e.g., Node.js with a specific version)
FROM node:16.20.0 

# Set the working directory for the frontend
WORKDIR /app

# Instalar Angular CLI globalmente
RUN npm install -g @angular/cli

# Copiar los archivos de la aplicación Angular y las dependencias
COPY package.json package-lock.json ./
RUN npm install

# Copiar el resto de los archivos
COPY . .

# Construir la aplicación Angular
RUN npm run build
