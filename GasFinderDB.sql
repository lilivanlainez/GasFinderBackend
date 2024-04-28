-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Apr 28, 2024 at 03:41 AM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `GasFinderDB`
--

-- --------------------------------------------------------

--
-- Table structure for table `Estaciones`
--

CREATE TABLE `Estaciones` (
  `id_estacion` int(11) NOT NULL,
  `nombre` varchar(255) DEFAULT NULL,
  `ubicacion` varchar(255) DEFAULT NULL,
  `disponible` tinyint(1) NOT NULL DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `Estaciones`
--

INSERT INTO `Estaciones` (`id_estacion`, `nombre`, `ubicacion`, `disponible`) VALUES
(3, 'Puma La Gloria', 'blv constitucion', 1);

-- --------------------------------------------------------

--
-- Table structure for table `PreciosCombustible`
--

CREATE TABLE `PreciosCombustible` (
  `id_PrecioCombustible` int(11) NOT NULL,
  `estacion_id` int(11) NOT NULL,
  `tipo_combustible` varchar(255) NOT NULL,
  `precio` decimal(5,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `ProveedoresOAuth`
--

CREATE TABLE `ProveedoresOAuth` (
  `id_ProveedorAuth` int(11) NOT NULL,
  `usuario_id` int(11) NOT NULL,
  `nombre_proveedor` varchar(255) NOT NULL,
  `id_proveedor` varchar(255) NOT NULL,
  `datos_proveedor` text DEFAULT NULL,
  `fecha_creacion` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `ProveedoresOAuth`
--

INSERT INTO `ProveedoresOAuth` (`id_ProveedorAuth`, `usuario_id`, `nombre_proveedor`, `id_proveedor`, `datos_proveedor`, `fecha_creacion`) VALUES
(1, 2, 'puma', '789', 'eble', '2024-04-15 21:28:45');

-- --------------------------------------------------------

--
-- Table structure for table `Usuarios`
--

CREATE TABLE `Usuarios` (
  `id_usuario` int(11) NOT NULL,
  `nombre_completo` varchar(255) NOT NULL,
  `nombre_usuario` varchar(255) NOT NULL,
  `correo_electronico` varchar(255) NOT NULL,
  `contraseña` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `Usuarios`
--

INSERT INTO `Usuarios` (`id_usuario`, `nombre_completo`, `nombre_usuario`, `correo_electronico`, `contraseña`) VALUES
(2, 'Ivan Lainez', 'Nelson Colorado', 'ivan@ivan.com', '1234');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `Estaciones`
--
ALTER TABLE `Estaciones`
  ADD PRIMARY KEY (`id_estacion`);

--
-- Indexes for table `PreciosCombustible`
--
ALTER TABLE `PreciosCombustible`
  ADD PRIMARY KEY (`id_PrecioCombustible`),
  ADD KEY `estacion_id` (`estacion_id`);

--
-- Indexes for table `ProveedoresOAuth`
--
ALTER TABLE `ProveedoresOAuth`
  ADD PRIMARY KEY (`id_ProveedorAuth`),
  ADD KEY `usuario_id` (`usuario_id`);

--
-- Indexes for table `Usuarios`
--
ALTER TABLE `Usuarios`
  ADD PRIMARY KEY (`id_usuario`),
  ADD UNIQUE KEY `nombre_usuario` (`nombre_usuario`),
  ADD UNIQUE KEY `correo_electronico` (`correo_electronico`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `Estaciones`
--
ALTER TABLE `Estaciones`
  MODIFY `id_estacion` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `PreciosCombustible`
--
ALTER TABLE `PreciosCombustible`
  MODIFY `id_PrecioCombustible` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `ProveedoresOAuth`
--
ALTER TABLE `ProveedoresOAuth`
  MODIFY `id_ProveedorAuth` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `Usuarios`
--
ALTER TABLE `Usuarios`
  MODIFY `id_usuario` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `PreciosCombustible`
--
ALTER TABLE `PreciosCombustible`
  ADD CONSTRAINT `precioscombustible_ibfk_1` FOREIGN KEY (`estacion_id`) REFERENCES `Estaciones` (`id_estacion`) ON DELETE CASCADE;

--
-- Constraints for table `ProveedoresOAuth`
--
ALTER TABLE `ProveedoresOAuth`
  ADD CONSTRAINT `proveedoresoauth_ibfk_1` FOREIGN KEY (`usuario_id`) REFERENCES `Usuarios` (`id_usuario`) ON DELETE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
