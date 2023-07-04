import importlib
import inspect

# Cover for existing method
def decotitle(method, line_code):
    def ret(*args):
        # add line code
        exec(line_code)
        ans = method(*args)
        if ans:
            return ans
    return ret

#Adds a line of code
def file_deco(file_name, line_code):
    classes = []
    allmethods = []
    allSignatures = []

    # Go over all the class
    for class_name, temp_class in inspect.getmembers(importlib.import_module(file_name), inspect.isclass):
        methods = []
        Signatures = []
        classes.append(temp_class)
    # Go over all the methods
        for method_name, temp_method in inspect.getmembers(temp_class, inspect.isfunction):
            methods.append(temp_method)
            Signatures.append(inspect.signature(temp_method))
            setattr(temp_class, method_name, decotitle(temp_method, line_code))
        allmethods.append(methods)
        allSignatures.append(Signatures)

    return classes, allmethods, allSignatures

# Error running method
def print_error (class_name,method_name):
    print(f"Error performing the function: {class_name} -->> {method_name}")

# Running examples on the methods in the class
def dothis (file_name, temp_class, methods , Signatures):

    try:
        exec(f"from {file_name} import {temp_class.__name__}")
    except:
        print("error with import file or class")
        exit(1)

    print(f"\nclass : {temp_class.__name__}")

    #Go over all the methods
    min_len = min(len(methods), len(Signatures))
    for i in range(min_len):
        temp_method = methods[i]
        temp_signature = Signatures[i]
        temp_signature = "("+str(temp_signature).strip("(self, ")

    # if __init__
        if temp_method.__name__ == "__init__":
            print(f"The variables for creating an object:{temp_signature}")
            valu = input(f"Please enter variables [ For example: 'idan',10  for (name,age) ] : ")
            try:
                exec(f"x = {temp_class.__name__} ({valu})")
                print("The object is created\n")
            except:
                print_error(temp_class.__name__,temp_method.__name__)

    # if __str__
        elif temp_method.__name__ == "__str__":
            try:
                print(f"__str__ methods:")
                exec(f"print(x)")
            except:
                print_error(temp_class.__name__,temp_method.__name__)

    # other methods
        else:
            print(f"methods:{temp_method.__name__} variables:{temp_signature}")
            valu = input(f"Please enter var (str with \"\")")
            try:
                exec(f"x.{temp_method.__name__}({valu})")
            except:
                print_error(temp_class.__name__,temp_method.__name__)

# Function for managing adding a line of code and displaying samples
def add_line_code():
    file_name = input("Please enter a Python file name: ")
    code_line = input("Please enter a Python code line: ")

    try :
    #Trying to add a line to the code
        classes, allmethods, allSignatures = file_deco(file_name, code_line)
    except:
        print("error with python file or code line")
        exit(1)

    #Go over all the classes in the file to run examples
    min_len = min(len(classes), len(allmethods), len(allSignatures))
    for x in range(min_len):
        temp_class = classes[x]
        methods = allmethods[x]
        Signatures = allSignatures[x]
    #Runs all methods in the class
        dothis(file_name, temp_class, methods, Signatures)


def main():
    add_line_code()

if __name__ == "__main__":
    main()
