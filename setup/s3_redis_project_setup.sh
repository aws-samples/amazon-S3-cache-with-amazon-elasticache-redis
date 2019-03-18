# Copyright 2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0   

#!/bin/bash -xe

sudo yum -y update
pip install awscli --user 
pip install redis --user

echo -e "\n\n** Sample App setup completed , enjoy!! **\n\n "

