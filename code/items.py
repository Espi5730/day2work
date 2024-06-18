heroes = {
  'Moira' : 'support',
  'Sombra' : 'dps',
  'Zarya' : 'tank'
}

print(heroes.items())

for item in heroes.items():
  print(f'{item[0]} is a {item[1]} hero.')

  heroes = {
  'Moira' : 'support',
  'Sombra' : 'dps',
  'Zarya' : 'tank'
}

for key, value in heroes.items():
  print(f'{key} is a {value} hero.')