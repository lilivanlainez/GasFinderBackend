from fastapi import FastAPI, HTTPException
from pydantic import BaseModel # type: ignore
import mysql.connector # type: ignore

# Definir la configuración de la base de datos
db_config = {
    'user': 'usuario_mysql',
    'password': 'contraseña_mysql',
    'host': 'localhost',
    'database': 'GasFinderDB'  # Nombre de la base de datos
}

# Inicializar la aplicación FastAPI
app = FastAPI()

# Modelo Pydantic para la tabla de Usuarios
class Usuario(BaseModel):
    id_usuario: int
    nombre_completo: str
    nombre_usuario: str
    correo_electronico: str
    contraseña: str

# Conexión a la base de datos MySQL
def connect_to_database():
    try:
        connection = mysql.connector.connect(**db_config)
        return connection
    except mysql.connector.Error as error:
        print("Error al conectar a la base de datos:", error)
        return None

# Obtener todos los usuarios de la base de datos
def get_usuarios():
    connection = connect_to_database()
    if connection:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Usuarios")
        usuarios = cursor.fetchall()
        cursor.close()
        connection.close()
        return usuarios
    else:
        return []

@app.get("/")
def index():
    return "hola mundo"

# Ruta para obtener todos los usuarios
@app.get("/usuarios/")
def obtener_usuarios():
    usuarios = get_usuarios()
    if usuarios:
        return usuarios
    else:
        raise HTTPException(status_code=404, detail="No se encontraron usuarios")

# Ruta para obtener un usuario por su ID
@app.get("/usuarios/{usuario_id}")
def obtener_usuario(usuario_id: int):
    connection = connect_to_database()
    if connection:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Usuarios WHERE id_usuario = %s", (usuario_id,))
        usuario = cursor.fetchone()
        cursor.close()
        connection.close()
        if usuario:
            return usuario
        else:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
    else:
        raise HTTPException(status_code=500, detail="Error al conectar a la base de datos")

# Ruta para crear un nuevo usuario
@app.post("/usuarios/")
def crear_usuario(usuario: Usuario):
    connection = connect_to_database()
    if connection:
        cursor = connection.cursor()
        cursor.execute("""
            INSERT INTO Usuarios (nombre_completo, nombre_usuario, correo_electronico, contraseña)
            VALUES (%s, %s, %s, %s)
        """, (usuario.nombre_completo, usuario.nombre_usuario, usuario.correo_electronico, usuario.contraseña))
        connection.commit()
        cursor.close()
        connection.close()
        return {"mensaje": "Usuario creado correctamente"}
    else:
        raise HTTPException(status_code=500, detail="Error al conectar a la base de datos")
