# Classifier
Procesador y Clasificador de sentimientos ejemplificado con Tweeter  

## Requirements

<img src="https://svn.apache.org/repos/asf/couchdb/supplement/logo/couchdb-icon-64px.png" height=50/><img src="http://devblog.info/wp-content/uploads/2017/01/python_icon.png" height=50/> 

## Minar Datos
Agregar las claves de la API de tweeter al script harvest.py despues:
```
$  python harvest.py
```  

## Configuracion
linea 123 URL = 'RemoteHost' ##Direccion del servidor de la base de datos## 

linea 124 db_name = 'tweet' ##Nombre de la base de datos donde estan los tweets minados##

linea 125 db1_name = 'cleantweet' ##Nombre de la base de datos donde estan los tweets limpios##

## Como levantar la aplicación
```
$ python Classifier.py 
```
