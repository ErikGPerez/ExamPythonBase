# Note: the module name is psycopg, not psycopg3
import psycopg
class Connection:
    def __init__(self):
        #Program no connection desu
        self.conn = psycopg.connect("host=localhost port=5432 dbname=training user=postgres password=p@ssw0rd")