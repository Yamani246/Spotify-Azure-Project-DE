from pyspark import pipelines as dp

exception = {"rule1":"user_id IS NOT NULL"}

@dp.table(
    name = "dimUser_stg"
)
@dp.expect_all_or_drop(exception)
def stg():
    df = spark.readStream.table("spotify_catalog.silver.dimUser")
    return df

dp.create_streaming_table(name='dimuser')

dp.create_auto_cdc_flow(
    target="dimuser",
    source="dimUser_stg",
    keys=['user_id'],
    sequence_by="updated_at",
    stored_as_scd_type= 2,
    track_history_except_column_list= None,
    name= None,
    once= False
)



