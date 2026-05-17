# Databricks notebook source
# MAGIC %md
# MAGIC # 05 - Orquestração sequencial local

# COMMAND ----------
notebooks = [
    "/Workspace/Repos/<user>/Trabalho-LAKEHOUSE-COM-DATABRICKS-FREE-EDITION-E-ARQUITETURA-MEDALHAO/notebooks/01_extract_landing",
    "/Workspace/Repos/<user>/Trabalho-LAKEHOUSE-COM-DATABRICKS-FREE-EDITION-E-ARQUITETURA-MEDALHAO/notebooks/02_landing_to_bronze",
    "/Workspace/Repos/<user>/Trabalho-LAKEHOUSE-COM-DATABRICKS-FREE-EDITION-E-ARQUITETURA-MEDALHAO/notebooks/03_bronze_to_silver",
    "/Workspace/Repos/<user>/Trabalho-LAKEHOUSE-COM-DATABRICKS-FREE-EDITION-E-ARQUITETURA-MEDALHAO/notebooks/04_silver_to_gold",
]

for notebook_path in notebooks:
    dbutils.notebook.run(notebook_path, timeout_seconds=0)
