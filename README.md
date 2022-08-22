# **TALLER DEVOPS - TECNOLOGÍAS EMERGENTES**

###### *Pontificia Universidad Javeriana Cali*

## **Autor:** Kevin Steven Ocampo Morales :nerd_face:

## **Prerrequisitos:**
- Python3 y pip, ya que es el lenguaje de programación en el que se encuentra desarrollada la API.
- Instalar fastapi para que reconozca la API y poder ejecutarla.
- Instalar uvicorn para poder tener el servidor local en el que correrá la API.
- Instalar requests para realizar peticiones REST desde nuestra API al servidor y los datos de mockapi.

## **Como ejecutar la app:**
Primero se debe bajar el proyecto del repositorio GitHub. Una vez teniendo el proyecto en la maquina 
y cumpliendo con todos los prerrequisitos, podemos abrir una terminal en la carpeta del proyecto 
y ejecutar el siguiente comando para correr el servidor local:
- uvicorn main:app --reload 

## **Como probar la app:**
Una vez ejecutado el servidor local para poder probar las funciones REST de la API se aconseja el uso de 
[Swagger Inspector](https://inspector.swagger.io/builder?_ga=2.265769100.2058817415.1661038696-931631949.1661038696) para poder enviar los datos que se quieran, escoger el metodo que se quiere ejecutar y ver el resultado de cada end point. Las URL's para probar cada end point son las siguientes:
- http://localhost:8000/items **(Metodo GET sin id)**
- http://localhost:8000/items/{id} **(Metodo GET con id)**
- http://localhost:8000/items/{id} **(Metodo PUT)**
- http://localhost:8000/items/ **(Metodo POST)**
- http://localhost:8000/items/{id} **(Metodo DELETE)**



