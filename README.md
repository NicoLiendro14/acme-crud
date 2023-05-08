# Proyecto de Django

Esta es una prueba tecnica en Django que utiliza GIS. Sigue los pasos a continuación para clonar el proyecto, cargar las variables de entorno y ejecutar el servidor de desarrollo.

## Clonar el proyecto

1. Abre una terminal.

2. Clona el proyecto desde el repositorio:

   ```shell
   git clone https://github.com/NicoLiendro14/acme-crud

3. Cambia al directorio del proyecto:
   ```shell
   cd <DIRECTORIO_DEL_PROYECTO>

## Configurar las variables de entorno
1. Crea un archivo .env en el directorio raíz del proyecto.

2. Abre el archivo .env y define las variables de entorno necesarias para tu configuración. Por ejemplo:

```plaintext

DATABASE_NAME=nombre_basedatos
DATABASE_USER=nombre_usuario
DATABASE_PASSWORD=contraseña
HOST=localhost
PORT=5432
GDAL_LIBRARY_PATH=/ruta/gdal_library.dll
GEOS_LIBRARY_PATH=/ruta/geos_library.dll
```

3. Guarda el archivo .env.

## Instalar dependencias

1. Asegúrate de tener Python y pip instalados en tu sistema.

2. En la terminal, ejecuta el siguiente comando para instalar las dependencias del proyecto:

```shell

    pip install -r requirements.txt
```

## Ejecutar el servidor de desarrollo

1. En la terminal, ejecuta el siguiente comando para aplicar las migraciones de la base de datos:

```shell
    python manage.py migrate
```

2. Finalmente, inicia el servidor de desarrollo:

```shell
    python manage.py runserver
```
    
3. Abre un navegador web y ve a http://localhost:8000 para acceder a la aplicación.

¡Listo! Ahora deberías tener el proyecto de Django clonado, las variables de entorno cargadas y el servidor de desarrollo en funcionamiento.
