/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

CREATE TABLE `editoras` (
  `idtable1` int NOT NULL AUTO_INCREMENT,
  `nome_editora` varchar(45) NOT NULL,
  PRIMARY KEY (`idtable1`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `emprestimos` (
  `idemprestimos` int NOT NULL AUTO_INCREMENT,
  `dataemprestimo` date NOT NULL,
  `livro_idlivro` int NOT NULL,
  `pessoas_idpessoas` int NOT NULL,
  PRIMARY KEY (`idemprestimos`),
  KEY `fk_emprestimos_livro1_idx` (`livro_idlivro`),
  KEY `fk_emprestimos_pessoas1_idx` (`pessoas_idpessoas`),
  CONSTRAINT `fk_emprestimos_livro1` FOREIGN KEY (`livro_idlivro`) REFERENCES `livro` (`idlivro`),
  CONSTRAINT `fk_emprestimos_pessoas1` FOREIGN KEY (`pessoas_idpessoas`) REFERENCES `pessoas` (`idpessoas`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `livro` (
  `idlivro` int NOT NULL AUTO_INCREMENT,
  `titulo` varchar(45) NOT NULL,
  `autor` varchar(45) NOT NULL,
  `editoras_idtable1` int NOT NULL,
  PRIMARY KEY (`idlivro`),
  KEY `fk_livro_editoras1_idx` (`editoras_idtable1`),
  CONSTRAINT `fk_livro_editoras1` FOREIGN KEY (`editoras_idtable1`) REFERENCES `editoras` (`idtable1`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `pessoas` (
  `idpessoas` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(45) DEFAULT NULL,
  `telefone` varchar(45) DEFAULT NULL,
  `email` varchar(45) DEFAULT NULL,
  `endereco` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idpessoas`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `editoras` (`idtable1`, `nome_editora`) VALUES
(1, 'Editora 1');
INSERT INTO `editoras` (`idtable1`, `nome_editora`) VALUES
(2, 'Editora 2');
INSERT INTO `editoras` (`idtable1`, `nome_editora`) VALUES
(3, 'Editora 3');
INSERT INTO `editoras` (`idtable1`, `nome_editora`) VALUES
(4, 'Editora 4'),
(5, 'Editora 5'),
(6, 'Editora 6');

INSERT INTO `emprestimos` (`idemprestimos`, `dataemprestimo`, `livro_idlivro`, `pessoas_idpessoas`) VALUES
(1, '2022-10-13', 1, 2);
INSERT INTO `emprestimos` (`idemprestimos`, `dataemprestimo`, `livro_idlivro`, `pessoas_idpessoas`) VALUES
(5, '2023-11-21', 3, 3);
INSERT INTO `emprestimos` (`idemprestimos`, `dataemprestimo`, `livro_idlivro`, `pessoas_idpessoas`) VALUES
(6, '2023-11-21', 1, 1);
INSERT INTO `emprestimos` (`idemprestimos`, `dataemprestimo`, `livro_idlivro`, `pessoas_idpessoas`) VALUES
(7, '2023-10-21', 1, 1);

INSERT INTO `livro` (`idlivro`, `titulo`, `autor`, `editoras_idtable1`) VALUES
(1, 'Reuri Poder', 'Juscelino Kubitschec', 1);
INSERT INTO `livro` (`idlivro`, `titulo`, `autor`, `editoras_idtable1`) VALUES
(2, 'Shrek versão livro', 'Autor de shrek livro', 4);
INSERT INTO `livro` (`idlivro`, `titulo`, `autor`, `editoras_idtable1`) VALUES
(3, 'Shrek 2 versão livro', 'Autor de shrek 2 livro', 2);
INSERT INTO `livro` (`idlivro`, `titulo`, `autor`, `editoras_idtable1`) VALUES
(4, 'Shrek 3 versão livro', 'Autor de shrek 3 livro', 2),
(5, 'Shrek 4 versão livro', 'Autor de shrek 4 livro', 2),
(6, 'Biblia', 'Enviado de Deux', 5),
(7, 'Biblia 2', 'Outro enviado de Deux', 5);

INSERT INTO `pessoas` (`idpessoas`, `nome`, `telefone`, `email`, `endereco`) VALUES
(1, 'Eudes Branco', '4002-8922', 'emailtop@hotwheels.com', 'casa da eudes');
INSERT INTO `pessoas` (`idpessoas`, `nome`, `telefone`, `email`, `endereco`) VALUES
(2, 'Eudes Verde', '4002-0000', 'emailmasseira@hotwheels.com', 'casa da eudes azul');
INSERT INTO `pessoas` (`idpessoas`, `nome`, `telefone`, `email`, `endereco`) VALUES
(3, 'Marcus', '190', 'hugonalta@hotmail.com', 'minha casa');


/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;