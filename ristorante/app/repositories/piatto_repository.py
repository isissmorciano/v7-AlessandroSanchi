from app.db import get_db



def get_all_piatti():
    db = get_db()
    return db.execute('''
        SELECT p.*, c.nome AS categoria_nome
        FROM piatti p
        JOIN categorie c ON c.id = p.categoria_id
        ORDER BY c.nome, p.nome
    ''').fetchall()


def get_piatti_by_category(category_id):
    db = get_db()
    return db.execute('''
        SELECT p.*, c.nome AS categoria_nome
        FROM piatti p
        JOIN categorie c ON c.id = p.categoria_id
        WHERE p.categoria_id = ?
        ORDER BY p.nome
    ''', (category_id,)).fetchall()

def create_piatto(category_id, nome, prezzo):
    db = get_db()
    db.execute('INSERT INTO piatti (categoria_id, nome, prezzo) VALUES (?, ?, ?)',
               (category_id, nome, prezzo))
    db.commit()



def find_piatti_by_name(search_term):
    db = get_db()
    return db.execute('''
        SELECT p.*, c.nome AS categoria_nome
        FROM piatti p
        JOIN categorie c ON c.id = p.categoria_id
        WHERE LOWER(p.nome) LIKE LOWER(?)
        ORDER BY c.nome, p.nome
    ''', (f'%{search_term}%',)).fetchall()