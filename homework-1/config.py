import pathlib

ROOT_DIR = pathlib.Path(__file__).parent
CUSTOMERS = pathlib.Path(ROOT_DIR, 'north_data', 'customers_data.csv')
EMPLOYEES = pathlib.Path(ROOT_DIR, 'north_data', 'employees_data.csv')
ORDERS = pathlib.Path(ROOT_DIR, 'north_data', 'orders_data.csv')
