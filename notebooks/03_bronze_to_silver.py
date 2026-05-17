# Databricks notebook source
# MAGIC %md
# MAGIC # 03 - BRONZE para SILVER com Data Quality

# COMMAND ----------
from pyspark.sql.functions import col, current_timestamp, lit

dbutils.widgets.text("catalog", "main")

# COMMAND ----------
catalog = dbutils.widgets.get("catalog")
bronze_schema = "bronze"
silver_schema = "silver"

spark.sql(f"CREATE SCHEMA IF NOT EXISTS {catalog}.{silver_schema}")

bronze_tables = [row.tableName for row in spark.sql(f"SHOW TABLES IN {catalog}.{bronze_schema}").collect()]

for table_name in bronze_tables:
    source = f"{catalog}.{bronze_schema}.{table_name}"
    target = f"{catalog}.{silver_schema}.{table_name}"

    df = spark.read.table(source)

    not_null_columns = [field.name for field in df.schema.fields if not field.nullable]
    cleaned = df
    for column_name in not_null_columns:
        cleaned = cleaned.filter(col(column_name).isNotNull())

    dq_result = (
        cleaned.dropDuplicates()
        .withColumn("dq_status", lit("valid"))
        .withColumn("silver_ts", current_timestamp())
    )

    dq_result.write.format("delta").mode("overwrite").saveAsTable(target)
