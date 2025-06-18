import pandas as pd
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg
import os

# Initialize Spark
spark = SparkSession.builder.appName("StockETL").getOrCreate()

# Step 1: Read hardcoded CSV
df = spark.read.csv("data/stock_data.csv", header=True, inferSchema=True)

# Step 2: Transformation – Add 3-day moving average of close price
windowSpec = (
    df.orderBy("date")
      .select("date", "close")
      .toPandas()
)

windowSpec["ma_3day"] = windowSpec["close"].rolling(window=3).mean()

# Save processed data
os.makedirs("output", exist_ok=True)
windowSpec.to_csv("output/processed.csv", index=False)
print("ETL job done!")
