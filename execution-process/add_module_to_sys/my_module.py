import sys
boolean = "my_module" in sys.modules
print(f"In my_module. {boolean}")


'''
Steps: 
1. Search for modules (builtin modules, sys.modules, and directories listed in sys.path)
2. Load bytecode of the module, if the module is not compiled or the source has been modified 
since last compilation, Python interpreter will compile the module
3. Add the module to `sys.modules`
4. Execute the module
'''