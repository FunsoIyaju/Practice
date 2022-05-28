motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles.append('Siemens')
print(motorcycles)

motorcycles.insert(2,'Sotra')
print(motorcycles)

#del motorcycles[0]
#print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was {last_owned.title()}.")