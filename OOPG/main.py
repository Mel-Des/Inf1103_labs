import json
import os

from product import Product
from inventory import Inventory

FILE_NAME = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "inventory.json"
)