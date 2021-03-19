import sqlite3

class DataStoreSQLite:

    def __init__(self, site_config, out_filename):
        self.site_config = site_config
        self.out_filename = out_filename
        self.connection =  sqlite3.connect(out_filename)

        # Create table
        cur = self.connection.cursor()
        cur.execute('''CREATE TABLE event
                       (title text, description text)''')
        self.connection.commit()

    def store(self, event):
        cur = self.connection.cursor()
        insert_data = [
            event.title,
            event.description,
        ]
        cur.execute("INSERT INTO event (title, description) VALUES (?, ?)", insert_data)
        self.connection.commit()

