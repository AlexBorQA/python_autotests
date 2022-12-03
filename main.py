import requests
import json

token = '359c8cdf32472a737698b25c044faf91'
response = requests.post('https://pokemonbattle.me:5000/pokemons', headers={'trainer_token': token}, json={"name": "Nord",
    "photo": "https://static.wikia.nocookie.net/pokemon/images/2/21/001Bulbasaur.png"})

print(response.json())

response_put = requests.put('https://pokemonbattle.me:5000/pokemons', headers={'trainer_token': token}, json={"pokemon_id": 1287,
    "name": "Nord-West",
    "photo": 'https://static.wikia.nocookie.net/pokemon/images/2/21/001Bulbasaur.png'})

print(response_put.json())


response_bol = requests.post('https://pokemonbattle.me:5000/trainers/addPokebol', headers={'trainer_token': token}, json={"pokemon_id": "1287"})


print(response_bol.json())