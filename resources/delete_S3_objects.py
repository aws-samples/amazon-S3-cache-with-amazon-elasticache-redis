# Copyright 2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

import boto3
import constants

s3 = boto3.resource('s3')

#Iterate through all created files and delete them
i = 0
while i < 100:
 s3.Object(constants.S3bucket, 'filename' + str(i) + '.txt').delete()
 i += 1

print("Completed Successfully!")


