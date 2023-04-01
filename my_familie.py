my_fam1 = {'name':'Dmitriy', 'age': 33, 'proffesion': 'chemist', 'family_member': 'dad'}
my_fam2 = {'name': 'Julia', 'age': 38, 'proffesion': 'chemist', 'family_member': 'mom'}
my_fam3 = {'name': 'Artem', 'age': 3, 'proffesion': 'baby', 'family_member': 'sun'}
print(my_fam1.get("name"))
my_fam1['proffesion'] = 'It_machine'
print(my_fam1)
my_fam3['family_member2'] = 'grandmother'
print(my_fam3)
keysList = list(my_fam2.keys())
print(keysList)
my_fam1['sex'] = 'man'
print(my_fam1)
popped_value = my_fam1.pop('sex')
print(my_fam1)