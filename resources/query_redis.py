# Copyright 2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0          

import boto3
import datetime
import redis
import constants

r = redis.StrictRedis(host=constants.redishost, port=6379)

# Query S3 Data
s3 = boto3.resource('s3')

keys = []
i = 0

while i < 100:
 
 # Start timer
 start = datetime.datetime.now()
 
 value = r.get(constants.S3bucket + ':filename' + str(i) + '.txt')
 
 end = datetime.datetime.now()
 # End timer

 delta = end - start
 millis = delta.seconds * 1000000
 millis += delta.microseconds 
 keys.append(millis)
 i += 1

#throw out first request due to initialization overhead
keys.pop(0)

#print timing
sum=0
for timing in keys: 
    sum+=timing
    #uncomment below to see timing for each request
    #print timing

average = sum / len(keys)

print("=====Timing=====\n")

average = sum / len(keys)
print ("Average Latency in Microseconds: ", average )
print ("MAX Latency in Microseconds: ", max(keys))
print ("MIN Latency in Microseconds: ", min(keys))
print("\nCompleted Successfully!")


print("Completed Successfully!")






  