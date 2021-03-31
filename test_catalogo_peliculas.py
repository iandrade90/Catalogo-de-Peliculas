from dominio.pelicula import Pelicula
from servicio.catalogo import CatalogoPeliculas

def main():

    opcion = None
    salir = 4

    while opcion != salir:
        print('---------------------------------------')
        print('Menu de opciones')
        print('---------------------------------------')
        print('1) Agregar pelicula')
        print('2) Lista de peliculas agregadas')
        print('3) Eliminar archivos con el catalogo')
        print('4) Salir')
        print('---------------------------------------')
        print('---------------------------------------')
        opcion = input('Indique su opcion: ')
        print('---------------------------------------')
        print()
        
        if opcion == '1':
            pelicula = Pelicula(input('Indique el nombre de la pelicula: '))
            CatalogoPeliculas.agregar_pelicula(pelicula)
        elif opcion == '2':
            CatalogoPeliculas.lista_peliculas()
        elif opcion == '3':
            CatalogoPeliculas.eliminar()
        else:
            print('Muchas gracias...!')
            break


main()
