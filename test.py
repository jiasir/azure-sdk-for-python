__author__ = 'Taio'


from azure.storage import TableService

ts = TableService(host_base='.table.core.windows.cn')
ts.create_table('shangpinimages')