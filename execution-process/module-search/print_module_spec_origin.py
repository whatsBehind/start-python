import importlib.util

module_name = "langchain"
module_spec = importlib.util.find_spec(module_name)
print(f"Origin of module [{module_name}]: [{module_spec.origin}]")