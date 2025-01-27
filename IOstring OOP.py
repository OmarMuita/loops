class IOstring:


    def _init_(self): 
        self.str1=""

    def get_string(self):
        self.str1=input("Enter string:")

    def print_String(self):
        print("Result is:",self.str1.upper())
str1=IOstring()

str1.get_string()
str1.print_String()
