import sqlite3

def initialize_database(db_name="data/compound_data.db"):
    """
    Initialize the SQLite database.
    """
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Existing Compounds table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Compounds (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            smiles TEXT,
            molecular_weight REAL
        )
    ''')

    # New UnifiedCompounds table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS UnifiedCompounds (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            compound_name TEXT NOT NULL,
            source TEXT NOT NULL,
            type TEXT NOT NULL,
            value TEXT NOT NULL
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
    print(f"Data for compound '{name}' saved successfully.")
    conn.close()


import sqlite3

def save_list(compound_name, results, db_name="data/compound_data.db"):
    """
    Save compound data into the UnifiedCompounds table in the database.
    """
    #try:
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Insert data into the UnifiedCompounds table
    for result in results:
        cursor.execute('''
            INSERT INTO UnifiedCompounds (compound_name, source, type, value)
            VALUES (?, ?, ?, ?)
        ''', (result["compound_name"], result["source"], result["type"], result["value"]))

    conn.commit()
    print(f"Data for compound '{compound_name}' saved successfully.")
    #except Exception as e:
    #    print(f"An error occurred while saving data for '{compound_name}': {e}")
    #finally:
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
    print(f"Data for compound '{compound_id}' saved successfully.")
    conn.close()

if __name__ == "__main__":
    initialize_database()
    save_compound("Aspirin", "CC(=O)OC1=CC=CC=C1C(=O)O", 180.16)
    sample_results = [
        {"compound_name": "Aspirin", "source": "PubMed", "type": "DOI", "value": "10.1234/abc123"},
        {"compound_name": "Aspirin", "source": "ChEMBL", "type": "Synonym", "value": "Acetylsalicylic Acid"}
    ]
    save_list("Aspirin", sample_results)
    save_document(1, "Aspirin inhibits COX enzymes.", 0.95)
