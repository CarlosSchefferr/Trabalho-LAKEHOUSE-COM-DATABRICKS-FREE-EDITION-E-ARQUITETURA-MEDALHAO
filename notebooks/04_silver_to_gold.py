# Databricks notebook source
# MAGIC %md
# MAGIC # 04 - SILVER para GOLD (Modelo Dimensional)

# COMMAND ----------
from pyspark.sql.functions import col, current_timestamp, monotonically_increasing_id

dbutils.widgets.text("catalog", "main")

# COMMAND ----------
catalog = dbutils.widgets.get("catalog")
silver_schema = "silver"
gold_schema = "gold"

spark.sql(f"CREATE SCHEMA IF NOT EXISTS {catalog}.{gold_schema}")

silver_tables = [row.tableName for row in spark.sql(f"SHOW TABLES IN {catalog}.{silver_schema}").collect()]

fact_rows = []

for table_name in silver_tables:
    source = f"{catalog}.{silver_schema}.{table_name}"
    dim_target = f"{catalog}.{gold_schema}.dim_{table_name}"

    df = spark.read.table(source)
    dim_df = (
        df.dropDuplicates()
        .withColumn("dim_id", monotonically_increasing_id())
        .withColumn("gold_ts", current_timestamp())
    )

    dim_df.write.format("delta").mode("overwrite").saveAsTable(dim_target)

    fact_rows.append((table_name, dim_df.count()))

fact_df = spark.createDataFrame(fact_rows, ["dim_table", "row_count"]).withColumn("load_ts", current_timestamp())
fact_df.write.format("delta").mode("overwrite").saveAsTable(f"{catalog}.{gold_schema}.fact_carga")
