import pymysql
import pandas as pd
from datetime import datetime

print("--- STARTING DATA PIPELINE ---")


# PHASE 1: EXTRACT (Extracción de Datos)

try:
    print("[INFO] Connecting to MySQL database...")
    
    # 1. Establecemos la conexión real con tu servidor local
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='251215', 
        database='practice_db'
    )
    
    # 2. Definimos la consulta SQL para traer los datos crudos
    query = "SELECT * FROM ventas_hvac;"
    
    print("[INFO] Executing SQL query...")
    # 3. Pandas ejecuta la consulta y guarda el resultado en memoria (DataFrame)
    df_crudo = pd.read_sql(query, connection)
    
    # 4. Cerramos la conexión (Siempre cerrar la conexion para no saturar el servidor)
    connection.close()
    
    print(f"[SUCCESS] Extract Phase: {len(df_crudo)} rows successfully extracted.")

except Exception as e:
    # Si pusiste mal la contraseña o la tabla no existe, este bloque salvará el programa
    print(f"[ERROR] Extract Phase Failed: {e}")
    exit()


# PHASE 2: TRANSFORM (Transformación)

print("\n[INFO] Starting Transform Phase...")

# Tomamos df_crudo y le quitamos las ventas canceladas

df_filtrado = df_crudo[df_crudo['estatus_pago'] != 'cancelled'].copy()
print(f"[SUCCESS] Filtered out cancelled orders. Rows remaining: {len(df_filtrado)}")

# Calculamos una nueva columna métrica (Precio x Cantidad)
df_filtrado['total_venta_usd'] = df_filtrado['precio_usd'] * df_filtrado['cantidad']

# Estandarizamos el texto a mayúsculas
df_filtrado['estatus_pago'] = df_filtrado['estatus_pago'].str.upper()

print("[SUCCESS] Transform Phase: Data cleaned and financial metrics calculated.")




# PHASE 3: LOAD (Carga o Almacenamiento Final)

print("\n[INFO] Starting Load Phase...")

# 1. Creamos un nombre de archivo dinámico usando la fecha actual
# Esto evita que el reporte de hoy borre o sobreescriba el reporte de ayer

fecha_hoy = datetime.now().strftime("%Y-%m-%d")
nombre_archivo = f"clean_sales_report_{fecha_hoy}.xlsx"

# 2. Usamos Pandas para guardar el DataFrame filtrado en un archivo CSV limpio
# index=False evita que se agregue una columna extra de números innecesarios

df_filtrado.to_excel(nombre_archivo, index=False)

print(f"[SUCCESS] Load Phase: High-value data successfully saved to '{nombre_archivo}'.")
print("\n--- PIPELINE EXECUTION COMPLETED SUCCESSFULLY ---")

