import sqlite3

class SQLiteCLI:
    """
    """
    def __init__(self, path_to_sqlite_db):
        """
        """
        self.path_to_sqlite_db = path_to_sqlite_db
        self.conn = sqlite3.connect(self.path_to_sqlite_db)
        self.table_names = self.get_table_names()
    
    def get_table_names(self):
        sql = """
        SELECT 
            name
        FROM 
            sqlite_master 
        WHERE 
            type ='table' AND 
            name NOT LIKE 'sqlite_%'
        """
        curr = self.conn.cursor()
        curr.execute(sql)
        table_names = [row[0] for row in curr.fetchall()]
        curr.close()
        return table_names

    def get_column_details_for_table(self, table_name):
        """
        """
        sql = "PRAGMA table_info('%s')" % table_name
        if table_name not in self.table_names:
            return [(),]
        curr = self.conn.cursor()
        curr.execute(sql)
        column_details_for_table = curr.fetchall()
        return column_details_for_table

    def __del__(self):
        self.conn.close()

if __name__ == '__main__':
    sql_cli = SQLiteCLI('genes.db')
    print(sql_cli.get_table_names())
    print(sql_cli.get_column_details_for_table('hug_genes'))
    del sql_cli