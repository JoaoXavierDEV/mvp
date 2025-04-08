SELECT * from eventos e ;

select * from inscricoes i ;

select * from pessoas p ;


-- quantos eventos a pessoa Z está inscrita?
select * 
from inscricoes i
inner join pessoas pe on pe.id = i.pessoa_id
where pe.nome like '%jo%'

-- quantos eventos estão disponiveis para amanhã?
select count(id) 
from eventos e 
where e.data > '2025-04-20 09:00:00'

SELECT 
'Existem ' || COUNT(id) || ' eventos para o dia ' || strftime('%d/%m/%Y', DATE('now', '+1 day')) AS query
FROM eventos e
WHERE DATE(e.data) > DATE('now', '+1 day');

