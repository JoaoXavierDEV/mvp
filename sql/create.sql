-- inscricoes definição

CREATE TABLE inscricoes
(
    id INTEGER NOT NULL,
    pessoa_id INTEGER NOT NULL,
    evento_id INTEGER NOT NULL,
    data DATETIME NOT NULL,
    email VARCHAR NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY(pessoa_id) REFERENCES pessoas (id),
    FOREIGN KEY(evento_id) REFERENCES eventos (id)
);

-- eventos definição

CREATE TABLE eventos
(
    id INTEGER NOT NULL,
    nome VARCHAR NOT NULL,
    descricao VARCHAR NOT NULL,
    local VARCHAR NOT NULL,
    data DATETIME NOT NULL,
    vagas INTEGER NOT NULL,
    PRIMARY KEY (id)
);

-- pessoas definição

CREATE TABLE pessoas
(
    id INTEGER NOT NULL,
    nome VARCHAR NOT NULL,
    "dataNascimento" DATETIME,
    PRIMARY KEY (id)
);