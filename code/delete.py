watches = {
  'Speedmaster' : 'Omega',
  'Submariner' : 'Rolex',
  'Tank' : 'Cartier'
}

del watches['Submariner']
print(watches)
watches = {
  'Speedmaster' : 'Omega',
  'Submariner' : 'Rolex',
  'Tank' : 'Cartier'
}

print(watches.pop('Speedmaster'))


watches = {
  'Speedmaster' : 'Omega',
  'Submariner' : 'Rolex',
  'Tank' : 'Cartier'
}

watches.clear()
print(watches)