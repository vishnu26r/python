import requests

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}"
    response =  requests.get(url)
    #print(response)
    if response.status_code == 200:
        pokemon_data = response.json()
        return pokemon_data
    else:
        print(f"failed to retrive data {response.status_code}")

pokemon_name = "ditto"
pokemon_info =  get_pokemon_info(pokemon_name)

if pokemon_info:
    print(f"Name      : {pokemon_info['name']}")
    print(f"Id        : {pokemon_info['id']}")
    print(f"Height    : {pokemon_info['height']}")
    print(f"Weight    : {pokemon_info['weight']}")

for ablility in pokemon_info['abilities']:
    print(f"abilities : {ablility['ability']['name']}")



