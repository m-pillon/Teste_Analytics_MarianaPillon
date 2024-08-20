/*
seleciona nome, categoria e soma de vendas
das tabelas produto INTERSECCAO com vendas
agrupado pelo produto
ordenado pela soma de vendas decrescente
*/
SELECT p.NomeProduto, p.categoria, SUM(v.quantidade * p.preco)
FROM Produto p NATURAL JOIN Venda v
GROUP BY p.NomeProduto
ORDER BY SUM(v.quantidade * p.preco) DESC;

/*
como mencionei no README, achei que '2024' no email
era um erro de digitação e fiz com 2023

seleciona nome e soma de vendas
das tabelas produto INTERSECCAO com vendas
em entradas com datas em junho
agrupado pelo produto
ordenado pela soma de vendas
retornando apenas 5 entradas (formato MySQL)
*/
SELECT p.NomeProduto, SUM(v.quantidade * p.preco)
FROM Produto p NATURAL JOIN Venda v
WHERE v.data BETWEEN '2023-06-01' AND '2023-06-30'
GROUP BY p.NomeProduto
ORDER BY SUM(v.quantidade * p.preco)
LIMIT 5;