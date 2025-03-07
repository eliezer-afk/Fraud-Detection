import os
import shutil
import pandas as pd

def create_data_folders(base_path="data"):
    """Crea la estructura de carpetas necesarias."""
    subfolders = ["raw", "processed", "features"]
    for folder in subfolders:
        os.makedirs(os.path.join(base_path, folder), exist_ok=True)
    print("📂 Estructura de carpetas creada.")

def move_file(source, destination):
    """Mueve un archivo a la carpeta correspondiente."""
    if os.path.exists(source):
        shutil.move(source, destination)
        print(f"✅ Archivo movido a {destination}")
    else:
        print(f"⚠️ Archivo {source} no encontrado.")

def generate_sample_data():
    """Genera un archivo de prueba en data/raw."""
    sample_data = {
        "transaction_id": [1, 2, 3, 4, 5],
        "amount": [100.5, 200.0, 50.75, None, 300.25],
        "is_fraud": [0, 1, 0, 1, 0]
    }
    df = pd.DataFrame(sample_data)
    raw_path = "data/raw/transactions.csv"
    df.to_csv(raw_path, index=False)
    print(f"📝 Archivo de prueba generado: {raw_path}")

def preprocess_data():
    """Lee los datos, limpia valores nulos y los guarda en processed."""
    raw_path = "data/raw/transactions.csv"
    processed_path = "data/processed/transactions_clean.csv"
    
    if not os.path.exists(raw_path):
        print("⚠️ No se encontró transactions.csv en raw/")
        return
    
    df = pd.read_csv(raw_path)
    print("📊 Datos originales:")
    print(df.head())
    
    # Limpiar valores nulos (rellenar con 0 en este caso)
    df.fillna(0, inplace=True)
    
    # Guardar datos procesados
    df.to_csv(processed_path, index=False)
    print(f"✅ Datos procesados guardados en {processed_path}")

if __name__ == "__main__":
    create_data_folders()
    generate_sample_data()
    preprocess_data()
