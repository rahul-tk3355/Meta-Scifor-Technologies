# Q1.Create a student management system project using the classes and objects concept in python which should perform the following operations

# 1.Accept Student details

# 2.Display Student Details

# 3.Search Details of a Student

# 4.Delete Details of Student

# 5.Update Student Details

# 6.Exit
#create a student class and add functions for the above shown options in the description and ask the user to choose one among them.

class Student:
  def __init__(self, name, rollno, m1, m2):
        self.name = name
        self.rollno = rollno
        self.m1 = m1
        self.m2 = m2
  def accept(self, Name, Rollno, marks1, marks2):
        ob = Student(Name, Rollno, marks1, marks2)
        ls.append(ob)

  def display(self, ob):
        print("Name : ", ob.name)
        print("RollNo : ", ob.rollno)
        print("Marks1 : ", ob.m1)
        print("Marks2 : ", ob.m2)
        print("\n")

  def search(self, rn):
        for i in range(ls.__len__()):
          if(ls[i].rollno == rn):
            return i

  def delete(self, rn):
        i = obj.search(rn)
        del ls[i]

  def update(self, rn, No):
        i = obj.search(rn)
        roll = No
        ls[i].rollno = roll

ls = []
obj = Student('', 0, 0, 0)
ch = int(input("Enter choice:"))
if ch == 1:
  obj.accept("A", 1, 100, 100)
  obj.accept("B", 2, 90, 90)
  obj.accept("C", 3, 80, 80)
elif ch == 2:
  print("\nList of Students\n")
  for i in range(ls.__len__()):
    obj.display(ls[i])
elif ch == 3:
  print("\n Student Found, ")
  s = obj.search(2)
  obj.display(ls[s])
elif ch == 4:
  obj.delete(2)
  print(len(ls))
  print("List after deletion")
  for i in range(ls.__len__()):
    obj.display(ls[i])
elif ch == 5:
  obj.update(3, 2)
  print(len(ls))
  print("List after updation")
  for i in range(ls.__len__()):
    obj.display(ls[i])
else:
  print("Thank You !")

# #Q2. Nidhi is trying to understand how the phone gets updated with
# new features with all the old features already available in the new phone.
# Write a program to explain this with the help of inheritance and method
# overriding. Hint: Create class Nokia1, then create class Nokia2 and
# inherit all the methods from Nokia1 to Nokia2. Also, modify the required
# methods in Nokia2 and add a few additional methods as well. In the
# same way, you can create Nokia3 and Nokia4 as well.
class Nokia1:
    def features(self):
        return ["Call", "Text"]

class Nokia2(Nokia1):
    def features(self):
        return super().features() + ["Camera"]

class Nokia3(Nokia2):
    def features(self):
        return super().features() + ["Music Player"]

class Nokia4(Nokia3):
    def features(self):
        return super().features() + ["Internet Browser"]


nokia1 = Nokia1()
nokia2 = Nokia2()
nokia3 = Nokia3()
nokia4 = Nokia4()

print("Nokia1 features:", nokia1.features())
print("Nokia2 features:", nokia2.features())
print("Nokia3 features:", nokia3.features())
print("Nokia4 features:", nokia4.features())