# /*
#  * Llamar a una API es una de las tareas más comunes en programación.
#  *
#  * Implementa una llamada HTTP a una API (la que tú quieras) y muestra su
#  * resultado a través de la terminal. Por ejemplo: Pokémon, Marvel...
#  *
#  * Aquí tienes un listado de posibles APIs:
#  * https://github.com/public-apis/public-apis
#  */

import requests

url = "https://pokeapi.co/api/v2/pokemon?limit=151"

response = requests.get(url)

for pokemon in response.json()['results']:
    print(pokemon['name'])



