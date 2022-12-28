import requests
import json

# Ask for user input
while True:
    pokemon_name = input("enter the name of a Pokemon: ")
    pokemon_name = pokemon_name.lower()

    # create a dynamic URL based on input
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"

    # Fetch data from URL
    response = requests.get(url)

    # Check if response is valid
    if response.status_code == 200:
        data = response.json()



    # print out all the pokemon data
    print(f"Name is \t\t{data['name']}")
    print("Abilities:")

    for ability in data['abilities']:
        print(ability['ability']['name'])
else:
    print("Sorry, I couldn't find that Pokemon")




