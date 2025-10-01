from flask import Flask
from flask_mysqldb import MySQL
import os

app = Flask(__name__)

# MySQL Configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'pms'

mysql = MySQL(app)

def add_column():
    try:
        with app.app_context():
            cur = mysql.connection.cursor()
            # Vérifier si la colonne existe déjà
            cur.execute("SHOW COLUMNS FROM registered_doctors LIKE 'Google_Maps_URL'")
            result = cur.fetchone()
            
            if not result:
                # Ajouter la colonne si elle n'existe pas
                cur.execute("ALTER TABLE registered_doctors ADD COLUMN Google_Maps_URL VARCHAR(255) AFTER Clinic_Address")
                mysql.connection.commit()
                print("La colonne Google_Maps_URL a été ajoutée avec succès!")
            else:
                print("La colonne Google_Maps_URL existe déjà.")
            
            cur.close()
    except Exception as e:
        print(f"Erreur lors de l'ajout de la colonne: {str(e)}")

if __name__ == "__main__":
    add_column() 