from setuptools import setup, find_packages

setup(
    name="treewe",
    version="0.0.1",
    author="rebase.energy",
    description="A Python library for energy prediction using decision trees.",
    packages=find_packages(),
    include_package_data=True,  # This ensures that data files are included
    package_data={
        'treen': ['data/*.csv'],  # Specify the file types to include
    },
    install_requires=[
    'EnergyDataModel>=0.0.1',  # Ensure you specify the correct version of enerflow
    'enflow>=0.0.1',  # Ensure you specify the correct version of enerflow
    'pvlib',
    'shap>=0.39.0',
    'lightgbm>=3.3.0',
    'xgboost>=1.5.0',
    'catboost>=0.26',
    'pandas>=1.0.0',  # If your project uses pandas
    'numpy>=1.19.0',  # If you use NumPy
    'scikit-learn>=0.24.0'],
    python_requires='>=3.7',  # Specify the minimum Python version
)
