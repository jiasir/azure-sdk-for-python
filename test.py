__author__ = 'Taio'

import os
from azure.storage import TableService

print os.environ.get('AZURE_STORAGE_ACCOUNT')
print os.environ.get('AZURE_STORAGE_ACCESS_KEY')
ts = TableService()
ts.create_table('shangpinimages')