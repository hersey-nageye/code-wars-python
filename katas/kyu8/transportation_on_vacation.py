def rental_car_cost(d):
    daily_rate = 40
    total_cost = daily_rate * d
    
    if d >= 7:
        total_cost -= 50
    elif d >= 3:
        total_cost -= 20
    
    return total_cost