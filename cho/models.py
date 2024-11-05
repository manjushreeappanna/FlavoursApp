import sqlite3

class ChocolateHouseDB:
    def __init__(self, db_name="chocolate_house.db"):
        self.db_name = db_name
        self.connection = sqlite3.connect(self.db_name, check_same_thread=False)
        self.cursor = self.connection.cursor()
        
    def create_tables(self):
        """Create tables if they don't already exist."""
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS flavors (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                name TEXT NOT NULL,
                                description TEXT,
                                season TEXT NOT NULL)''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS ingredients (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                name TEXT NOT NULL,
                                stock_quantity INTEGER NOT NULL)''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS customer_feedback (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                flavor_id INTEGER NOT NULL,
                                suggestion TEXT,
                                allergy_concern TEXT,
                                FOREIGN KEY(flavor_id) REFERENCES flavors(id))''')
        self.connection.commit()

    def add_flavor(self, name, description, season):
        """Add a new seasonal flavor to the database."""
        self.cursor.execute('''INSERT INTO flavors (name, description, season) VALUES (?, ?, ?)''',
                            (name, description, season))
        self.connection.commit()

    def add_ingredient(self, name, stock_quantity):
        """Add a new ingredient to the inventory."""
        self.cursor.execute('''INSERT INTO ingredients (name, stock_quantity) VALUES (?, ?)''',
                            (name, stock_quantity))
        self.connection.commit()

    def add_customer_feedback(self, flavor_id, suggestion, allergy_concern):
        """Add customer feedback about a flavor."""
        self.cursor.execute('''INSERT INTO customer_feedback (flavor_id, suggestion, allergy_concern) 
                               VALUES (?, ?, ?)''', (flavor_id, suggestion, allergy_concern))
        self.connection.commit()

    def get_flavors(self):
        """Get all seasonal flavors."""
        self.cursor.execute("SELECT * FROM flavors")
        return self.cursor.fetchall()

    def get_ingredients(self):
        """Get all ingredients in inventory."""
        self.cursor.execute("SELECT * FROM ingredients")
        return self.cursor.fetchall()

    def get_customer_feedback(self):
        """Get all customer feedback."""
        self.cursor.execute("SELECT * FROM customer_feedback")
        return self.cursor.fetchall()

    def close(self):
        """Close the database connection."""
        self.connection.close()
