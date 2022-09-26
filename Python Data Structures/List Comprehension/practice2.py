starter_pokemons = [{'name': 'Pikachu', 'type': 'Electric'},
         {'name': 'Charmander', 'type': 'Fire'},
         {'name': 'Squirtle', 'type': 'Water'},
         {'name': 'Baulbasaur', 'type': 'Grass'}]

choosing_starter_pokemons = [starter_pokemon['name']
                             for starter_pokemon in starter_pokemons
                             if starter_pokemon['type'] == 'Fire']

print(choosing_starter_pokemons)