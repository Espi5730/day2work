import pprint

actor = {
  'first_name' : 'Denzel',
  'last_name' : 'Washington',
  'films' : [
    ('Malcolm X', 1992),
    ('The Hurricane',  1999),
    ('Training Day', 2001),
    ('Fences', 2016)
  ],
  'oscars' : [{
    'award' : 'Best actor in a supporting role',
    'film' : 'Glory',
    'year' : 1990
  }, {
    'award' : 'Best actor in a leading role',
    'film' : 'Training Day',
    'year' : 2002
  }]
}

movie = actor['films'][0][0]
pprint.pprint(movie)

movie = actor['last_name']
pprint.pprint(movie)
movie = actor['oscars'][0]['film']
pprint.pprint(movie)

import pprint

actor = {
  'first_name' : 'Denzel',
  'last_name' : 'Washington',
  'films' : [
    ('Malcolm X', 1992),
    ('The Hurricane',  1999),
    ('Training Day', 2001),
    ('Fences', 2016)
  ],
  'oscars' : [{
    'award' : 'Best actor in a supporting role',
    'film' : 'Glory',
    'year' : 1990
  }, {
    'award' : 'Best actor in a leading role',
    'film' : 'Training Day',
    'year' : 2002
  }]
}

pprint.pprint(actor.items())

oscars = actor['oscars']
for oscar in oscars:
  pprint.pprint(oscar.keys())


  stock_prices = {
  'AAPL' : [
    {
      'date' : '04-06-2022',
      'open' : 172.36,
      'close' : 171.83
    },
    {
      'date' : '04-07-2022',
      'open' : 171.16,
      'close' : 172.14
    }
  ],
  'MSFT' : [
    {
      'date' : '04-06-2022,
      'open' : 305.14,
      'close' : 299.5
    },
    {
      'date' : '04-07-2022',
      'open' : 296.66,
      'close' : 301.37
    }
  ]
}