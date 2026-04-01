from app.db import get_db



def get_all_categories():
    db = get_db()
    return db.execute('SELECT * FROM categorie ORDER BY nome').fetchall()

def create_category(nome):
    db = get_db()
    db.execute('INSERT INTO categorie (nome) VALUES (?)', (nome,))
    db.commit()


def get_category_by_id(category_id):
    db = get_db()
    return db.execute('SELECT * FROM categorie WHERE id = ?', (category_id,)).fetchone()