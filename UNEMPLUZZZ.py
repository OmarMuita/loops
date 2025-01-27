class Employee:
    def _init_(self):
        print("Employe created")

    def _del_(self):
        print("Destructor called")

def Create_obj():
    print("Making object...")
    obj=Employee()
    print("Function end...")
    return obj
print("calling Create obj() function...")
obj=Create_obj()
print("Program end...")
