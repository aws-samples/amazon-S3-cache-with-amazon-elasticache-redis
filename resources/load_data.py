# Copyright 2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0     

import boto3
import redis
import constants

r = redis.StrictRedis(host=constants.redishost, port=6379)

# Load data into S3 & Redis
s3 = boto3.resource('s3')
i = 0
while i < 100:
 #PUT data in S3
 object = s3.Object(constants.S3bucket, 'filename' + str(i) + '.txt')
 object.put(Body="some generated data for filename" + str(i))
 #Cache the data [ KEY = bucket:filenameX.txt]
 r.set(constants.S3bucket + ':filename' + str(i) + '.txt', 'some generated data for filename' + str(i))
 i += 1

print("Data loaded successfully!")
 
 
