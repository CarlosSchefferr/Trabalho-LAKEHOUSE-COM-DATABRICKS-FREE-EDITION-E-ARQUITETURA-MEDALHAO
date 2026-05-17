# Trabalho 3 - Lakehouse com Databricks (Arquitetura Medalhão)

Este repositório contém a implementação do **Trabalho 3** com pipeline completo em Databricks:

- Extração de todas as tabelas de um banco relacional para `LANDING/DADOS` em **CSV**
- Conversão para **Delta Lake** no schema **BRONZE**
- Aplicação de **Data Quality** e gravação no schema **SILVER**
- Carga de modelo dimensional (**Kimball**) no schema **GOLD**
- Encadeamento sequencial por **Databricks Job (Jobs & Pipelines)**

## Estrutura

- `notebooks/01_extract_landing.py`
- `notebooks/02_landing_to_bronze.py`
- `notebooks/03_bronze_to_silver.py`
- `notebooks/04_silver_to_gold.py`
- `notebooks/05_orchestrator.py`
- `jobs/trabalho3_job.json`
- `mkdocs.yml` e `docs/`

## Documentação

Execute o MkDocs localmente:

```bash
pip install mkdocs mkdocs-material
mkdocs serve
```
