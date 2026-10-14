class Parrot:
    species ="bird"
    def __init__(self, name, age):
        self.name = name 
        self.age = age
blu = Parrot("blu", 10)
print(blu.name )
print(blu.age)