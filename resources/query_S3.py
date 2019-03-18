# Copyright 2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0             

import boto3
import datetime
import constants

# Query & Record Individual GET requests on S3 Objects
s3 = boto3.resource('s3')

keys = []
i = 0

while i < 100:
 
 # Start timer
 start = datetime.datetime.now()
 
 obj = s3.Object(constants.S3bucket, 'filename' + str(i) + '.txt')
 data = obj.get()['Body'].read().decode('utf-8') 
 
 end = datetime.datetime.now()
# End timer
 
 # Parse each result into microseconds
 delta = end - start
 millis = delta.seconds * 1000000
 millis += delta.microseconds 
 keys.append(millis)
 i += 1
 
#Throw out first request due to initialization overhead
keys.pop(0)

#print timing
sum=0
for timing in keys: 
    sum+=timing
     
print("=====Timing=====\n")

average = sum / len(keys)
print ("Average Latency in Microseconds: ", average )
print ("MAX Latency in Microseconds: ", max(keys))
print ("MIN Latency in Microseconds: ", min(keys))
print("\nCompleted Successfully!")






  