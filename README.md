# Caching Amazon S3 with Amazon ElastiCache for Redis

This sample project demonstrates how you can cache [Amazon S3](https://aws.amazon.com/s3/) objects with [Amazon ElastiCache for Redis](https://aws.amazon.com/elasticache/redis/) . This project also uses [AWS CloudFormation](https://aws.amazon.com/cloudformation/) & [AWS Cloud9](https://aws.amazon.com/cloud9/) as means to deploy, build and run this tutorial, although you can run this in your own environments as well.

These examples are also referenced in the following [blog](https://aws.amazon.com/blogs/storage/turbocharge-amazon-s3-with-amazon-elasticache-for-redis/) which provide background and context to this project. It is recommended to read the blog as a prerequisite.

## Deployment

1. Download from github, then run the following CFN template with AWS CloudFormation: [cfn/S3RedisCFN.yaml](https://raw.githubusercontent.com/aws-samples/amazon-S3-cache-with-amazon-elasticache-redis/master/cfn/S3RedisCFN.yaml)

2. Upon running the CFN, you will be prompted to enter a Subnet Id for AWS Cloud9 and Amazon ElastiCache to be launched in. Enter a subnet id to use and then click next, next, create. (Note: This step ensures that both services are running within the same availability zone for optimal performance. You can find your subnet ids within the Amazon VPC console.)

## Setup and Build

1. Upon CFN completion, take note of the generated S3 Bucket name and the Redis endpoint within the cloudformation outputs tab. Then navigate to AWS Cloud9 and open the **S3RedisCache** IDE environment.

2. Within the AWS Cloud9 environment, open (+) a new terminal and clone this repository:

   ``` 
       (ssh) 
       git clone git@github.com:aws-samples/amazon-S3-cache-with-amazon-elasticache-redis.git 
       
       (https)
       git clone https://github.com/aws-samples/amazon-S3-cache-with-amazon-elasticache-redis.git 
   ``` 
3. Navigate to the downloaded setup directory (/amazon-S3-cache-with-amazon-elasticache-redis/setup) and run the following script to further prepare your environment:
 
   ```
       cd amazon-S3-cache-with-amazon-elasticache-redis/setup
       sh s3_redis_project_setup.sh  
   ```

 4. Navigate to the resources directory (amazon-S3-cache-with-amazon-elasticache-redis/resources) and update the following properties within **constants.py**. Provide the generated resource values you captured in the cloudformation outputs: 

   ```
      redishost="" (leave out the port)
      S3bucket= "" 
   ```
 5. Next right click on and run **load_data.py**. This will generate and load 100 objects into both Amazon S3 and Amazon ElastiCache for Redis

 6. Next right click on and run **query_redis.py** and **query_S3.py** . Then compare the generated latency (in microseconds) output. 

 You will notice a significant performance improvement when querying redis vs S3. This performance test is intended to be lightweight and only for illustration purposes. Your results may slightly vary based on your environment. An example comparison between the two services converted in milliseconds is as follows: 

 ![latency](images/latency.jpg)

## Lazy-load example

A common caching technique often used is lazy loading. This approach assumes data is cached and if not, retrieves data from the origin data source, then caches the data future requests. In order to illustrate this example we must first flush the redis cache.

1. Next right click on and run **flush_redis.py** (this deletes all your keys)

2. Next right click on and run **lazy_load.py** found within the following directory (amazon-S3-cache-with-amazon-elasticache-redis/examples/lazyload). Upon first run, you will notice a cache miss because the object was not initially cached in redis. Run the script again and you will now notice a cache hit since the object was set into redis after the initial cache miss. 

## Terminate your environment

Upon running these examples, terminate your environment by the following steps:

1. Next right click on and run **delete_S3_objects.py** within the (amazon-S3-cache-with-amazon-elasticache-redis/resources) directory. This will delete all your generated S3 Objects.

2. Next, within the AWS CloudFormation console, delete the stack you launched. 
 

