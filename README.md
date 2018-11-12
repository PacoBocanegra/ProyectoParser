# ProyectoParser

Este script esta realizado integramente en Python 3. Para ello he utilizado el modulo de feedparser, asegurate de tenerlo instalado si quieres que te funcione todo perfectamente:

# Requisitos

• pip3 install feedparser

# Objetivo del script

Este script tiene como objetivo principal dos cosas:

   • Obtener la información contenida dentro de las etiquetas <title>, mediante una lista de palabras (Ej, si la lista contiene la palabra "sevilla", te recopilará todas las etiquetas que contengan en su interior la palabra "Sevilla").
  
   • Además, si lo ejecutamos varias veces, este script es capaz de detectar información nueva con respecto a la que ya había almacenada en el fichero_datos.txt. Por lo que solo recogerá noticias nuevas o que no estaban almacenadas ya en dicho fichero (es perfecto para recopilar información reciente)

# Como ejecutar el script

• Pasos a realizar: 

    touch fichero_datos.txt #(solo es necesario crearlo 1 vez, en posteriores ejecuciones lo usa como referencia para saber si hay novedades)
  
    python3 proyecto.py
    
    cat fichero_datos.txt

# Como modificar los enlaces o el nombre del archivo

• Enlaces: linea 26

    rss = 'https://e00-marca.uecdn.es/rss/futbol/sevilla.xml'

• Nombre Archivo: linea 7 && 39

    f = open('fichero_datos.txt', 'r')
  
    with open('fichero_datos.txt', 'a') as f:


Si hay algun error notificarlo por favor, un saludo.
