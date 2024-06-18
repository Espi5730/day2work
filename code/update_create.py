watches = {
  'Speedmaster' : 'Omega',
  'Submariner' : 'Rolex',
  'Tank' : 'Cartier'
}

watches.update(Speedmaster='Swatch Group', Tank='Richemont')
print(watches)
watches1 = {
  'Speedmaster' : 'Omega',
  'Submariner' : 'Rolex',
  'Tank' : 'Cartier'
}

watches2 = {
  'Calatrava' : 'Patek PhilippUpdating and Creatinge',
  'Datejust' : 'Rolex',
  'Royal Oak' : 'Audemars Piguet'
}

watches1.update(watches2)
print(watches1)

models = ['Speedmaster', 'Submariner', 'Tank']

watches1 = dict.fromkeys(models)
watches2 = dict.fromkeys(models, 'Manufacturer')

print(watches1)
print(watches2)


dict1 = {
  'red' : 'english',
  'rouge' : 'french',
  'rojo' : 'spanish'
}

dict2 = {
  'blue' : 'english',
  'bleu' : 'french',
  'azul' : 'spanish'
}

dict1.update(dict2)

print(dict1)