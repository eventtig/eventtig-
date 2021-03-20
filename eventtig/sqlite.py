import sqlite3

class DataStoreSQLite:

    def __init__(self, site_config, out_filename):
        self.site_config = site_config
        self.out_filename = out_filename
        self.connection =  sqlite3.connect(out_filename)

        # Create table
        cur = self.connection.cursor()
        cur.execute('''CREATE TABLE event (
            id TEXT PRIMARY KEY, 
            title text, 
            description text,
            start_year integer,
            start_month integer,
            start_day integer,
            start_hour integer,
            start_minute integer,
            start_epoch integer,
            end_year integer,
            end_month integer,
            end_day integer,
            end_hour integer,
            end_minute integer,
            end_epoch integer
            )'''
        )
        cur.execute('''CREATE TABLE tag (
            id TEXT PRIMARY KEY, 
            title text
            )'''
        )

        cur.execute('''CREATE TABLE event_has_tag (
            event_id TEXT, 
            tag_id TEXT,
            PRIMARY KEY(event_id, tag_id)
            )'''
        )

        self.connection.commit()

    def store_event(self, event):
        cur = self.connection.cursor()
        insert_data = [
            event.id,
            event.title,
            event.description,
            event.start_year,
            event.start_month,
            event.start_day,
            event.start_hour,
            event.start_minute,
            event.get_start_epoch(),
            event.end_year,
            event.end_month,
            event.end_day,
            event.end_hour,
            event.end_minute,
            event.get_end_epoch()
        ]
        cur.execute(
            """INSERT INTO event (
            id, title, description,
            start_year, start_month,start_day,start_hour,start_minute,start_epoch,
            end_year,end_month,end_day,end_hour,end_minute,end_epoch
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            insert_data
        )
        for tag_id in event.tag_ids:
            cur.execute("INSERT INTO event_has_tag (event_id, tag_id) VALUES (?, ?)", [ event.id, tag_id ])
        self.connection.commit()


    def store_tag(self, tag):
        cur = self.connection.cursor()
        insert_data = [
            tag.id,
            tag.title,
        ]
        cur.execute("INSERT INTO tag (id, title) VALUES (?, ?)", insert_data)
        self.connection.commit()

