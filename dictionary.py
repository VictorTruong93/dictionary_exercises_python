

# # dictionary:
# # collection of objects in a key value pair
meal = {
# key : value,
    'drink':'Creature Comforts Athena',
    'appetizer':'charcuterie',
    'dinner':'Grindhouse burger',
    'dessert':'cupcakes',
}
house = {
    'kitchen':'Fancy Refrigerator',
    'bathroom':3,
    'bedrooms':4,
    'living room':'giant',
}
user ={
    'firstname': 'Victor',
    'lastname':'Truong',
}

# # print(meal['dessert'])
# # print(house['kitchen'])
# # print(user['firstname'])
# # # print('%s would like the %s in the %s'% (user['firstname'],meal['dessert'],house['kitchen']))
# # if/else looks at keys, not value
# # if 'appetizer' in meal:
# #     print ('We have appetizer.')
# # else:
# #     print('Where is the ham?')
# # # print(meal) (method to search for if key is in dictionary)
# # # meal['water'] = 'tap'
# # # meal['bread'] = True
# # meal['drink']= 'Guinness' (changes key's value in dictionary)
# # print(meal)
# # del meal['water']

# digitalcrafts
# ['US']['Georgia']['Atlanta']
digitalcrafts ={
    'US':{
        'Georgia':{
            'Atlanta':'3424 Piedmont Rd NE #420',},
        'Texas': {
            'Houston':'3302 Canal St.'}
        }
    }


# add into dictionary with nested
digitalcrafts['US']['Washington']={'Seattle':'123 Pearl Jam Ave'}
#below is example of adding only a key, needs empty square bracket.
digitalcrafts['US']['Florida']={}
# to add a campus in canada
digitalcrafts['Canada']={'British Columbia': {'Vancouver':'123 Terrance and Phillip Way'}}
# print(digitalcrafts)
# Convenience methods
countries = digitalcrafts.keys()
state =digitalcrafts['US'].keys()
# for key in state:
#     print(digitalcrafts['US'][key])
def us_cities(state):
    cities=[]
    for key in state:
        cities.append(digitalcrafts['US'][key])
    return cities
# # print(us_cities(state))


# nesting for-loops
for country in digitalcrafts:
    for state in digitalcrafts[country]:
        print(country, state, end=': ')
        for city in digitalcrafts[country][state]:
            print(city)