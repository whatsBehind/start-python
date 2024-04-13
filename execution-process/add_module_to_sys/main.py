import sys

boolean = "my_module" in sys.modules
print(f"In main, before import. {boolean}")

import my_module

boolean = "my_module, after import" in sys.modules
print(f"In main. {boolean}")