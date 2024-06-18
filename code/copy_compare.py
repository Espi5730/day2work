watches1 = {
  'Speedmaster' : 'Omega',
  'Submariner' : 'Rolex',
  'Tank' : 'Cartier'
}

watches2 = watches1
watches1['Submariner'] = 'Tudor'

print(watches1)
print(watches2)

watches1 = {
  'Speedmaster' : 'Omega',
  'Submariner' : 'Rolex',
  'Tank' : 'Cartier'
}

watches2 = watches1.copy()
watches1['Submariner'] = 'Tudor'

print(watches1)
print(watches2)

watches1 = {
  'Speedmaster' : 'Omega',
  'Submariner' : 'Rolex',
  'Tank' : 'Cartier'
}

watches2 = {
  'Tank' : 'Cartier',
  'Submariner' : 'Rolex',
  'Speedmaster' : 'Omega'
}

print(watches1 == watches2)