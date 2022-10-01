school = []

klass = {
    'name': '1a',
    'year': '5',
}
school.append(klass)

klass = {
    'name': '3a',
    'year': '7',
}
school.append(klass)

school[1] = {
    'name': '3a',
    'year': '4',
}
klass = {
    'name': '4f',
    'year': '32',
}
school.append(klass)

del(school[0])

print(school)