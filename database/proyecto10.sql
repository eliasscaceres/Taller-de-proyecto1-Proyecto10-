-- phpMyAdmin SQL Dump
-- version 4.8.2
-- https://www.phpmyadmin.net/
--
-- Servidor: db
-- Tiempo de generación: 24-07-2018 a las 20:43:23
-- Versión del servidor: 5.7.22
-- Versión de PHP: 7.2.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "-03:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `samples`
--
CREATE DATABASE IF NOT EXISTS `proyecto10` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;
USE `proyecto10`;


-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `samples`
--

CREATE TABLE `events` (
  `id` int(11) NOT NULL,
  `semaphore_state` boolean NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `samples`
--
ALTER TABLE `events`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `samples`
--
ALTER TABLE `events`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
