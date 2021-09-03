import random

meleeWeap = 'itemgen/medivalmelee.txt'
rangedWeap = 'itemgen/medivalranged.txt'
powderWeap = 'itemgen/medivalgunpowder.txt'
enchantments = 'itemgen/enchantments.txt'
ofsomething = 'itemgen/ofsomething.txt'

def randstat():
  chancePool = random.randrange(100)
  if chancePool in range(0, 10):
    return '+3 '
  if chancePool in range(11, 35):
    return '+1 '
  if chancePool in range(36, 75):
    return ''
  if chancePool in range(76, 85):
    return '+2 '
  if chancePool in range(86, 95):
    return '+4 '
  if chancePool in range(96, 100):
    return '+5 '
  else:
    return '+99 '

def randweap(typeOf):
  if typeOf == 'melee':
    weapList = open(meleeWeap)
    chanceWeap = random.choice(weapList.read().split('\n'))
    weapList.close()
    return chanceWeap
  if typeOf == 'ranged':
    weapList = open(rangedWeap)
    chanceWeap = random.choice(weapList.read().split('\n'))
    weapList.close()
    return chanceWeap
  if typeOf == 'gunpowder':
    weapList = open(powderWeap)
    chanceWeap = random.choice(weapList.read().split('\n'))
    weapList.close()
    return chanceWeap
  if typeOf == 'random':
    weapList = open(random.choice([meleeWeap, rangedWeap, powderWeap]))
    chanceWeap = random.choice(weapList.read().split('\n'))
    weapList.close()
    return chanceWeap

def randenchantment():
  chanceEnchant = random.randrange(100)
  if chanceEnchant in range(0, 25):
    enchList = open(enchantments)
    enchWeap = random.choice(enchList.read().split('\n'))
    enchList.close()
    return enchWeap
  if chanceEnchant in range(26, 75):
    return ''
  if chanceEnchant in range(76, 100):
    enchList = open(enchantments)
    enchWeap = random.choice(enchList.read().split('\n'))
    enchList.close()
    return enchWeap

def randsomething():
  chanceSomething = random.randrange(100)
  if chanceSomething in range(0, 25):
    someList = open(ofsomething)
    someWeap = random.choice(someList.read().split('\n'))
    someList.close()
    return someWeap
  if chanceSomething in range(26, 75):
    return ''
  if chanceSomething in range(76, 100):
    someList = open(ofsomething)
    someWeap = random.choice(someList.read().split('\n'))
    someList.close()
    return someWeap

def generateWeapon(typeOf):
  if typeOf not in ['melee', 'ranged', 'powder']:
    weapon = randweap('random')
  if typeOf == None:
    weapon = randweap('random')
  stat = randstat()
  enchant = randenchantment()
  somethings = randsomething()
  return stat + enchant + weapon + somethings
