import sys

print(sys.path)

'''
Module search path

1. built-in module (`sys.builtin_module_names`)

2. `sys.modules` cache

3. Python Path (`sys.path`)

    a. The directory containing the running script(? how about nested path)
    b. The directories in PYTHONPATH environment variable(? how is it normally used)
    c. Standard library directories
    d. Site-package directories for third-party packages
'''