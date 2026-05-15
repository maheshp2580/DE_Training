from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.types import StructType, StructField, StringType, IntegerType
from pathlib import Path

def main():
    spark = SparkSession.builder.appName("Week5_Exercises").getOrCreate()
    spark.sparkContext.setLogLevel("ERROR")

    data_dir = Path(__file__).resolve().parent.parent / "data"
    events_csv = str(data_dir / "events.csv")
    users_csv = str(data_dir / "users.csv")
    events_json = str(data_dir / "events.json")

    print("\n=== Day 2: DataFrame vs Spark SQL ===")
    df = spark.read.csv(events_csv, header=True, inferSchema=True)
    df.show(5)

    df.createOrReplaceTempView("events")
    spark.sql("SELECT country, COUNT(*) AS event_count FROM events GROUP BY country").show()

    print("\n=== Day 3: Lazy Evaluation ===")
    filtered = df.filter(df.country == 'India')
    selected = filtered.select('user_id', 'event_type', 'event_date')
    grouped = selected.groupBy('event_type').count()
    grouped.show()

    print("\n=== Day 4: Core Operations ===")
    df_users = spark.read.csv(users_csv, header=True, inferSchema=True)
    india_events = df.filter(df.country == 'India')
    df_with_flag = df.withColumn('is_purchase', F.when(df.event_type == 'purchase', True).otherwise(False))
    enriched = df.join(df_users, on='user_id', how='left')
    daily_summary = df.groupBy('country', 'event_date').agg(
        F.count('event_id').alias('event_count'),
        F.avg('session_time_sec').alias('avg_session_sec')
    )
    daily_summary.show()

    print("\n=== Day 5: Schema Definition & NULLs ===")
    schema = StructType([
        StructField('event_id', IntegerType(), True),
        StructField('user_id', StringType(), True),
        StructField('event_type', StringType(), True),
        StructField('device', StringType(), True),
        StructField('country', StringType(), True),
        StructField('event_date', StringType(), True),
        StructField('session_time_sec', IntegerType(), True)
    ])
    df_schema = spark.read.csv(events_csv, header=True, schema=schema)
    df_schema.filter(F.col('user_id').isNull()).show()
    df_clean = df_schema.fillna({'user_id': 'unknown', 'session_time_sec': 0})
    df_valid = df_schema.dropna(subset=['event_id', 'event_type'])
    df_clean.show()

    print("\n=== Day 6: Partitions & Cache ===")
    print(f"Partitions: {df.rdd.getNumPartitions()}")
    df_repartitioned = df.repartition(4)
    df_smaller = df.coalesce(2)
    df.cache()
    print(f"Count: {df.count()}")

    spark.stop()

if __name__ == "__main__":
    main()
