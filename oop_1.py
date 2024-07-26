class Student:
    def __init__(self, name, marks):
        self.name = name;
        self.marks = marks;
                
    #Defining the method to get avg marks
    def avg_mark(self):
        sum = 0;
        for val in self.marks:
            sum += val;
        print(f"Hello {self.name}, your average mark is {sum/3}")
            
s1 = Student("Fahad", [99, 98, 97])

s1.avg_mark()