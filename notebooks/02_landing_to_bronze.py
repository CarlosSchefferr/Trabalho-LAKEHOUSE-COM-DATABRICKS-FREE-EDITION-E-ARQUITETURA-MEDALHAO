# Databricks notebook source
# MAGIC %md
# MAGIC # 02 - LANDING/DADOS (CSV) para BRONZE (DELTA)

# COMMAND ----------
from pyspark.sql.functions import current_timestamp

dbutils.widgets.text("catalog", "main")

# COMMAND ----------
catalog = dbutils.widgets.get("catalog")
landing_schema = "landing"
bronze_schema = "bronze"
landing_prefix = "dados_"

spark.sql(f"CREATE SCHEMA IF NOT EXISTS {catalog}.{bronze_schema}")

landing_tables = [
    row.tableName
    for row in spark.sql(f"SHOW TABLES IN {catalog}.{landing_schema}").collect()
    if row.tableName.startswith(landing_prefix)
]

for landing_table in landing_tables:
    source = f"{catalog}.{landing_schema}.{landing_table}"
    table_name = landing_table.replace(landing_prefix, "", 1)
    target = f"{catalog}.{bronze_schema}.{table_name}"

    (
        spark.read.table(source)
        .withColumn("ingestion_ts", current_timestamp())
        .write.format("delta")
        .mode("overwrite")
        .saveAsTable(target)
    )
