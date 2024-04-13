import sys
import json

# Extract module names
module_names = list(sys.modules.keys())

# Convert the list of module names to a JSON string
json_string = json.dumps(module_names, indent=4)

# Print the JSON string
print(json_string)
