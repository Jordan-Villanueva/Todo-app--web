tmax = 100
tmin = 0
def state_of_water(temperature):
    if temperature >= tmax:
        return "Gas"
    elif tmin < temperature < tmax:
        return "Liquid"
    else:
        return "Solid"

