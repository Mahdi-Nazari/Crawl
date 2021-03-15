import requests

"""words = ['Mahdi', "Nazari", '16']

name = "_".join(words)

print(name)


mahdi = "Mah.di"
if "." in mahdi:
    mahdi = mahdi.replace('.', '/')
    print(mahdi)
"""
"""
my_dict = {
    'Sound': {
        'Louds.peaker ': 'Yes', 
        '3.5mm jack ': 'Yes'
    }
}

for key in my_dict:
    for inner_key in my_dict[key]:
        if "." in inner_key:
            new_inner_key = inner_key.replace('.', '/')
    if new_inner_key:
        my_dict[key][new_inner_key] = my_dict[key].pop(inner_key)

print(my_dict)

my_dict['Sound']['3/5mm jack '] = my_dict['Sound'].pop('3.5mm jack ')
print(my_dict)"""


"""myDict = {1:"one",2:{3:"three",4:"four"}}
myDict[2][5] = myDict[2].pop(4)
print myDict

Output
{1: 'one', 2: {3: 'three', 5: 'four'}}"""

url = 'https://www.gsmarena.com/sitemap-phones.xml'
r = requests.get(url, allow_redirects=True)
open('sitemap-phones.xml', 'wb').write(r.content)