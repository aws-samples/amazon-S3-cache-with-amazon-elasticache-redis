# Copyright 2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0      

import boto3
import datetime
import redis
import sys
sys.path.insert(0,'amazon-S3-cache-with-amazon-elasticache-redis/resources/')
import constants

r = redis.StrictRedis(host=constants.redishost, port=6379)

s3 = boto3.resource('s3')

###Sample object to test with
S3ObjectKey = "filename0.txt"

### Check to see if value is in Redis
value = r.get(constants.S3bucket + ':' + S3ObjectKey)

if value is None:
    print("Cache Miss")
    ### Get data from S3
 
    obj = s3.Object(constants.S3bucket, S3ObjectKey)
    data = obj.get()['Body'].read().decode('utf-8') 
    
    ### Store the data into Redis
    r.set(constants.S3bucket + ':' + S3ObjectKey, data)

else:
    print ("Cache Hit")
    print("Data retrieved from redis = " + value)