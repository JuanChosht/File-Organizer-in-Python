import os
import shutil
import pdfplumber
from docx import Document

diccionario = {
    "Ecuaciones Diferenciales": ["Ecuaciones Diferenciales"],
    "Programacion": ["Programación"],
    "Fundamentos de TI": ["Fundamentos de TI", "CISCO"],
    "Interacción Hombre Computador": ["Interacción Hombre Computador"],
    "Auto": ["PBV", "Municipio de Quito"],
    "Estadistica Ing": ["Estadística para Ingenieros"],
    "Programas": [".zip", ".exe"],
    "Audio": [".mp3", ".wav", ".aac", ".flac", ".ogg"],
    "Videos": [".mp4", ".avi", ".mkv", ".mov", ".wmv"],
    "Pics": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"]
    #agregar mas
}

def ruta():
    ruta = input("Ingrese la ruta de la carpeta: ").strip()
    rutaexe = ruta.replace("\\", "/").replace('"', '') 
    return rutaexe

def iterar(carpeta):  # Iterar sobre los archivos PDF
    filesPdf = []
    filesWord = []
    for file in os.listdir(carpeta):
        filePath = os.path.join(carpeta, file)
        if file.startswith("~$") or file.startswith("."):
            continue

        if file.endswith(".pdf"):  
            filesPdf.append(filePath)
        elif file.endswith(".docx"):
            filesWord.append(filePath)
        #programas, audios, videos
        elif file.endswith(tuple(diccionario["Programas"])):
            carpetas(carpeta, "Programas", filePath)
        elif file.endswith(tuple(diccionario["Audio"])):
            carpetas(carpeta, "Audio", filePath)
        elif file.endswith(tuple(diccionario["Videos"])):
            carpetas(carpeta, "Videos", filePath)
        elif file.endswith(tuple(diccionario["Pics"])):
            carpetas(carpeta, "Pics", filePath)

    return filesPdf, filesWord

def carpetas(ruta, key, file):
    rutaCarpeta = os.path.join(ruta, key.upper())
    if not os.path.exists(rutaCarpeta):
        os.makedirs(rutaCarpeta)
    shutil.move(file, os.path.join(rutaCarpeta, os.path.basename(file)))
    return rutaCarpeta

def buscarenPDF(file, ruta, diccionario):
    try:
        with pdfplumber.open(file) as pdf:
            for i in range(min(3, len(pdf.pages))):
                firstPage = pdf.pages[i]
                texto = firstPage.extract_text().splitlines()
                for linea in texto:  #chequeamos cada linea dentro del texto
                    for key, values in diccionario.items():
                        for value in values:
                            if value.lower() in linea.lower():
                                pdf.close()
                                carpetas(ruta, key, file) #USO DE FUNCION
                                return
    except Exception as e:
        print(f"Error al abrir el archivo: {file}")                     
    carpetas(ruta, "OTROS", file)

def buscarWord(file, ruta, diccionario):
    try:
        doc = Document(file)
        for texto in doc.paragraphs:
            for key, values in diccionario.items():
                for value in values:
                    if value.lower() in texto.text.lower():
                        carpetas(ruta, key, file) 
                        return
    except Exception as e:
        print(f"Error al abrir el archivo: {file}") 
    carpetas(ruta, "OTROS", file)
    
def ejecutar():
    directorio = ruta()
    archivosPdf, archivosWord = iterar(directorio) 
    for archivo in archivosPdf:
        buscarenPDF(archivo, directorio, diccionario)
    for archivo in archivosWord:
        buscarWord(archivo, directorio, diccionario)
    
       
ejecutar()
