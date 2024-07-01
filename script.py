#!/usr/bin/env python3

import os
import sys
import re

def main():
    # Lista de información adicional a agregar al inicio de cada archivo
    info_lines = [
        "<!-- Autor: Daniel Benjamin Perez Morales -->",
        "<!-- GitHub: https://github.com/DanielPerezMoralesDev13 -->",
        "<!-- Correo electrónico: danielperezdev@proton.me -->"
    ]
    
    # Obtener la lista de archivos en el directorio actual, excepto el propio script
    files = os.listdir(".")
    # files.remove(sys.argv[0])  # Remove the script itself from the list
    
    files.remove("script.py")
    
    # Iterar sobre cada archivo encontrado
    for filename in files:
        # Construir el nuevo nombre del archivo con extensión .md y título capitalizado
        new_filename = f"{filename[:-3].title()}.md"

        # # Agregar información adicional al inicio del archivo
        # for line in info_lines:
        #     os.system(f'echo "{line}" >> "{filename}"')

        # Intentar renombrar el archivo
        try:
            os.rename(filename, new_filename)
        except FileNotFoundError:
            print(f"Error: El archivo '{filename}' no existe.")
        except FileExistsError:
            print(f"Error: Ya existe un archivo con el nombre '{new_filename}'.")
        except Exception as e:
            print(f"Error al renombrar '{filename}' a '{new_filename}': {str(e)}")

def second():

    # Ruta al directorio que contiene los archivos
    directorio = '.'

    # Obtener la lista de archivos ordenados
    archivos = sorted(os.listdir(directorio))

    # Expresión regular para encontrar el número al inicio del nombre del archivo
    numero_regex = re.compile(r'^(\d+)')

    # Iterar sobre los archivos
    for i, archivo in enumerate(archivos):
        # Encontrar el número al inicio del nombre del archivo
        match = numero_regex.match(archivo)
        if match:
            numero_actual = int(match.group(1))
            
            # Solo modificar archivos con números a partir de 15
            if numero_actual >= 1:
                # Calcular el nuevo número según la lógica especificada (incrementar en 1)
                nuevo_numero = numero_actual + 1
                
                # Crear el nuevo nombre de archivo
                nuevo_nombre = f"{nuevo_numero:02d} {archivo.split(maxsplit=1)[1]}"
                
                # Renombrar el archivo
                os.rename(os.path.join(directorio, archivo), os.path.join(directorio, nuevo_nombre))
                print(f"Renombrado: {archivo} -> {nuevo_nombre}")
            else:
                print(f"No se modificó el archivo: {archivo}")
        else:
            print(f"No se pudo encontrar un número al inicio en el archivo: {archivo}")

    print("Renombrado completado.")


if __name__ == "__main__":
    # main()
    second()