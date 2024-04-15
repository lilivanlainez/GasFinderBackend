from fastapi import FastAPI, HTTPException
from pydantic import BaseModel # type: ignore
import mysql.connector # type: ignore

# Definir la configuración de la base de datos
db_config = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'database': 'GasFinderDB'  # Nombre de la base de datos
}

# Inicializar la aplicación FastAPI
app = FastAPI()
#---------------------Usuarios-------------------------------------
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
# Ruta para eliminar un usuario por su ID
@app.delete("/usuarios/{usuario_id}")
def eliminar_usuario(usuario_id: int):
    connection = connect_to_database()
    if connection:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM Usuarios WHERE id_usuario = %s", (usuario_id,))
        connection.commit()
        cursor.close()
        connection.close()
        return {"mensaje": "Usuario eliminado correctamente"}
    else:
        raise HTTPException(status_code=500, detail="Error al conectar a la base de datos")
#-------------------------Estaciones de servicio---------------------------------------------
# Obtener todas las estaciones de servicio de la base de datos
class Estacion(BaseModel):
    id_estacion: int
    nombre: str
    ubicacion: str
    disponible: bool

def get_estaciones():
    connection = connect_to_database()
    if connection:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Estaciones")
        estaciones = cursor.fetchall()
        cursor.close()
        connection.close()
        return estaciones
    else:
        return []

# Ruta para obtener todas las estaciones de servicio
@app.get("/estaciones/")
def obtener_estaciones():
    estaciones = get_estaciones()
    if estaciones:
        return estaciones
    else:
        raise HTTPException(status_code=404, detail="No se encontraron estaciones de servicio")

# Ruta para obtener una estación de servicio por su ID
@app.get("/estaciones/{estacion_id}")
def obtener_estacion(estacion_id: int):
    connection = connect_to_database()
    if connection:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Estaciones WHERE id_estacion = %s", (estacion_id,))
        estacion = cursor.fetchone()
        cursor.close()
        connection.close()
        if estacion:
            return estacion
        else:
            raise HTTPException(status_code=404, detail="Estación de servicio no encontrada")
    else:
        raise HTTPException(status_code=500, detail="Error al conectar a la base de datos")

# Ruta para crear una nueva estación de servicio
@app.post("/estaciones/")
def crear_estacion(estacion: Estacion):
    connection = connect_to_database()
    if connection:
        cursor = connection.cursor()
        cursor.execute("""
            INSERT INTO Estaciones (nombre, ubicacion, disponible)
            VALUES (%s, %s, %s)
        """, (estacion.nombre, estacion.ubicacion, estacion.disponible))
        connection.commit()
        cursor.close()
        connection.close()
        return {"mensaje": "Estación de servicio creada correctamente"}
    else:
        raise HTTPException(status_code=500, detail="Error al conectar a la base de datos")

# Ruta para eliminar una estación de servicio por su ID
@app.delete("/estaciones/{estacion_id}")
def eliminar_estacion(estacion_id: int):
    connection = connect_to_database()
    if connection:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM Estaciones WHERE id_estacion = %s", (estacion_id,))
        connection.commit()
        cursor.close()
        connection.close()
        return {"mensaje": "Estación de servicio eliminada correctamente"}
    else:
        raise HTTPException(status_code=500, detail="Error al conectar a la base de datos")
    #------------PreciosCombustible---------------------------
    # Modelo Pydantic para la tabla PreciosCombustible
class PrecioCombustible(BaseModel):
    id_PrecioCombustible: int
    estacion_id: int
    tipo_combustible: str
    precio: float

# Conexión a la base de datos MySQL
def connect_to_database():
    try:
        connection = mysql.connector.connect(**db_config)
        return connection
    except mysql.connector.Error as error:
        print("Error al conectar a la base de datos:", error)
        return None

# Obtener todos los precios de combustible de la base de datos
def get_precios_combustible():
    connection = connect_to_database()
    if connection:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM PreciosCombustible")
        precios_combustible = cursor.fetchall()
        cursor.close()
        connection.close()
        return precios_combustible
    else:
        return []

# Ruta para obtener todos los precios de combustible
@app.get("/precios_combustible/")
def obtener_precios_combustible():
    precios_combustible = get_precios_combustible()
    if precios_combustible:
        return precios_combustible
    else:
        raise HTTPException(status_code=404, detail="No se encontraron precios de combustible")

# Ruta para obtener un precio de combustible por su ID
@app.get("/precios_combustible/{precio_combustible_id}")
def obtener_precio_combustible(precio_combustible_id: int):
    connection = connect_to_database()
    if connection:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM PreciosCombustible WHERE id_PrecioCombustible = %s", (precio_combustible_id,))
        precio_combustible = cursor.fetchone()
        cursor.close()
        connection.close()
        if precio_combustible:
            return precio_combustible
        else:
            raise HTTPException(status_code=404, detail="Precio de combustible no encontrado")
    else:
        raise HTTPException(status_code=500, detail="Error al conectar a la base de datos")

# Ruta para crear un nuevo precio de combustible
@app.post("/precios_combustible/")
def crear_precio_combustible(precio_combustible: PrecioCombustible):
    connection = connect_to_database()
    if connection:
        cursor = connection.cursor()
        cursor.execute("""
            INSERT INTO PreciosCombustible (estacion_id, tipo_combustible, precio)
            VALUES (%s, %s, %s)
        """, (precio_combustible.estacion_id, precio_combustible.tipo_combustible, precio_combustible.precio))
        connection.commit()
        cursor.close()
        connection.close()
        return {"mensaje": "Precio de combustible creado correctamente"}
    else:
        raise HTTPException(status_code=500, detail="Error al conectar a la base de datos")

# Ruta para eliminar un precio de combustible por su ID
@app.delete("/precios_combustible/{precio_combustible_id}")
def eliminar_precio_combustible(precio_combustible_id: int):
    connection = connect_to_database()
    if connection:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM PreciosCombustible WHERE id_PrecioCombustible = %s", (precio_combustible_id,))
        connection.commit()
        cursor.close()
        connection.close()
        return {"mensaje": "Precio de combustible eliminado correctamente"}
    else:
        raise HTTPException(status_code=500, detail="Error al conectar a la base de datos")
#----------------ProveedoresOAuth-----------------------
# Modelo Pydantic para la tabla ProveedoresOAuth
class ProveedorOAuth(BaseModel):
    id_ProveedorAuth: int
    usuario_id: int
    nombre_proveedor: str
    id_proveedor: str
    datos_proveedor: str

# Conexión a la base de datos MySQL
def connect_to_database():
    try:
        connection = mysql.connector.connect(**db_config)
        return connection
    except mysql.connector.Error as error:
        print("Error al conectar a la base de datos:", error)
        return None

# Obtener todos los proveedores OAuth de la base de datos
def get_proveedores_oauth():
    connection = connect_to_database()
    if connection:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM ProveedoresOAuth")
        proveedores_oauth = cursor.fetchall()
        cursor.close()
        connection.close()
        return proveedores_oauth
    else:
        return []

# Ruta para obtener todos los proveedores OAuth
@app.get("/proveedores_oauth/")
def obtener_proveedores_oauth():
    proveedores_oauth = get_proveedores_oauth()
    if proveedores_oauth:
        return proveedores_oauth
    else:
        raise HTTPException(status_code=404, detail="No se encontraron proveedores OAuth")

# Ruta para obtener un proveedor OAuth por su ID
@app.get("/proveedores_oauth/{proveedor_oauth_id}")
def obtener_proveedor_oauth(proveedor_oauth_id: int):
    connection = connect_to_database()
    if connection:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM ProveedoresOAuth WHERE id_ProveedorAuth = %s", (proveedor_oauth_id,))
        proveedor_oauth = cursor.fetchone()
        cursor.close()
        connection.close()
        if proveedor_oauth:
            return proveedor_oauth
        else:
            raise HTTPException(status_code=404, detail="Proveedor OAuth no encontrado")
    else:
        raise HTTPException(status_code=500, detail="Error al conectar a la base de datos")

# Ruta para crear un nuevo proveedor OAuth
@app.post("/proveedores_oauth/")
def crear_proveedor_oauth(proveedor_oauth: ProveedorOAuth):
    connection = connect_to_database()
    if connection:
        cursor = connection.cursor()
        cursor.execute("""
            INSERT INTO ProveedoresOAuth (usuario_id, nombre_proveedor, id_proveedor, datos_proveedor)
            VALUES (%s, %s, %s, %s)
        """, (proveedor_oauth.usuario_id, proveedor_oauth.nombre_proveedor, proveedor_oauth.id_proveedor, proveedor_oauth.datos_proveedor))
        connection.commit()
        cursor.close()
        connection.close()
        return {"mensaje": "Proveedor OAuth creado correctamente"}
    else:
        raise HTTPException(status_code=500, detail="Error al conectar a la base de datos")

# Ruta para eliminar un proveedor OAuth por su ID
@app.delete("/proveedores_oauth/{proveedor_oauth_id}")
def eliminar_proveedor_oauth(proveedor_oauth_id: int):
    connection = connect_to_database()
    if connection:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM ProveedoresOAuth WHERE id_ProveedorAuth = %s", (proveedor_oauth_id,))
        connection.commit()
        cursor.close()
        connection.close()
        return {"mensaje": "Proveedor OAuth eliminado correctamente"}
    else:
        raise HTTPException(status_code=500, detail="Error al conectar a la base de datos")