from pyspark import pipelines as dp

@dp.table(
    name = "dimtrack_stg"
)
def stg():
    df = spark.readStream.table("spotify_catalog.silver.dimtrack")
    return df

dp.create_streaming_table(name='dimtrack')

dp.create_auto_cdc_flow(
    target="dimtrack",
    source="dimtrack_stg",
    keys=['track_id'],
    sequence_by="updated_at",
    stored_as_scd_type= 2,
    track_history_except_column_list= None,
    name= None,
    once= False
)



