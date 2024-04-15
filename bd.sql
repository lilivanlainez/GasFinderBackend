-- Autor: Maynol Fabricio DÍaz Sarmiento
-- Fecha: [22:41]

-- Creación de la base de datos GasFinderDB si no existe
CREATE DATABASE IF NOT EXISTS GasFinderDB;

-- Selección de la base de datos GasFinderDB
USE GasFinderDB;

-- Tabla para los usuarios
CREATE TABLE IF NOT EXISTS Usuarios (
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    nombre_completo VARCHAR(255) NOT NULL,
    nombre_usuario VARCHAR(255) NOT NULL UNIQUE,
    correo_electronico VARCHAR(255) NOT NULL UNIQUE,
    contraseña VARCHAR(255) NOT NULL -- Debería ser un hash de la contraseña, no la contraseña en texto plano
);

-- Tabla para las estaciones de servicio
CREATE TABLE IF NOT EXISTS Estaciones (
    id_estacion INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255),
    ubicacion VARCHAR(255),
    disponible BOOLEAN NOT NULL DEFAULT TRUE -- Este campo correspondería al "Disponible"
);

-- Tabla para los precios de los combustibles
CREATE TABLE PreciosCombustible (
    id_PrecioCombustible INT AUTO_INCREMENT PRIMARY KEY,
    estacion_id INT NOT NULL,
    tipo_combustible VARCHAR(255) NOT NULL,
    precio DECIMAL(5, 2) NOT NULL,
    FOREIGN KEY (estacion_id) REFERENCES Estaciones(id_estacion) ON DELETE CASCADE
);


-- Tabla para autenticación con proveedores externos (por ejemplo, Google)
CREATE TABLE IF NOT EXISTS ProveedoresOAuth (
    id_ProveedorAuth INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT NOT NULL,
    nombre_proveedor VARCHAR(255) NOT NULL,
    id_proveedor VARCHAR(255) NOT NULL,
    datos_proveedor TEXT, -- JSON con datos específicos del proveedor
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (usuario_id) REFERENCES Usuarios(id_usuario) ON DELETE CASCADE
);
