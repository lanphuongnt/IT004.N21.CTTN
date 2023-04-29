-- MySQL dump 10.13  Distrib 5.7.17, for Win64 (x86_64)
--
-- Host: localhost    Database: truonghoc
-- ------------------------------------------------------
-- Server version	5.7.20-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
DROP DATABASE IF EXISTS `truonghoc`/* DROP DATABASE IF EXISTS */; 
CREATE DATABASE IF NOT EXISTS `truonghoc` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `truonghoc`;
--
-- Table structure for table `so`
--

DROP TABLE IF EXISTS `so`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `so` (
  `idso` tinyint(2) NOT NULL,
  `tenso` varchar(50) NOT NULL,
  PRIMARY KEY (`idso`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `phong`
--

DROP TABLE IF EXISTS `phong`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `phong` (
  `idphg` tinyint(2) NOT NULL,
  `tenphong` varchar(50) NOT NULL,
  `idso` tinyint(2) NOT NULL,
  PRIMARY KEY (`idphg`, `idso`),
  CONSTRAINT `PHONG-SO` FOREIGN KEY (`idso`) REFERENCES `so` (`idso`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `loaihinh`
--

DROP TABLE IF EXISTS `loaihinh`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `loaihinh` (
  `idlh` tinyint(2) NOT NULL,
  `tenlh` varchar(50) NOT NULL,
  PRIMARY KEY (`idlh`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `cap`
--

DROP TABLE IF EXISTS `cap`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cap` (
  `idcap` varchar(4) NOT NULL,
  `tencap` varchar(50) NOT NULL,
  PRIMARY KEY (`idcap`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `loaitruong`
--

DROP TABLE IF EXISTS `loaitruong`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `loaitruong` (
  `idlt` tinyint(2) NOT NULL,
  `tenlt` varchar(50) NOT NULL,
  PRIMARY KEY (`idlt`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;


--
-- Table structure for table `truong`
--

DROP TABLE IF EXISTS `truong`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `truong` (
  `matrg` varchar(20) NOT NULL,
  `tentrg` varchar(100) NOT NULL,
  `dchi` varchar(300) DEFAULT NULL,
  `idso` tinyint(2) DEFAULT NULL,
  `idphg` tinyint(2) DEFAULT NULL,
  `idlh` tinyint(2) DEFAULT NULL,
  `idlt` tinyint(2) DEFAULT NULL,
  `idcap` varchar(4) NOT NULL,
  PRIMARY KEY (`matrg`, `idcap`),
  FOREIGN KEY (`idso`) REFERENCES `so` (`idso`),
  FOREIGN KEY (`idphg`) REFERENCES `phong` (`idphg`),
  FOREIGN KEY (`idlh`) REFERENCES `loaihinh` (`idlh`),
  FOREIGN KEY (`idlt`) REFERENCES `loaitruong` (`idlt`),
  FOREIGN KEY (`idcap`) REFERENCES `cap` (`idcap`) 
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;


/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-27-04 