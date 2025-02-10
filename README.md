📂 Organizador Automático de Archivos
Este script en Python clasifica archivos dentro de una carpeta según su contenido y extensión. 
Analiza documentos PDF y Word en busca de palabras clave para organizarlos en categorías específicas.

🚀 Características
✔️ Clasificación automática de archivos PDF y Word según su contenido.
✔️ Organización por tipo de archivo, moviendo imágenes, videos, audios y programas a carpetas correspondientes.
✔️ Personalizable: Se pueden añadir nuevas categorías y palabras clave fácilmente.

🛠️ Tecnologías utilizadas
Python
pdfplumber (para extraer texto de PDFs)
python-docx (para leer documentos Word)
os y shutil (para gestionar archivos y carpetas)

📌 Cómo usarlo
1. Instalar dependencias:
pip install pdfplumber python-docx
2. Ejecutar el script:
python organizador.py

Ingresar la ruta de la carpeta con los archivos a organizar.

📁 Organización de archivos

El script creará carpetas y moverá los archivos según estas categorías predeterminadas:
Ecuaciones Diferenciales
Programación
Fundamentos de TI
Interacción Hombre Computador
Auto
Estadística para Ingenieros
Programas
Audio
Videos
Pics
OTROS (para archivos sin coincidencias)

🛠️ Personalización
Puedes agregar nuevas categorías editando el diccionario en el código:
diccionario = {
    "Nueva Categoría": ["palabra clave 1", "palabra clave 2"]
}
