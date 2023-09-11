
from models.table import Table


class Order:
    def __init__(self):
        self.tables = {}

    def get_table(self, table_number):
        return self.tables[table_number]

    def get_all_tables(self):
        return list(self.tables.values())

    def add_table(self,table_number,items):
        if table_number not in self.tables:
            table = Table(table_number)
            table.add_items(items)
            self.tables[table_number] = table
        else:
            table = self.get_table(table_number)
            table.add_items(items)

    def remove_table(self,table_number):

         return self.tables.pop(table_number, None)
    