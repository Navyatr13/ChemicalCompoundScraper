import sqlite3


def initialize_database(db_name="data/compound_data.db"):
    """
    Initialize the SQLite database.
    """
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Compounds (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            smiles TEXT,
            molecular_weight REAL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Documents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            compound_id INTEGER,
            content TEXT,
            score REAL,
            FOREIGN KEY (compound_id) REFERENCES Compounds(id)
        )
    ''')
    conn.commit()
    conn.close()


def save_compound(name, smiles, molecular_weight, db_name="data/compound_data.db"):
    """
    Save a compound into the database.
    """
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Compounds (name, smiles, molecular_weight) VALUES (?, ?, ?)",
                   (name, smiles, molecular_weight))
    conn.commit()
    conn.close()


def save_document(compound_id, content, score, db_name="data/compound_data.db"):
    """
    Save a document into the database.
    """
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Documents (compound_id, content, score) VALUES (?, ?, ?)",
                   (compound_id, content, score))
    conn.commit()
    conn.close()
