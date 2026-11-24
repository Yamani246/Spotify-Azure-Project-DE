from pyspark import pipelines as dp

@dp.table(
    name = "factstream_stg"
)
def stg():
    df = spark.readStream.table("spotify_catalog.silver.factstream")
    return df

dp.create_streaming_table(name='factstream')

dp.create_auto_cdc_flow(
    target="factstream",
    source="factstream_stg",
    keys=['stream_id'],
    sequence_by="stream_timestamp",
    stored_as_scd_type= 1,
    track_history_except_column_list= None,
    name= None,
    once= False
)



