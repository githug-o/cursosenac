/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

CREATE TABLE `categoria` (
  `idcategoria` int NOT NULL AUTO_INCREMENT,
  `categoria` varchar(45) NOT NULL,
  PRIMARY KEY (`idcategoria`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb3;

CREATE TABLE `cliente` (
  `idcliente` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(45) NOT NULL,
  `email` varchar(45) NOT NULL,
  `telefone` varchar(45) NOT NULL,
  `tipo` varchar(45) NOT NULL,
  `id_endereco` int NOT NULL,
  PRIMARY KEY (`idcliente`),
  KEY `fk_cliente_endereco1_idx` (`id_endereco`),
  CONSTRAINT `fk_cliente_endereco1` FOREIGN KEY (`id_endereco`) REFERENCES `endereco` (`idendereco`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb3;

CREATE TABLE `endereco` (
  `idendereco` int NOT NULL AUTO_INCREMENT,
  `cep` varchar(45) NOT NULL,
  `uf` varchar(45) NOT NULL,
  `cidade` varchar(45) NOT NULL,
  `bairro` varchar(45) NOT NULL,
  `rua` varchar(45) NOT NULL,
  `numero` varchar(45) NOT NULL,
  `complemento` varchar(45) NOT NULL,
  PRIMARY KEY (`idendereco`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb3;

CREATE TABLE `produto` (
  `idproduto` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(45) NOT NULL,
  `quantidade` int NOT NULL,
  `valor` decimal(6,0) NOT NULL,
  `frete` decimal(6,0) NOT NULL,
  `imposto1` decimal(6,0) NOT NULL,
  `imposto2` decimal(6,0) NOT NULL,
  `imposto3` decimal(6,0) NOT NULL,
  `valor_custo` decimal(6,0) NOT NULL,
  `valor_venda` decimal(6,0) NOT NULL,
  `id_fornecedor` int NOT NULL,
  `id_fabricante` int NOT NULL,
  `id_categoria` int NOT NULL,
  `lucro` decimal(6,0) NOT NULL,
  PRIMARY KEY (`idproduto`),
  KEY `fk_produto_cliente_idx` (`id_fornecedor`),
  KEY `fk_produto_cliente1_idx` (`id_fabricante`),
  KEY `fk_produto_categoria1_idx` (`id_categoria`),
  CONSTRAINT `fk_produto_categoria1` FOREIGN KEY (`id_categoria`) REFERENCES `categoria` (`idcategoria`),
  CONSTRAINT `fk_produto_cliente` FOREIGN KEY (`id_fornecedor`) REFERENCES `cliente` (`idcliente`),
  CONSTRAINT `fk_produto_cliente1` FOREIGN KEY (`id_fabricante`) REFERENCES `cliente` (`idcliente`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb3;

INSERT INTO `categoria` (`idcategoria`, `categoria`) VALUES
(11, 'Bebidas');
INSERT INTO `categoria` (`idcategoria`, `categoria`) VALUES
(12, 'Comidinhas');
INSERT INTO `categoria` (`idcategoria`, `categoria`) VALUES
(13, 'Tomperro');
INSERT INTO `categoria` (`idcategoria`, `categoria`) VALUES
(14, 'Miojo');

INSERT INTO `cliente` (`idcliente`, `nome`, `email`, `telefone`, `tipo`, `id_endereco`) VALUES
(12, 'nomeinsert', 'testeemail', 'teste telefone', '1', 11);
INSERT INTO `cliente` (`idcliente`, `nome`, `email`, `telefone`, `tipo`, `id_endereco`) VALUES
(13, 'nomeinsert', 'testeemail', 'teste telefone', '1', 11);
INSERT INTO `cliente` (`idcliente`, `nome`, `email`, `telefone`, `tipo`, `id_endereco`) VALUES
(14, 'nomeinsert', 'testeemail', 'teste telefone', '1', 11);
INSERT INTO `cliente` (`idcliente`, `nome`, `email`, `telefone`, `tipo`, `id_endereco`) VALUES
(16, 'nomeinsert', 'testeemail', 'teste telefone', '1', 11),
(17, 'nomeinsert', 'testeemail', 'teste telefone', '1', 11),
(18, 'nomeinsert', 'testeemail', 'teste telefone', '1', 11),
(19, 'nomesfsdfinsert', 'testeemail', 'teste telefone', '1', 11),
(20, 'nomesfsdfinsert', 'testeemail', 'teste telefone', '1', 11),
(21, 'fornecedor1', 'testeemail', 'telasjdi', '2', 12),
(22, 'fabricante', 'fabricantfabriquei', '4002-8922', '3', 13);

INSERT INTO `endereco` (`idendereco`, `cep`, `uf`, `cidade`, `bairro`, `rua`, `numero`, `complemento`) VALUES
(11, '770000', 'TO', 'Palmas', 'bairrotop', 'rua paia', '10', 'minha casa uai');
INSERT INTO `endereco` (`idendereco`, `cep`, `uf`, `cidade`, `bairro`, `rua`, `numero`, `complemento`) VALUES
(12, 'cepforn', 'RJ', 'Rio de Fevereiro', 'Indutrisal', 'rua paia', '1200', 'um fornecedor');
INSERT INTO `endereco` (`idendereco`, `cep`, `uf`, `cidade`, `bairro`, `rua`, `numero`, `complemento`) VALUES
(13, 'cepforn', 'RJ', 'Rio de Fevereiro', 'Indutrisal', 'rua paia', '1200', 'um fornecedor');

INSERT INTO `produto` (`idproduto`, `nome`, `quantidade`, `valor`, `frete`, `imposto1`, `imposto2`, `imposto3`, `valor_custo`, `valor_venda`, `id_fornecedor`, `id_fabricante`, `id_categoria`, `lucro`) VALUES
(1, 'Pizza', 10, 50, 30, 0, 0, 0, 120, 100, 21, 22, 12, 1051);



/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;