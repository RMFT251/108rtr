

def about_me():
    me = {
        "first": "Big Meech",
        "last": "LarryHoover",
        "age": 33,
        "address": {
            "street": "GetMoneyLn",
            "number": "8888",
            "city": "Pritchard",
            "zip": "68833",
        }
    }
    
    print(me)
    
    
    # read values
    print(me["first"] + "" + me["last"])
    print("I'm" + str(me["age"]) + "years old")
    
    # read the address
    
    address = me["address"]
    street = address["street"]
    num = address["number"]
    city = address["city"]
    zip = address["zip"]
    print(street)
    
    # a) Return to : street #numb, city, zip.
    print(f"Return to: {street} #{num} {city} {zip}.")
    
    
# fn calls
about_me()    