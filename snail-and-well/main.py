import statistics

print('PROBLEM 1:')
accumulated_distance = 0
daily_advance = 30
well_height = 0
night_retreat = 20
days = 0

while well_height <= 125:
    well_height += daily_advance
    accumulated_distance += daily_advance
    if well_height <= 125:
        well_height = well_height - night_retreat
        accumulated_distance += daily_advance
    days += 1
print('Days = ' + str(days))

print('BONUS 1:')
accumulated_distance = 0
daily_advance = 0
well_height = 0
night_retreat = 20
days = 0
advance_cm = [30, 21, 33, 77, 44, 45, 23, 45, 12, 34, 55]

for daily_advance in advance_cm:
    daily_advance = int(daily_advance)
    well_height += daily_advance
    accumulated_distance += daily_advance
    well_height = well_height - night_retreat
    days += 1
    accumulated_distance += daily_advance
    if well_height > 125:
        break

print('Days = ' + str(days))
print('Maximun Displacement = ' + str(max(advance_cm)))
print('Minimum Displacement = ' + str(min(advance_cm)))
print('Average = ' + str(sum(advance_cm) / len(advance_cm)))
print('Deviation = ' + str(statistics.stdev(advance_cm)))

