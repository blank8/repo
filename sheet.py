print("helloworld")

# Mathmatical Operators
a = 2 + 2
print(a)

b = 7 - 4
print(b)

c = 2 * 4
print(c)

d = 8 / 2
print(d)

e = 21 // 7
print(e)

f = 7 % 2
print(f)

# Function Definition
def print_lyrics():
    print("I'm a lumberjake, and I'm okay.")
    print("I sleep all night and I work all day")

# Function Returns a String
def return_lyrics():
    lyrics = "I'm a lumberjack, and I'm okay"
    lyrics = lyrics + "I sleep all night and I work all day"
    return lyrics
lumberjackSong = return_lyrics()

# If Statement
numb = 1
if numb == 1:
    print("one")
elif numb == 2:
    print("two")
else:
    print("bigger number")

# While Loop
i = 0
while i < 5:
    print('hello')
    i += 1

# Nested Loop
i = 0
j = 0
while i < 5:
    while j < 5:
        print(j, end='')
        j += 1
    print('\n###############')
    j = 0
    i += 1

# While Using Range()
for number in reange(12, 20):
    print(number)

# Boolean Operators
x = 41
if x == 42: # equals
    print("equals")
if x != 42: # not equal
    print("not equals")
if x > 42: # greater than
    print("greater than")
if x >= 42: # greater than or equal to
    print("greater than or equal to")
if x < 42: # less than
    print("less than")
if x <= 42: # less than or equal to
    print("less than or equal to")

# List
fruits = ['apple', 'orange', 'banana', 'grape']

# Dictionarie
favFoods = {'cheese': 'mozzarella', 'meat': 'beef', 'vegetable': 'bogle'}

faveMeat = faveFoods['meat']

for foodType, food in favFoods.items():
    print('My favorite ' + foodType + ' is: ' + food)

favFoods = {'cheese': 'mozzarella',
            'meat': 'beef',
            'vegetable': 'brogle',
            'desert': 'pie',
            'meat product': 'spam'}

# str.find()
# use when the index of the subString is needed
string = "catch my catatonic cat."
subString = "cat"
stringIndex = string.find(subString)
print(stringIndex)

# using the operator "in"
# "in" will return a boolean
if(subString in string):
    print("yes")
else:
    print("no")

# str.lower()
#convert a string to lower will allow you to make comparisons that ignore case
crazyString = "It will be easy to cAtch my cAtAtonic cat."
stringIndex = crazyString.find(subString)
print(stringIndex)
stringIndex =crezyString.lower().find(subString)
print(stringIndex)
# the second print statement prints the oriinal crazyString

print(crazyString.lower())
print(crazyString)

# comparison operator
if crazyString > string:
    print("crazy")










