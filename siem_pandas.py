import pandas as pd

# Leer el archivo de logs (asegurase de que logs.csv esté en la misma carpeta que este script)
df = pd.read_csv("logs.csv")

# Mostrar primeras filas
print("=== Primeros eventos ===")
print(df.head())

# Filtrar intentos fallidos
fallidos = df[df["evento"] == "login_fail"]

# Contar intentos fallidos por usuario
conteo = fallidos["usuario"].value_counts()
print("\n=== Intentos fallidos por usuario ===")
print(conteo)

# Generar alertas si superan el umbral
UMBRAL = 3
print("\n=== ALERTAS ===")
for usuario, cantidad in conteo.items():
    if cantidad > UMBRAL:
        print(f"⚠️ ALERTA: Usuario {usuario} con {cantidad} intentos fallidos")

# Reporte final
print("\n=== REPORTE FINAL ===")
print(f"Total de eventos: {len(df)}")
print(f"Total de intentos fallidos: {len(fallidos)}")
print("Usuarios con más fallos:")
print(conteo.head())
