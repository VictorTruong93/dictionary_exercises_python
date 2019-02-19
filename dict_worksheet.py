


# phonebook_dict = {
#     'Alice': '703-493-1834',
#     'Bob': '857-384-1234',
#     'Elizabeth': '484-584-2923'
# }

# # print(phonebook_dict['Elizabeth'])
# phonebook_dict["Kareem"]='938-489-1234'
# # print(phonebook_dict['Kareem'])
# del phonebook_dict['Alice']
# # print(phonebook_dict)
# # phonebook_dict['Bob']='968-345-2345'
# # print(phonebook_dict['Bob'])
# print(phonebook_dict)

ramit = {
    'name': 'Ramit',
    'email': 'ramit@gmail.com',
    'interests': ['movies', 'tennis'],
    'friends': [
    {
        'name': 'Jasmine',
        'email': 'jasmine@yahoo.com',
        'interests': ['photography', 'tennis']
    },
    {
        'name': 'Jan',
        'email': 'jan@hotmail.com',
        'interests': ['movies', 'tv']
    }
    ]
}

## print Jasmine's email address
# for f in ramit['friends']:
#     if f['name']=='Jasmine':
#         print(f['email'])

# # print 2nd of Jan's interest
# for f in ramit['friends']:
#     if f['name']=='Jan':
        # print(f['interests'][1])

letters = {
    'a':0,
    'b':0,
    'c':0,
    'd':0,
    'e':0,
    'f':0,
    'g':0,
    'h':0,
    'i':0,
    'j':0,
    'k':0,
    'l':0,
    'm':0,
    'n':0,
    'o':0,
    'p':0,
    'q':0,
    'r':0,
    's':0,
    't':0,
    'u':0,
    'v':0,
    'w':0,
    'x':0,
    'y':0,
    'z':0,
}
phrase=input('Enter phrase: ')
phrase=list(phrase)

for x in phrase:
    if x ==letters['a']:
        letters ['a'] = letters['a'] +1
print(letters['a'])
