import requests

def get_population(municipio):
    url = "https://servicodados.ibge.gov.br/api/v1/projecoes/populacao/municipio"
    response = requests.get(url).json()
    
    for m in response:
        if m['nome'].upper() == municipio.upper():
            return{
                "municipio": m['nome'],
                "uf": m["microrregiao"]["mesorregiao"]["UF"]["nome"],
                "id": m["id"],
            }
            
    return None        