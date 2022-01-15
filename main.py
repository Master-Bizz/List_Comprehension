def greet(name):
   return f" Welcome back, {name}."

print(greet('William'))

def greet(name, msg):
   return f" Time for lists part_2.. Master {name},\n {msg}"
print(greet("William", " Repetition is more accurate & focused then mere practice."))


list = ['William', 'concatenation', 'faustration']
list.append('Kind')
print(list)

list.insert(0, 'Master')
print(list)

print(list[1:2])

list[2] = ['is, cool']
print(list)
list[3] = "ez"
print(list)
print(list[2][0])
#---------------------------ME RECAPPING-------------------------------------------=


'''
List Comprehension
'''
squares = []
for x in range(10):
   squares.append(x*2)
print(squares)

squares = []
for x in range(10):
   squares.append(x**2)
print(squares)
# Same as...
print([x**2 for x in range(10)])  # comprehension - all on one line
'''
Conditionals in List Comprehension
'''# 4 loops
combs = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:   # (!=) means 'not equal to..''
            combs.append((x, y))
print(combs)

combs = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]  # comprehension may be too long so previous method may be ideal
print(combs)
'''
Nested List Comprehensions
'''
matrix = [
  [1,2,3,4],
  [5,6,7,8],
  [9,10,11,12]
]
print(len(matrix))

k = [[row[r] for row in matrix] for r in range(4)]    # Simplified
print(k)

k = []
for r in range(4):
   k.append ([row[r] for row in matrix])     # Expanded
print(k)

k = []
for r in range(4):
   k_row = []
   for row in matrix:
       k_row.append (row[r])
   k.append(k_row)                 # Expanded further still
print(k)
#---------------------------------------------------

juke = []
for s in [23,89,89,367]:
  for p in [89,23,367,89]:
    for t in [56,567,78,23]:
       if s != p != t != s:
         juke.append(((s, p, t)))
    else:
     juke.append("Yay")
print(juke)
juke = [(s,p,t) for s in [23,89,89,367] for p in [89,23,367,89] for t in [56,567,78,23] if s != p != t != s]
print(juke)

Jack = [
  ['Zaz',63,23,'Ouch',9],
  ['pow',23,90,'Soft',0],
  [23,22,15,349,'Smoothie'],
  [67,879,67,34,'nut']
]

print(len(Jack))
test = [[column[c] for column in Jack] for c in range(5)]
print(test)
test = []
for c in range(5):
   test.append ([column[c] for column in Jack])
   print(test)

test = []
for c in range(5):
   test_column = []
   for column in Jack:
      test_column.append(column[c])
   test.append(test_column)
print(test)