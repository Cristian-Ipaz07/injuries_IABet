import requests
import json
import os
from datetime import datetime

# Configuración de la API
API_KEY = 'Z46Ud2TAfYs4jeaeUZF3cxoggW7ZNuhneOAdtued'
LANG = 'en'

def get_nba_injuries():
    """Obtiene y procesa datos de lesiones de la NBA"""
    url = f'https://api.sportradar.com/nba/trial/v7/{LANG}/league/injuries.json?api_key={API_KEY}'
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Lanza error si hay problemas HTTP
        
        data = response.json()
        print_injury_summary(data)
        save_injury_data(data)
        
    except requests.exceptions.RequestException as e:
        print(f"❌ Error al conectar con la API: {e}")

def print_injury_summary(data):
    """Muestra un resumen de las lesiones en consola"""
    print("\n📊 RESUMEN DE LESIONES NBA - ÚLTIMAS ACTUALIZACIONES")
    print("=" * 50)
    
    for team in data.get('teams', []):
        print(f"\n🏀 {team['name']} ({team['market']} {team['alias']})")
        
        if not team.get('players'):
            print("  ✅ No hay jugadores lesionados.")
            continue
            
        for player in team['players']:
            print(f"  ❗ {player['full_name']} - {player['injuries'][0]['desc']}")
            print(f"     📅 Fecha: {player['injuries'][0]['date']}")
            print(f"     📝 Detalle: {player['injuries'][0]['comment']}")

def save_injury_data(data):
    """Guarda los datos en un archivo JSON con fecha"""
    fecha = datetime.now().strftime('%Y-%m-%d')
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.abspath(os.path.join(script_dir, '..', 'data', 'json'))
    
    os.makedirs(output_dir, exist_ok=True)
    file_path = os.path.join(output_dir, f"nba_injuries_{fecha}.json")
    
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    
    print(f"\n💾 Datos guardados en: {file_path}")

if __name__ == "__main__":
    get_nba_injuries()