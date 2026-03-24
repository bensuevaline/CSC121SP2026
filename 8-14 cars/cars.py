def make_car(manufacturer, model, **kwargs):
    car = {}
    
    car['manufacturer'] = manufacturer
    car['model'] = model
    
    # add any additional information
    for key, value in kwargs.items():
        car[key] = value
        
    return car


# function call
car = make_car('tesla', 'model 3', color='white', autopilot=True)

# print result
print(car)
