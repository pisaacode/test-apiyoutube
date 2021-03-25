# Backend API-YOUTUBE
Test api youtube endpoind, el cual se le pasa un parametro en la url y devuelve un listado de videos de youtube
````
http://app-youtubetest.herokuapp.com/lista?search=busqueda
````

### Pre - Requisitos para desarrollar:
* Tener la api key de youtube
### Start/Running
Instalar las dependencias con 
````
pipenv install
`````
Crear el archivo .env haciendo una copia del .env_src
````
cp .env_src .env
`````
Para arrancar el proyecto ejecutar
````
python app.py
`````
Para ejecutar los test ejecutar el siguiente comando
````
python -m pytest
`````
