
# Dictionaries aka 
# Hashes, HashMap, HashTables, Object, Map

# places = {
#     'farm burger': '1234 piedmont, atlanta',
#     'naan stop': '12345 piedmont, atlanta',
# }
# what is the address of farm burger?

# print(places['farm burger'])

friends = {
    'Europe':{ 
        'Paris': ['Frankie','Grace'],
        'Berlin': ['Bobbie']
    },
    'Asia': ['my cousin', 'my other cousin', 'their friend'],
    'US': {
        'Angela':{
            'pets':{
                'Oakley': { 
                    'toys':['everything'
                    ]
                }
            }
        }
    }
}

#directs to berlin
friends['Europe']['Berlin']

friends['Europe']['Paris'][0] #directs to Grace

friends['US']['Angela']['pets']['Oakley']['toys']

for item in friends['toys'][0]:
    print('%s is one of Oakley\'s fav toys' %( item))
