'''
Both running script (the main program) and any imported modules
are compiled to bytecode before execution

When you execute a python script directly (e.g., `python3 my_script.py`), 
the Python interpreter first compiles the script into bytecode. The compilation
happens in memory, and typically, for the main script being executed directly,
the bytecode is not saved to disk

When a script imports modules, these modules are also compiled into bytecode 
if they haven't been compiled or the source has been modified since the last 
compilation. Unlike the main script, the bytecode of imported modules will 
be save to disk in `__pycache__` directories within the same directory as 
the module
'''