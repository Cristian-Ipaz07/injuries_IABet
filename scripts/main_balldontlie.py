import requests
import json
import os
from datetime import datetime

def get_nba_injuries():
    """Obtiene lesiones de NBA usando balldontlie.io"""
    url = "https://www.balldontlie.io/api/v1/injuries" 

    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Verifica errores HTTP
        
        data = response.json()
        print_injury_summary(data['data'])  # 'data' contiene la lista de lesiones
        save_injury_data(data)
        
    except requests.exceptions.RequestException as e:
        print(f"❌ Error al conectar con la API: {e}")

def print_injury_summary(injuries):
    """Muestra resumen de lesiones"""
    print("\n📊 RESUMEN DE LESIONES NBA (Balldontlie.io)")
    print("=" * 50)
    
    if not injuries:
        print("No hay lesiones registradas hoy.")
        return
    
    for injury in injuries:
        print(f"\n❗ {injury['player']['full_name']} ({injury['team']['full_name']})")
        print(f"  🩹 Tipo: {injury['type']}")
        print(f"  📝 Detalle: {injury['note'] or 'Sin detalles'}")

def save_injury_data(data):
    """Guarda los datos en JSON"""
    fecha = datetime.now().strftime('%Y-%m-%d')
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.abspath(os.path.join(script_dir, '..', 'data', 'json'))
    
    os.makedirs(output_dir, exist_ok=True)
    file_path = os.path.join(output_dir, f"nba_injuries_balldontlie_{fecha}.json")
    
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    
    print(f"\n💾 Datos guardados en: {file_path}")

if __name__ == "__main__":
    get_nba_injuries()