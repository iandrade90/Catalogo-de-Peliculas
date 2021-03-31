import os

class CatalogoPeliculas():

    ruta_archivo = 'peliculas.txt'

    @staticmethod
    def agregar_pelicula(pelicula):
        try:
            archivo = open(CatalogoPeliculas.ruta_archivo, 'a')
            archivo.write(pelicula.__str__())
            archivo.write('\n')
        except Exception as identifier:
            print('Error:', identifier)
        finally:
            archivo.close()

    @staticmethod
    def lista_peliculas():
        try:
            archivo = open(CatalogoPeliculas.ruta_archivo, 'r')
            print('Catalogo de Peliculas: ')
            print(archivo.read())
        except Exception as identifier:
            print('Error:', identifier)
        finally:
            archivo.close()

    @staticmethod
    def eliminar():
        try:
            os.remove(CatalogoPeliculas.ruta_archivo)
            print('Archivo eliminado: ', CatalogoPeliculas.ruta_archivo)
        except Exception as identifier:
            print('Error:', identifier)
