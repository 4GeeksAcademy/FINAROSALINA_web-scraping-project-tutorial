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
    
    tables = soup.find_all('table')
    table = tables[0] 
    
    rows = table.find_all('tr')
    table_data = []
    
    # Iterar sobre las filas de la tabla 
    for row in rows[:]:  
        # Obtener las celdas de la fila (<td>)
        cells = row.find_all('td')

        if len(cells) > 0:
            row_data = [cell.text.strip() for cell in cells]  # Extraer el texto de cada celda
            table_data.append(row_data) 
       
    for data in table_data:
        print(data)
else:
    print(f"Error en la solicitud: {response.status_code}")

 
ds=pd.DataFrame(table_data)

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
        df_beneficios = pd.DataFrame(beneficios, columns=["Año", "Beneficio", "Evolución"])
       
            # Mostrar el DataFrame de beneficios
            print("\nDataset de beneficios:")
            print(df_beneficios.head())
else:
    print(f"Error en la solicitud: {response.status_code}")


ultimo_año = df_beneficios.iloc[0] 

print(f"Los beneficios del último año ({ultimo_año['Año']}) fueron: {ultimo_año['Beneficio']}")

# guardar en csv
df.to_csv('company_revenue_dataset.csv', index=False)