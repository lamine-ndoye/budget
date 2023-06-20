# app.py
import sqlite3

print("Application de Gestion de budget avec Python et Sqlite3")

with sqlite3.connect("budget.db") as connection:
    cursor = connection.cursor()


def create_table():
    cursor.execute(
        "CREATE TABLE montant_ver (id INTEGER PRIMARY KEY AUTOINCREMENT,montant INTEGER, unite TEXT)"
        "CREATE TABLE depenses (id INTEGER PRIMARY KEY AUTOINCREMENT,montant INTEGER, unite TEXT)"
        "CREATE TABLE revenues (id INTEGER PRIMARY KEY AUTOINCREMENT,montant INTEGER, unite TEXT)"
        )


def ajouter_contacte():
    cursor.execute(
        "INSERT INTO client(nomComplet, email, telephone) VALUES('Lamine Ndoye', 'lamine@gmail.com', '773864835')")
    cursor.execute(
        "INSERT INTO client(nomComplet, email, telephone) VALUES('Mamy Ndiaye', 'mamy@gmail.com', '763647625')")
    cursor.execute(
        "INSERT INTO client(nomComplet, email, telephone) VALUES('mamadou DIOP', 'diop@gamil.com', '763547282')")
    cursor.execute(
        "INSERT INTO client(nomComplet, email, telephone) VALUES('mamadou seye', 'mamadou@gamil.com', '763887243')")
    cursor.execute(
        "INSERT INTO client(nomComplet, email, telephone) VALUES('yacine ndoye', 'ndoye@gamil.com', '763007282')")
    connection.commit()


def afficher_les_client():
    rows = cursor.execute("SELECT * FROM client").fetchall()
    print(rows)


def afficher_un_client():
    row = cursor.execute(
        "SELECT * FROM client WHERE id = 1").fetchone()
    print(row)


def supprimer_client():
    nomComplet = "Lamine Ndoye"
    cursor.execute(
        "DELETE FROM client WHERE nomComplet = ?",
        (nomComplet,)
    )
    connection.commit()


def modifier_client():
    nouveau_email = "ndoye@gmail.com"
    ancien_email = "lamine@gmail.com"
    cursor.execute(
        "UPDATE client SET email = ? WHERE email = ?",
        (nouveau_email, ancien_email)
    )
    connection.commit()