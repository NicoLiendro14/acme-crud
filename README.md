# Proyecto de Django

Esta es una prueba tecnica en Django que utiliza GIS. Sigue los pasos a continuación para clonar el proyecto, cargar las variables de entorno y ejecutar el servidor de desarrollo.

## Clonar el proyecto

1. Abre una terminal.

2. Clona el proyecto desde el repositorio:

   ```shell
   git clone https://github.com/NicoLiendro14/acme-crud

3. Cambia al directorio del proyecto:
   ```shell
   cd acme-crud
# Instalación de OSGeo4W, Postgres y PostGIS

Este repositorio utiliza tecnologías de información geoespacial (GIS) y requiere la instalación de OSGeo4W, Postgres y PostGIS. Sigue los pasos a continuación para configurar tu entorno de desarrollo.

## Instalación de OSGeo4W

1. Descarga el instalador de OSGeo4W desde el siguiente enlace: [https://trac.osgeo.org/osgeo4w/](https://trac.osgeo.org/osgeo4w/).

2. Ejecuta el instalador descargado y sigue las instrucciones del asistente de instalación.

3. Durante la instalación, selecciona los paquetes necesarios para tu proyecto GIS. 

4. Una vez completada la instalación, OSGeo4W estará listo para su uso.

## Instalación de Postgres y PostGIS

1. Para instalar Postgres, sigue las instrucciones de instalación correspondientes a tu sistema operativo desde el sitio web oficial de Postgres: [https://www.postgresql.org/download/](https://www.postgresql.org/download/).

2. Después de instalar Postgres, puedes proceder a la instalación de PostGIS siguiendo los pasos que se detallan en el siguiente enlace: [https://postgis.net/workshops/postgis-intro/installation.html](https://postgis.net/workshops/postgis-intro/installation.html).

3. Sigue las instrucciones proporcionadas en el enlace de instalación de PostGIS para tu sistema operativo específico.

4. Una vez completada la instalación de PostGIS, tendrás todo lo necesario para ejecutar y desarrollar aplicaciones GIS utilizando este repositorio.




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

## Convenciones para los Endpoints

Se han respetado las reglas para nombrar y asignar los verbos HTTP correspondientes a cada endpoint. A continuación, se muestra un ejemplo:

- Endpoint para crear un usuario: `POST /usuario`
- Endpoint para crear un plan: `POST /plan`
- Etc...

## Documentación de los Endpoints

Cada vista (endpoint) cuenta con un docstring detallado que explica su funcionamiento. Los docstrings incluyen información sobre los parámetros, el comportamiento esperado y la estructura de las respuestas. A continuación, se muestra un ejemplo:

```python
@api_view(["GET"])
def obtener_planes_disponibles(request):
    """
    Vista para el endpoint de obtener planes disponibles.

    Permite a los usuarios obtener una lista de planes disponibles basados en la ubicación.

    Parámetros:
    - request: La solicitud HTTP recibida.

    Retorna:
    - Una respuesta HTTP con la lista de planes disponibles.
    """
    # Código de la vista
```

## Pruebas de la API con Postman

Se incluye una colección de Postman en formato JSON que contiene una serie de solicitudes predefinidas para probar la API. La colección se encuentra en el archivo collection.json en la raíz del proyecto.

Puedes importar esta colección en Postman y utilizar las solicitudes predefinidas para realizar pruebas en la API. Asegúrate de actualizar las URL y los datos según tu entorno de desarrollo.


## Iniciar sesión y obtener el token

Para acceder a los endpoints protegidos, primero debes iniciar sesión y obtener un token de acceso. 
Endpoint de inicio de sesión:

```
POST /login/
```
Enviar una solicitud POST a este endpoint con las credenciales de usuario (nombre de usuario y contraseña) en el cuerpo de la solicitud. Si las credenciales son válidas, la respuesta contendrá un token de acceso.

## Usar el token de acceso

Una vez que tienes el token de acceso, debes incluirlo en los encabezados de tus solicitudes para acceder a los endpoints protegidos.

Ejemplo de encabezado:
```
Authorization: Token {token}
```

Reemplaza `{token}` por el valor real de tu token de acceso.

## Obtener todos los planes

Un ejemplo de endpoint protegido es el que permite obtener todos los planes.

Endpoint para obtener todos los planes:
```
GET  /planes?latitud=10.1234&longitud=20.5678
```
Para acceder a este endpoint, debes incluir el token de acceso en el encabezado de la solicitud como se mencionó anteriormente. Si el token es válido, recibirás la respuesta con todos los planes disponibles.

Recuerda que debes incluir el token en cada solicitud a los endpoints protegidos para acceder a ellos correctamente.
