# Trabalho 3 - Arquitetura Medalhão

Este repositório implementa o pipeline completo do trabalho 3 em Databricks:

1. Extração de todas as tabelas de um banco relacional para `LANDING/DADOS` em CSV.
2. Conversão de `LANDING` para `BRONZE` em Delta Lake.
3. Aplicação de regras de Data Quality e carga no `SILVER`.
4. Carga dimensional (Kimball) no `GOLD`.
5. Encadeamento sequencial via Databricks Job.
