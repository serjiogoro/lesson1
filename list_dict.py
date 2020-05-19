a = [3,5,7,9,10.5]
print(a)
a.append('Python')
print(len(a))
#
print(a[0])
print(a[-1])
print(a[2:4])
a.remove('Python')
#----------------------
d = {"city": "Москва", "temperature": "20"}
print(d['city'])
d['temperature'] = int(d['temperature']) - 5
print(d)
#
print(d.get('country'))
print(d.get('country', 'Россия'))
d['date'] = '27.05.2019'
print(d)