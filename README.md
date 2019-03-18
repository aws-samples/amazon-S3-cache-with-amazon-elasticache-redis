# Caching Amazon S3 with Amazon ElastiCache for Redis

This sample project demonstrates how you can cache Amazon S3 objects with Amazon ElastiCache for Redis. This project also uses AWS CloudFormation & AWS Cloud9 as means to launch and run this tutorial, although you can run this in your own environments.

These examples are also references in the following blog:TBD which provide background and context to this project.

## Deployment

1. Download and run the following CFN template with AWS CloudFormation: [cfn/S3RedisCFN.yaml](https://raw.githubusercontent.com/aws-samples/blah/master/cfn/S3RedisCFN.yaml)

2. Upon running the CFN, you will be prompted to enter a subnet to launch AWS Cloud9 and Amazon ElastiCache in. Enter a subnet id to use and then click next, next, create. (Note: this step ensures that both services are running within the same availability zone for optimal performance. You can find your subnet ids within the Amazon VPC console.)

## Setup and Build

1. Upon CFN completion, take note of the generated S3 Bucket name and the ElastiCache Redis endpoint. Then navigate to AWS Cloud9 and open the 'S3RedisCache' environment.
2. Within the AWS Cloud9 environment, open (+) a new terminal and clone this repository:

   ```git clone repo```

3. Navigate to the downloaded setup directory, run the following script to further prepare your environment:
 
   ```sh S3RedisPerformanceTestSetup.sh ```

 4. Navigate to the resources directory and edit the constants.py script. Update the following properties with your launched resources: 

   ```
      redishost="" (leave out the port)
      S3bucket= "" 
   ```
 5. Next run load_data.py. This will generate and load 100 objects into both Amazon S3 and Amazon ElastiCache for Redis

 6. Next run 'query_redis.py' and 'query_S3.py' and compare the generated latency. 

 You will notice a huge improvement from querying redis as opposed to S3. This performance test is intended to be lightweight and only for purposes to illustrate performance gains with caching. An example comparison between the two services in milliseconds is as follows:

 ![latency](images/latency.jpg)

## Lazy-load example

A common caching technique is to leverage lazy loading. This approach assumes data is cached and if not, retrieves data from the origin data source, then caches the data future requests. In order to illustrate this example we must first flush the redis cache.

1. run flush_redis.py (this deletes all your keys)

2. Navigate to examples/lazyload and run lazy_load.py. You should notice a cache MISS upon first run. Run it again and the following request will return a cache HIT.

## Terminate your environment

Upon running these examples, terminate your environment by the following steps:

1. run delete_S3_objects.py (this deletes all the generated S3 objects)

2. Within the AWS CloudFormation console, delete the stack you launched. 
 

