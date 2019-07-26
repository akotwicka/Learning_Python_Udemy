ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ',
         'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']

#1
all_to_all = [(a, b) for a in ports for b in ports]
print(all_to_all)
print(len(all_to_all))

#2
not_the_same = [(a, b) for a in ports for b in ports if a != b]
print(not_the_same)
print(len(not_the_same))

#3
not_dubbled = [(a, b) for a in ports for b in ports if a > b]
print(not_dubbled)
print(len(not_dubbled))
