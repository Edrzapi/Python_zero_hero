import requests

# Define the base URL for the PokéAPI
base_url = "https://pokeapi.co/api/v2/"

# Define an invalid Pokémon name (or an incorrect endpoint)
pokemon_name = "nonexistentpokemon"  # This Pokémon doesn't exist

# Construct the URL to fetch data
url = f"{base_url}pokemon/{pokemon_name}"

# Send the GET request
response = requests.get(url)

# Check if the response was successful
if response.status_code == 200:
    # If successful, parse the JSON response
    data = response.json()
    print(f"Name: {data['name'].capitalize()}")
    print(f"Height: {data['height']} ")
    print(f"Weight: {data['weight']}")
    print("Types:")
    for type_info in data['types']:
        print(f"- {type_info['type']['name'].capitalize()}")
else:
    # Handle different types of errors based on the status code
    if response.status_code == 400:
        print("Bad Request: There was an issue with the request. Maybe the endpoint or parameters are wrong.")
    elif response.status_code == 404:
        print(f"Not Found: The Pokémon '{pokemon_name}' does not exist.")
    elif response.status_code == 500:
        print("Server Error: Something went wrong on the server. Please try again later.")
    else:
        print(f"Error {response.status_code}: Something went wrong. Please check the request and try again.")

# =========================== Iterate List of Names ================================= #

pokemon_names = ["pikachu", "bulbasaur", "charmander", "squirtle"]

for pokemon_name in pokemon_names:
    url = f"{base_url}pokemon/{pokemon_name}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print(f"Name: {data['name'].capitalize()}")
        print(f"Height: {data['height']} ")
        print(f"Weight: {data['weight']} ")
        print("Types:")
        for type_info in data['types']:
            print(f"- {type_info['type']['name'].capitalize()}")
        print("-" * 40)

# =========================== Iterator ================================= #

# URL for the Pokémon API
api_url = "https://pokeapi.co/api/v2/pokemon/"


# Function to fetch and print Pokémon info as dictionary
def fetch_pokemon_info(pokemon_id):
    response = requests.get(f"{api_url}{pokemon_id}")
    if response.status_code == 200:
        # Convert the response to JSON and return it
        return response.json()
    else:
        return None


# Iterate through first 20 Pokémon
for i in range(1, 21):
    pokemon_info = fetch_pokemon_info(i)
    if pokemon_info:
        print(f"Pokémon #{i}: {pokemon_info['name']}")
        print(f"ID: {pokemon_info['id']}")
        print(f"Height: {pokemon_info['height']}")
        print(f"Weight: {pokemon_info['weight']}")
        print(f"Types: {[t['type']['name'] for t in pokemon_info['types']]}")
        print("-----")

# =========================== Search by type ================================= #

type_name = "fire"
url = f"{base_url}type/{type_name}"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(f"{type_name.capitalize()} type Pokémon:")
    for pokemon in data['pokemon']:
        print(f"- {pokemon['pokemon']['name'].capitalize()}")
else:
    print(f"Failed to fetch data for {type_name} type Pokémon.")
