show DATABASES

CREATE DATABASE data_cars

use data_cars

show tables

CREATE TABLE marca (
    marca_id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL
);


CREATE TABLE carro (
    carro_id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    ano INT,
    preco DECIMAL(10, 2),
    marca_id INT,
    FOREIGN KEY (marca_id) REFERENCES marca(marca_id)
);

INSERT INTO marca (nome) VALUES ('Toyota');

INSERT INTO marca (nome) VALUES ('Honda');


INSERT INTO marca (nome) VALUES ('Ford');


INSERT INTO marca (nome) VALUES ('Chevrolet');

INSERT INTO carro (nome, ano, preco, marca_id) VALUES ('Corolla', 2022, 35000.00, 1);

INSERT INTO carro (nome, ano, preco, marca_id) VALUES ('Civic', 2021, 32000.00, 2);

INSERT INTO carro (nome, ano, preco, marca_id) VALUES ('Accord', 2020, 29000.00, 2);

INSERT INTO carro (nome, ano, preco, marca_id) VALUES ('Focus', 2019, 25000.00, 3);

INSERT INTO carro (nome, ano, preco, marca_id) VALUES ('Fusion', 2020, 31000.00, 3);

INSERT INTO carro (nome, ano, preco, marca_id) VALUES ('Cruze', 2019, 27000.00, 4);

INSERT INTO carro (nome, ano, preco, marca_id) VALUES ('Malibu', 2021, 34000.00, 4);

select * from carro where marca_id = "1"