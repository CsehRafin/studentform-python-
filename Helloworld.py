class studentform:
    formtype = "studentform"
    def PPRD(self):
        print(f"name: {self.name}")
        print(f"age: {self.age}")
        print(f"E-mail: {self.email}")
        print(f"Linkedin: {self.linkedin}")
        
print("when filling form don't leave name and age blank because it causes error")

def studentformfill():
    std = studentform()
    std.name = input("Name: ")
    std.age = int(input("Age: "))
    if (std.age<18):
        print("You can't be student of this College")
        exit()
    else:
        pass
    std.email = input("E-mail: ")
    std.linkedin = input("Linkedin:")
    return std

std = studentformfill()
srd = std.PPRD()

print(f"""
Hello, {std.name}
age {std.age}
you have been selected in MOCT college UK
Thanks for reading {std.name}
-Regards Vera davidsoma """)




