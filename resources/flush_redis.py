# Copyright 2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

import boto3
import redis
import constants

r = redis.StrictRedis(host=constants.redishost, port=6379)

# Drop data in Redis
r.flushdb()
print("redis db size now = " + str( r.dbsize()) )

print("Completed Successfully!")



