#lets you interact with web api
import requests


#gets the info from the api to to answer the country input
def Country_info(country):
    Base_url = "https://restcountries.com/v3.1/name/" + country
    req = requests.get(Base_url)
    info = req.json()
    return info


#this should show up and prompt you to put in a country
def begin():
    defined_country = input("Put a country: ")
   
    #attempts to try and run the info and if not, the except steps into play.
    try:
        info = Country_info(defined_country)
    except Exception as e:
        print("None of this information can be found.")
        return


    #This grabs information about the places
    data = info[0]
    capital_city = data.get('capital', ['No capital'])[0]
    Population_of_country = data.get('population', "This is not known")
    Place = data.get('place', "This isn't made clear")


    #This is a function
    Capital_is_existing = "Correct" if capital_city != 'not a capital' else "Incorrect"


    #This should display stuff about the countries
    print("Country:", defined_country)
    print("Capital:", capital_city)
    print("Has a capital:", Capital_is_existing)
    print("Place (Location):", Place)
    print("Population:", Population_of_country)


    #This should find the information about the certain currency for that specific country
    cash = data.get('currencies', {})
    print("Money:")
    for amount in cash.values():
        print("-", amount.get('name', 'Not sure what money this is'))
   
    #This gets the language information for that country
    Foreign = data.get('languages', {})
    print("Language:")
    for language in Foreign.values():
        print("-", language)


    #This portion asks if the population is over 1 million and then prints the response
    if Population_of_country > 1000000:
        print(f"{defined_country} is populated.")
    
    #this will print if the population is below 1 million
    else:
        print(f"{defined_country} is not populated?")


#this checks if the file is being ran
if __name__ == "__main__":
    begin()
