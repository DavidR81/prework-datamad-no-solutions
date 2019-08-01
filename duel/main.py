import statistics

print('PROBLEM 2: ')
gandalf = [10, 11, 13, 30, 22, 11, 10, 33, 22, 22]
saruman = [23, 66, 12, 43, 12, 10, 44, 23, 12, 17]
gandalf_wins = 0
saruman_wins = 0

for index in range(len(gandalf)):
    if gandalf[index] > saruman[index]:
        gandalf_wins += 1
    else:
        saruman_wins += 1

print(gandalf_wins)
print(saruman_wins)
if gandalf_wins > saruman_wins:
    print('Gandalf wins')
else:
    print('Saruman wins')

print('BONUS 2: ')
POWER = {
    'Fireball': 50,
    'Lightning bolt': 40,
    'Magic arrow': 10,
    'Black Tentacles': 25,
    'Contagion': 45
}

gandalf = ['Fireball', 'Lightning bolt', 'Lightning bolt', 'Magic arrow', 'Fireball',
           'Magic arrow', 'Lightning bolt', 'Fireball', 'Magic arrow', 'Fireball']
saruman = ['Contagion', 'Contagion', 'Black Tentacles', 'Fireball', 'Black Tentacles',
           'Lightning bolt', 'Magic arrow', 'Contagion', 'Magic arrow', 'Magic arrow']
gandalf_wins = 0
saruman_wins = 0
gandalf_list = []
saruman_list = []

for index in range(len(gandalf)):
    gandalf_power = POWER[gandalf[index]]
    saruman_power = POWER[saruman[index]]
    gandalf_list.append(gandalf_power)
    saruman_list.append(saruman_power)
    if gandalf_power > saruman_power:
        gandalf_wins += 1
    else:
        saruman_wins += 1
    if gandalf_wins == 3:
        winner = 'Gandalf'
    else:
        winner = 'Saruman'

print([gandalf_list, saruman_list])
if winner == 'Gandalf':
    print('Gandalf wins')
else:
    print('Saruman wins')
print(str(sum(gandalf_list) / len(gandalf_list)))
print(str(sum(saruman_list) / len(saruman_list)))
print(str(statistics.stdev(gandalf_list)))
print(str(statistics.stdev(saruman_list)))
