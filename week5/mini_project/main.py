from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.types import StructType, StructField, StringType, IntegerType
from pathlib import Path

def main():
    spark = SparkSession.builder.appName("Week5_MiniProject").getOrCreate()
    spark.sparkContext.setLogLevel("ERROR")

    data_dir = Path(__file__).resolve().parent.parent / "data"
    output_dir = Path(__file__).resolve().parent.parent / "output"
    
    events_csv = str(data_dir / "events.csv")
    users_csv = str(data_dir / "users.csv")
    curated_out = str(output_dir / "curated_events")
    bad_records_out = str(output_dir / "bad_records")

    schema = StructType([
    ])

    df_events = None
    
    null_user_id_count = 0
    null_event_type_count = 0
    
    print(f"NULL user_id count: {null_user_id_count}")
    print(f"NULL event_type count: {null_event_type_count}")

    bad_records = None
    good_records = None

    good_records_filled = None

    df_users = None
    joined_df = None

    joined_df_with_minutes = None

    daily_summary = None

    spark.stop()

if __name__ == "__main__":
    main()
