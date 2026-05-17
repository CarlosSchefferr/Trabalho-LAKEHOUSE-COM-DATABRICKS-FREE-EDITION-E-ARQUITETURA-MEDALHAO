# Databricks notebook source
# MAGIC %md
# MAGIC # 01 - Extração para LANDING/DADOS (CSV)

# COMMAND ----------
dbutils.widgets.text("jdbc_host", "")
dbutils.widgets.text("jdbc_port", "3306")
dbutils.widgets.text("jdbc_database", "")
dbutils.widgets.text("jdbc_user", "")
dbutils.widgets.text("jdbc_password", "")
dbutils.widgets.text("jdbc_driver", "com.mysql.cj.jdbc.Driver")
dbutils.widgets.text("catalog", "main")

# COMMAND ----------
source = {
    "host": dbutils.widgets.get("jdbc_host"),
    "port": dbutils.widgets.get("jdbc_port"),
    "database": dbutils.widgets.get("jdbc_database"),
    "user": dbutils.widgets.get("jdbc_user"),
    "password": dbutils.widgets.get("jdbc_password"),
    "driver": dbutils.widgets.get("jdbc_driver"),
}

catalog = dbutils.widgets.get("catalog")
landing_schema = "landing"
landing_table_base = "dados"

jdbc_url = f"jdbc:mysql://{source['host']}:{source['port']}/{source['database']}"
options = {
    "user": source["user"],
    "password": source["password"],
    "driver": source["driver"],
}

spark.sql(f"CREATE SCHEMA IF NOT EXISTS {catalog}.{landing_schema}")

# COMMAND ----------
metadata_query = "(SELECT table_name FROM information_schema.tables WHERE table_schema = '{db}') tbl".format(db=source["database"])
tables_df = spark.read.format("jdbc").option("url", jdbc_url).option("dbtable", metadata_query).options(**options).load()
table_names = [row.table_name for row in tables_df.collect()]

for table_name in table_names:
    df = spark.read.format("jdbc").option("url", jdbc_url).option("dbtable", table_name).options(**options).load()
    target = f"{catalog}.{landing_schema}.{landing_table_base}_{table_name}"

    (
        df.write.mode("overwrite")
        .option("header", "true")
        .option("sep", ";")
        .format("csv")
        .saveAsTable(target)
    )
