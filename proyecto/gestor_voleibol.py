import pandas as pd

# 1. Creamos la lista de jugadoras
jugadoras = ["Lucía Pérez", "Sofía Gómez", "Valentina Torres", "Camila Ruiz"]

# 2. Creamos la tabla con los datos
df = pd.DataFrame({
    "Jugadora": jugadoras,
    "Asistencia": ["Pendiente", "Pendiente", "Pendiente", "Pendiente"]
})

# 3. Guardamos la tabla en un archivo de Excel
df.to_excel("asistencia_voleibol.xlsx", index=False)

print("¡Lista de asistencia creada con éxito!")