# Organização de Pastas e Execução

## Estrutura

- `notebooks/01_extract_landing.py`: extrai tabelas do banco relacional para `landing.dados_*` (CSV).
- `notebooks/02_landing_to_bronze.py`: converte landing para Delta no schema `bronze`.
- `notebooks/03_bronze_to_silver.py`: aplica Data Quality (remoção de nulos obrigatórios e duplicados) e grava em `silver`.
- `notebooks/04_silver_to_gold.py`: cria dimensões `dim_*` e fato `fact_carga` no `gold`.
- `notebooks/05_orchestrator.py`: execução sequencial dos notebooks.
- `jobs/trabalho3_job.json`: definição do Job com dependências entre tarefas.

## Como executar no Databricks

1. Importe/sincronize este repositório no Workspace.
2. Configure os widgets do notebook `01_extract_landing` com credenciais JDBC.
3. Ajuste os caminhos `/Workspace/Repos/<user>/...` para seu usuário real.
4. Crie o Job usando `jobs/trabalho3_job.json` (Jobs & Pipelines).
5. Execute o Job para processar LANDING -> BRONZE -> SILVER -> GOLD.
