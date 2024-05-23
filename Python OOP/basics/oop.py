'''you can create as much object as you like but 
the memory is allocated only one time which helps for big and complex programme.'''

'''constructor is a built-in function which is called automatically when the object
is created...'''

class Student:
    '''gives the name of student'''


    def __init__(self, age, name, address):
        '''constructor is also important as we can pass value to
          the class or constructor let's say'''
        self.age = age
        self.name = name
        self.address = address

    def myname(self):
        print(self.name)
        print(self.age)
        print(self.address)

# std = Student(23)
std1 = Student(23, 'suman', 'Kathmandu')
# print(f"I am {std1.name} and I am {std1.age} years old. I am from {std1.address}")
# std1.myname()

class Mark:
    '''calculates the percentage of student'''

    def __init__(self, name, id, science, math, english, nepali):
        '''name, id, science, math english, nepali'''
        self.name = name
        self.id = id
        self.science = science
        self.math = math
        self.english = english
        self.nepali = nepali


    
    def percentage(self):
        self.total = self.science + self.math + self.english + self.nepali
        self.percent = (self.total)/4
    
    def result(self):
        self.percentage()
        print(f'''
The result of {self.name} with id {self.id} is:
Total Marks: {self.total}
Percentage: {self.percent}%''')
        


student1 = Mark('Suman', 11, 90, 95, 87,75)
student1.result()