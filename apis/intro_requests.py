import requests

# =========================== HTTP Status Codes ============================ #
# Status Code Overview:
# 200: OK - The request was successful.
# 201: Created - Resource was successfully created (used in POST requests).
# 204: No Content - The request was successful but no content was returned.
# 400: Bad Request - The request is malformed or missing required parameters.
# 401: Unauthorized - Authentication is required to access the resource.
# 403: Forbidden - The server understands the request, but it refuses to authorize it.
# 404: Not Found - The requested resource could not be found on the server.
# 500: Internal Server Error - A generic error occurred on the server.
# 503: Service Unavailable - The server is currently unavailable (overloaded or down for maintenance).
# 300s: Redirection - The request needs further action to complete (e.g., URL has moved).

# Base URL for the PokéAPI
base_url = "https://pokeapi.co/api/v2/"

# =========================== Single Pokémon Fetch =========================== #

# Define a Pokémon name (can be replaced with user input)
pokemon_name = "nonexistentpokemon"  # Example: a Pokémon that doesn't exist

# Construct the URL to fetch data
url = f"{base_url}pokemon/{pokemon_name}"

# Send GET request to the API
response = requests.get(url)

# Handle the response based on the status code
if response.status_code == 200:
    # Successful request
    data = response.json()
    print(f"Name: {data['name'].capitalize()}")
    print(f"Height: {data['height']} m")
    print(f"Weight: {data['weight']} hectograms")
    print("Types:")
    for type_info in data['types']:
        print(f"- {type_info['type']['name'].capitalize()}")
else:
    # Handle errors based on status code
    if response.status_code == 400:
        print("Bad Request: The request might have an issue with the endpoint or parameters.")
    elif response.status_code == 404:
        print(f"Not Found: The Pokémon '{pokemon_name}' does not exist.")
    elif response.status_code == 500:
        print("Server Error: Something went wrong on the server. Please try again later.")
    else:
        print(f"Error {response.status_code}: Please check your request and try again.")

# =========================== Iterate List of Pokémon ========================= #

pokemon_names = ["pikachu", "bulbasaur", "charmander", "squirtle"]

# Iterate through a list of Pokémon names
for pokemon_name in pokemon_names:
    url = f"{base_url}pokemon/{pokemon_name}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print(f"Name: {data['name'].capitalize()}")
        print(f"Height: {data['height']} m")
        print(f"Weight: {data['weight']} hectograms")
        print("Types:")
        for type_info in data['types']:
            print(f"- {type_info['type']['name'].capitalize()}")
        print("-" * 40)
    else:
        print(f"Failed to fetch data for {pokemon_name}")


# =========================== Fetch Pokémon by ID =========================== #

# Function to fetch and print Pokémon info using the Pokémon ID
def fetch_pokemon_info(pokemon_id):
    response = requests.get(f"{base_url}pokemon/{pokemon_id}")
    if response.status_code == 200:
        return response.json()  # Return the JSON data if successful
    else:
        return None


# Iterate through the first 20 Pokémon by ID
for i in range(1, 21):
    pokemon_info = fetch_pokemon_info(i)
    if pokemon_info:
        print(f"Pokémon #{i}: {pokemon_info['name'].capitalize()}")
        print(f"ID: {pokemon_info['id']}")
        print(f"Height: {pokemon_info['height']} m")
        print(f"Weight: {pokemon_info['weight']} hectograms")
        print(f"Types: {[t['type']['name'] for t in pokemon_info['types']]}")
        print("-----")

# =========================== Search Pokémon by Type ======================== #

# Example type: 'fire'
type_name = "fire"
url = f"{base_url}type/{type_name}"

response = requests.get(url)

# Check if the request for the Pokémon type was successful
if response.status_code == 200:
    data = response.json()
    print(f"{type_name.capitalize()} type Pokémon:")
    for pokemon in data['pokemon']:
        print(f"- {pokemon['pokemon']['name'].capitalize()}")
else:
    print(f"Failed to fetch data for {type_name} type Pokémon.")
