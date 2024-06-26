import sqlite3

rutaBD = "C:\\Users\\ARCADE_PC_01\\Documents\\DUOC\\REDES_VIRTUALIZADAS\\ET\\ITEM03\\EJ02_ITEM03\\envi\\instance\\usuarios.db"

def crearBD():
        conn = sqlite3.connect(rutaBD)
        cursor = conn.cursor()
        cursor.execute("""CREATE TABLE usuarios (nombre text, rut integer)""")
        conn.commit()
        conn.close()

def AgregarUser():
        conn = sqlite3.connect(rutaBD)
        cursor = conn.cursor()
        data = [
            ("Ignacio Jorquera", 176665785),
            ("Oscar Bravo", 173791720),
            ("Yeremy Gatica", 202188397)
            ("Jordan Gonzalez", 204017123)
        ]
        cursor.executemany("""INSERT INTO usuarios VALUES (?,?,)""",data)
        conn.commit()
        conn.close()

if __name__ == "__main__":
    crearBD()
    AgregarUser()


