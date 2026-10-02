import requests
import pandas as pd
from datetime import datetime

print("--- STARTING API INTEGRATION PIPELINE ---")


# PHASE 1: EXTRACT (Obtener datos de una API)

try:
    print("[INFO] Fetching real-time exchange rates from public API...")
    
    # Esta es otra alternativa excelente y súper estable de API pública
    url = "https://api.frankfurter.dev/v2/rates"
    
    # Añadimos un "User-Agent" para que el servidor sepa que es una petición segura
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }
    
    # Pasamos el link y los encabezados de seguridad
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data_json = response.json() 
        print("[SUCCESS] API Data successfully retrieved.")
    else:
        print(f"[ERROR] API returned an error status: {response.status_code}")
        exit()

except Exception as e:
    print(f"[ERROR] Extract Phase Failed: {e}")
    exit()



# PHASE 2: TRANSFORM (Filtrar y dar formato)

print("\n[INFO] Starting Transform Phase...")

# Como la API nos devolvió una lista, extraemos el primer elemento [0]
datos_interiores = data_json if isinstance(data_json, dict) else data_json[0]

todas_las_tasas = datos_interiores.get("rates", {})
fecha_actualizacion = datos_interiores.get("date", "")

# Filtramos las monedas que nos interesan
datos_limpios = {
    "Base_Currency": "USD",
    "MXN_Mexico": todas_las_tasas.get("MXN"),
    "API_Last_Updated": fecha_actualizacion,
    "Extraction_Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
}

# Convertimos nuestro diccionario limpio en una fila de Pandas DataFrame
df_api = pd.DataFrame([datos_limpios])
print("[SUCCESS] Transform Phase: JSON parsed into structured DataFrame.")



# PHASE 3: LOAD --Guardar en un Excel--

print("\n[INFO] Starting Load Phase...")

# Generamos el nombre del archivo final
nombre_archivo = "live_exchange_rates.xlsx"

# Guardamos el resultado en Excel
df_api.to_excel(nombre_archivo, index=False)

print(f"[SUCCESS] Load Phase: High-value currency data saved to '{nombre_archivo}'.")
print("--- PIPELINE COMPLETED SUCCESSFULLY ---")
