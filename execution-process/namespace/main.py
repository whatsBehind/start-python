string = "global namespace"

def my_func():
    string = "local namespace of my_func"
    print(string)

    def nested_func():
        string = "local namespace of nested_func"
        print(string)

    nested_func()

my_func()
print(string)