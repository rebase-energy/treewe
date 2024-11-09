import os
import importlib


def list_problems():
    # Get the directory where problem files are stored
    problems_dir = os.path.join(os.path.dirname(__file__), 'problems')

    # List all Python files in the problems directory
    problems = [
        os.path.splitext(file)[0].replace("_", "-")
        for file in os.listdir(problems_dir)
        if file.endswith(".py") and file != "__init__.py"
    ]
    return problems


def load_problem(problem_name):
    module_name = f"treewe.problems.{problem_name.replace('-', '_')}"
    try:
        # Dynamically import the module
        module = importlib.import_module(module_name)
        # Get the problem name 
        dataset = getattr(module, "dataset")
        env = getattr(module, "env")
        obj = getattr(module, "obj")
        #problem = getattr(module, "problem")
        return dataset, env, obj
    except (ImportError, AttributeError) as e:
        raise ValueError(f"Could not load problem '{problem_name}': {e}")

def load_dataset(problem_name):
    module_name = f"treewe.problems.{problem_name.replace('-', '_')}"
    try:
        # Dynamically import the module
        module = importlib.import_module(module_name)
        # Get the problem name 
        dataset = getattr(module, "dataset")
        return dataset
    except (ImportError, AttributeError) as e:
        raise ValueError(f"Could not load dataset '{problem_name}': {e}")