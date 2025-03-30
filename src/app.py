import os
from bs4 import BeautifulSoup
import requests
import time
import sqlite3
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

resource_url = "https://companies-market-cap-copy.vercel.app/index.html"

# Petición para descargar el fichero de Internet
response = requests.get(resource_url)

# Verificar si la respuesta fue exitosa (código 200)
if response.status_code == 200:
    print("¡Petición exitosa! Código:", response.status_code)
    # Se almacena el archivo en el directorio actual para usarlo más tarde
    with open("adult.csv", "wb") as dataset:
        dataset.write(response.content)
else:
    print("Error al descargar el archivo. Código de estado:", response.status_code)



# URL del recurso
resource_url = "https://companies-market-cap-copy.vercel.app/index.html"

# Pausa de 10 segundos antes de hacer la solicitud (esto es opcional)
time.sleep(3)

# Hacer la petición para descargar el archivo
response = requests.get(resource_url)

# Si la petición se ha ejecutado correctamente
if response.status_code == 200:
    print("¡Petición exitosa! Código:", response.status_code)
    
    # Parsear el HTML
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Buscar todas las tablas en la página
    tables = soup.find_all('table')
    
    # Seleccionamos la tabla que deseas, en este caso la primera tabla
    table = tables[0]  # Si deseas una tabla diferente, cambia el índice, ej. tables[1] para la segunda
    
    # Obtener todas las filas de la tabla (<tr>)
    rows = table.find_all('tr')
    
    # Crear una lista para almacenar los datos extraídos
    table_data = []
    
    # Iterar sobre las filas de la tabla 
    for row in rows[:]:  
        # Obtener las celdas de la fila (<td>)
        cells = row.find_all('td')

        if len(cells) > 0:
            row_data = [cell.text.strip() for cell in cells]  # Extraer el texto de cada celda
            table_data.append(row_data) 
       
    # Mostrar los datos extraídos
    for data in table_data:
        print(data)
else:
    print(f"Error en la solicitud: {response.status_code}")

 
ds=pd.DataFrame(table_data)
ds


# limpia las filas para obtener los valores limpios eliminando $ y B. Elimina también vacías o no tengan información.
ds.head()
# Renombrar las columnas
ds.columns = ['Year', 'Revenue', 'change']  
# cambiatr a tipo string pq el metodo str no me deja acceder si no es str
ds['Revenue'] = ds['Revenue'].astype(str)

ds["Revenue"] = ds["Revenue"].str.replace('$', '').str.replace(' B', '').astype(float)
ds



import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL del recurso
url = "https://companies-market-cap-copy.vercel.app/earnings.html"

response = requests.get(url)
if response.status_code == 200:
    print("Petición exitosa, código:", response.status_code)

    # Crear el objeto BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")

    table = soup.find_all("table")  # Encuentra todas las tablas
    if table: 
        table = table[0]  # primera tabla
        rows = table.find_all("tr")

        beneficios = []

        for row in rows:
            cells = row.find_all('td')
            if len(cells) > 0: 
                row_data = [cell.text.strip() for cell in cells] 
                beneficios.append(row_data)  

        # Crear un DataFrame con los datos extraídos
        df = pd.DataFrame(beneficios, columns=["Año", "Beneficio", "Evolución"])
        
else:
    print(f"Error en la solicitud: {response.status_code}")

print(df.head())

ultimo_año = df.iloc[0] 
print(f"Los beneficios del último año ({ultimo_año['Año']}) fueron: {ultimo_año['Beneficio']}")
  


import json

# Ruta del archivo fuente (explore.es.ipynb)
origen = '/workspaces/FINAROSALINA_web-scraping-project-tutorial/src/explore.es.ipynb'

# Ruta de destino (app.py)
destino = '/workspaces/FINAROSALINA_web-scraping-project-tutorial/src/app.py'

# Abrir el archivo .ipynb y cargar su contenido como JSON
with open(origen, 'r') as file:
    contenido = json.load(file)

# Extraer solo las celdas de tipo 'code' del cuaderno
celdas_de_codigo = [cell['source'] for cell in contenido['cells'] if cell['cell_type'] == 'code']

# Unir todo el código en un solo bloque
codigo_completo = "\n\n".join(["".join(celda) for celda in celdas_de_codigo])

# Abrir el archivo app.py y escribir el código extraído
with open(destino, 'w') as file:
    file.write(codigo_completo)

print(f"Código copiado de {origen} a {destino}")
