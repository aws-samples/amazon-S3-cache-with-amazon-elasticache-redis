# Copyright 2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0   

import boto3
import redis
import constants

r = redis.StrictRedis(host=constants.redishost, port=6379)

print("Redis DB size = " + str( r.dbsize()) )

print("Completed Successfully!")


