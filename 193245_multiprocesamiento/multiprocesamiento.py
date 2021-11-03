from imgurpython import ImgurClient
from concurrent.futures import ThreadPoolExecutor
import urllib.request
import timeit
import multiprocessing  
 
secreto_cliente = "5f8c3cce299db5e26a2eb96b0b7809a82805c9ad"
id_cliente = "bfa0e227a1c5643"
 
cliente = ImgurClient(id_cliente, secreto_cliente)
 
# Metodo para la descarga url imagen
# Datos necesarios del metodo
# Nombre de la imagen => yntdWAr
# Formato de la imagen => png
 
listaImagen = []

def descarga_url_img(link):
   print(link)
   # Con esto ya podemos obtener el corte de la url imagen
   nombre_img = link.split("/")[3]
   formato_img = nombre_img.split(".")[1]
   nombre_img = nombre_img.split(".")[0]
   print(nombre_img, formato_img)
   url_local = "/Users/1097499132/OneDrive/Documents/cuatrimestre/193245_Imagenes/193245_multiprocesamiento/{}.{}"
   #Guardar nne local las imagenes
   urllib.request.urlretrieve(link, url_local.format(nombre_img, formato_img))
 
 
def main():
   id_album = "bUaCfoz"
   imagenes = cliente.get_album_images(id_album)
 
   for imagen in imagenes:
      descarga_url_img(imagen.link)
      listaImagen.append(imagen.link)

def multiprocesamiento():
   pool = multiprocessing.Pool(10)    
   pool.map(descarga_url_img, listaImagen)   



if __name__ == "__main__":
   print("Tiempo de descarga {}".format(timeit.Timer(main).timeit(number=1)), "\n")
   print("Tiempo de descarga {}".format(timeit.Timer(multiprocesamiento).timeit(number=1)))
