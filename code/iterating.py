print(dir({}))

hero = {
  'name' : 'Moira',
  'role' : 'support',
  'health' : 200
}

for item in hero:
  print(item)


for key in hero:
  print(f'Key: {key}, Value: {hero[key]}')