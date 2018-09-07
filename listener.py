from boto import kinesis
import time

kinesis = kinesis.connect_to_region("eu-west-1")
shard_id = 'shardId-000000000000' #we only have one shard!
shard_it = kinesis.get_shard_iterator("BotoDemo", shard_id, "LATEST")["ShardIterator"]

while True:
    out = kinesis.get_records(shard_it, limit=2)
    shard_it = out["NextShardIterator"]
    if out['Records']:
        for record in out['Records']:
            print(record['Data'])
    else:
        time.sleep(1)