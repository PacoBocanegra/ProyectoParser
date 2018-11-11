# ProyectoParser

Este script esta realizado integramente en Python 3. Para ello he utilizado el modulo de feedparser, asegurate de tenerlo instalado si quieres que te funcione todo perfectamente:

# Requisitos

• pip3 install feedparser

# Objetivo del script

Este script tiene como objetivo principal dos cosas:

• Obtener la información contenida dentro de las etiquetas <title> & Filtrar dicha información, para recopilar únicamente la que nosotros necesitamos
  
• Además, si lo ejecutamos varias veces, únicamente recopilará la información nueva. Es decir, solo recogerá noticias o información nueva. 

# Como ejecutar el script

• Pasos a realizar: 
  › touch fichero_datos.txt
  
  › python3 proyecto.py
  
  › cat fichero_datos.txt

# Como modificar los enlaces o el nombre del archivo

• Enlaces: linea 26
  › rss = 'https://e00-marca.uecdn.es/rss/futbol/sevilla.xml'

• Nombre Archivo: linea 7 && 39
  › f = open('fichero_datos.txt', 'r')
  
  › with open('fichero_datos.txt', 'a') as f:


Si hay algun error notificarlo por favor, un saludo.
