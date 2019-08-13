# Variables

dbs = [0, 1, 0, 0, 0, 0, 1, 0, 1, 23, 1, 0, 1, 1, 0, 0, 0, 
       1, 1, 0, 20, 1, 1, 15, 1, 0, 0, 0, 40, 15, 0, 0]

# Show volumes that exceed 10 dBs

exceed = []
for i in dbs:
    if i >= 10:
        exceed.append(i)
print(exceed)


# Show the moments (indexs of the list) in which a volume exceeds 10 dBs

exceed_index = []
contador = 0
for i in dbs:
    if i >= 10:
        exceed_index.append(contador)
    contador += 1    
print(exceed_index)

# Combine the last two exercises to show the moments when a 
# volume exceeds 10 dBs. HINT: Use the enumerate function

print(list(zip(exceed_index,exceed)))


# Ethan is discovered if two consecutive volumes are greater than 10 dB. Is he safe? 
# HINT: Beware of the extremes, do not have an error of the type
# IndexError: list index out of range

alarm = False
for i in dbs:
    if i > 20 and i+1 > 20:
        alarm = True
        
if alarm == True:
    print("Alarm!")









