def city_functions(cityname, countryname, population=''):
    if population:
        city_country = f"{cityname}, {countryname} - population: {population}"
    else:
        city_country = f"{cityname}, {countryname}"
    return city_country.title()