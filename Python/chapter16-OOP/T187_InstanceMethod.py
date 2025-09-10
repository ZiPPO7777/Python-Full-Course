# Instance methods

class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.age}"
    
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

p1 = Person('Bulbul', 'Hassan', 21)

print(p1)

print(p1.full_name())


# Clear Method
l = [1,2,3,4,5]

# l.clear()
list.clear(l)
print(l)
print('---------------------cleared-----------------')


l = [1, 2, 3]
list.append(l, 4) 
print(l)  # [1, 2, 3, 4]
