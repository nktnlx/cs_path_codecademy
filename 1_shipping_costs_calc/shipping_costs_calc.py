from tabulate import tabulate  # https://pypi.org/project/tabulate/


print('Welcome to the "Fast&Furious" Shipping Agency!\nHere is a list of our tariffs:')


# shipping tariffs data
ground_shipping = [['less than 2 kg', 1.5],
                   ['from 2 to 6 kg', 3.0],
                   ['from 6 to 10 kg', 4.0],
                   ['10 kg and more', 4.75]]

drone_shipping = [['less than 2 kg', 4.5],
                   ['from 2 to 6 kg', 9.0],
                   ['from 6 to 10 kg', 12.0],
                   ['10 kg and more', 14.25]]


# formatting tables to display with shipping tariffs
print('\n', *'GROUND SHIPPING')
print(tabulate(ground_shipping, headers=['Weight', 'Price per kg, USD'], tablefmt='pretty'))
print('Plus 20.0 USD fix price for the total sum of the tariff.')

print('\n')
print(*'PREMIUM GROUND SHIPPING')
print(tabulate([['125.0 USD fix price for any weight!']], tablefmt='pretty'))

print('\n')
print(*'DRONE SHIPPING')
print(tabulate(drone_shipping, headers=['Weight', 'Price per kg, USD'], tablefmt='pretty'))


# receiving an input from a user
weight = 0
while weight == 0:
    try:
        weight = abs(float(input('\n\nPlease, enter the weigth of your parcel in kg and we\'ll provide you with the cheapest option of the shipment: ')))
    except ValueError:
        print('Please, enter a valid weight in kg!')

        
def shipping_cost_ground(weight):
    if weight < 2:
        price_per_kg = 1.50
    elif weight < 6:
        price_per_kg = 3.00
    elif weight < 10:
        price_per_kg = 4.00
    else:
        price_per_kg = 4.75
        
    return 20 + (price_per_kg * weight)


shipping_cost_premium = 125.00


def shipping_cost_drone(weight):
    if weight < 2:
        price_per_kg = 4.50
    elif weight < 6:
        price_per_kg = 9.00
    elif weight < 10:
        price_per_kg = 12.00
    else:
        price_per_kg = 14.25
        
    return price_per_kg * weight


def print_cheapest_method(weight):
    ground = shipping_cost_ground(weight)
    premium = shipping_cost_premium
    drone = shipping_cost_drone(weight)
    
    if ground < premium and ground < drone:
        method = 'standard ground'
        cost = ground
    elif premium < ground and premium < drone:
        method = 'premium ground'
        cost = premium
    else:
        method = 'drone'
        cost = drone
                
    print(f'\nThe cheapest option available for a {weight} kg parcel is {cost:.2f} USD with {method} shipping.')
    
    
print_cheapest_method(weight)