#lets you interact with web api
import requests


#gets the info from the api to to answer the country input
def Country_info(country):
    Base_url = "https://restcountries.com/v3.1/name/" + Country
    req = requests.get(Base_url)
    info = req.json()
    return info


    #this should show up and prompt you to put in a country
    def begin():
    defined_country = ("put a country")
   
   
    #attempts to try and run the info and if not, the except steps into play.
   
    try:
        info = Country_info
    except:
        print("no information")
        return
   

    #This grabs information about the places
    data = info[0]
    capital_city = data.get('capital', ['no capital']) [0]
    Population_of_country = data['population'] if 'population' in data else "not known"
    Place = data.get('place' , 0)



    #function
    Capital_is_existing = capital_city = "not a capital"



    #This should display stuff about the countries
    print("Country:" , defined_country)
    print("Capital:" , capital_city)
    print("has a capital:" , Capital_is_existing)
    print("place:" , Place)
    print("population:" , defined_country)


   #This should find the information about the certain currency for that specific country
    cash = data.get('money', {})
    print("Money")
    for key in cash.key():
        print("-", key)
   

    #This gets the language information for that country
    Foreign = data.get('language', {})
    print("language:")
    for Foreign in Foreign:
        print("-", Foreign[Foreign])
   

    #This portion asks if the population is over 1 million
    if Population_of_country > 1000000:
        print(defined_country + "is populated.")
   

    #this will print if the population is below 1 million
    else:
        print(defined_country + "Not populated?")
   

    #this checks if the file is being ran
    if _name_ =="_main_":
        begin()
