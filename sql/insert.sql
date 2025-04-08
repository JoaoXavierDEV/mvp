-- Inserindo dados na tabela pessoas
INSERT INTO pessoas
    (nome, "dataNascimento")
VALUES
    ('joao', '1990-01-01');
-- Adicionei uma data de nascimento fictícia

-- Inserindo dados na tabela eventos
INSERT INTO eventos
    (data, local, descricao, vagas, nome)
VALUES
    ('2025-04-10 10:00:00', 'Auditório A', 'Palestra sobre IA', 100, 'Inteligência Artificial'),
    ('2025-04-15 14:00:00', 'Sala 202', 'Workshop de Python', 50, 'Python Avançado'),
    ('2025-04-20 09:00:00', 'Auditório B', 'Seminário de Tecnologia', 200, 'Futuro da Tecnologia'),
    ('2025-04-25 16:00:00', 'Sala 101', 'Curso de Banco de Dados', 30, 'SQL para Iniciantes'),
    ('2025-04-30 18:00:00', 'Auditório C', 'Encontro de Desenvolvedores', 150, 'Dev Meetup 2025');

-- Inserindo dados na tabela inscricoes
INSERT INTO inscricoes
    (pessoa_id, evento_id, data, email)
VALUES
    (1, 2, '2025-04-30 18:00:00', 'joao@outlook.com'); 