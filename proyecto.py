import feedparser

# Palabras para buscar dentro de la etiqueta <title>
filtro = ['Betis','vs','madrid']

# Comprueba que los enlaces no estan en nuestro fichero (hay que crearlo antes de ejecutar el script).
f = open('fichero_datos.txt', 'r')
urls = f.readlines()
urls = [url.rstrip() for url in urls] # Elimina el '\n'
f.close()

def contains_wanted(in_str):
    # Devuelve verdadero si la palabra esta en nuestra lista "filtro"
    for wrd in filtro:
        if wrd.lower() in in_str:
            return True
    return False

def url_is_new(urlstr):
    # Devuelve verdadero si el enlace no existe previamente en nuestro archivo
    if urlstr in urls:
        return False
    else:
        return True

rss = 'https://e00-marca.uecdn.es/rss/futbol/sevilla.xml'
feed = feedparser.parse(rss)
for key in feed["entries"]: 
    url = key['links'][0]['href']
    title = key['title']
    content = key['content']

    if contains_wanted(title.lower()) and url_is_new(url):
        print('{} - {}'.format(title, url))

        msgtitle = title
        msg = '{}\n{}'.format(title, url)

        with open('fichero_datos.txt', 'a') as f:
            f.write('{}\n'.format( title + "\n" + url + "\n"))
            
