# Copyright 2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0      

import boto3
import datetime
import redis

### Required: update Redis endpoint information ###
redishost=""
### Required: update S3 bucket information ###
S3bucket = ""

r = redis.StrictRedis(host=redishost, port=6379)

s3 = boto3.resource('s3')
### Check to see if value is in Redis

value = r.get(S3bucket + ':' + S3ObjectKey)

if value is None:
    print("Cache Miss")
    ### Get data from S3
 
    obj = s3.Object(S3bucket, S3ObjectKey)
    data = obj.get()['Body'].read().decode('utf-8') 
    
    ### Store the data into Redis
    r.set(S3bucket + ':' + S3ObjectKey, data)

else:
    print ("Cache Hit")
    print("Data retrieved from redis = " + value)



