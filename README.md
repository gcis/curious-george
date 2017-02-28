![alt tag](https://raw.githubusercontent.com/gcis/curious-george/master/doc/resources/img/curiousgeorge.png)


Curiosous George is a very simple app that will kill instances in you AWS environment, based on a tag value provided by the user (more complex tag key/value configuration will be implemented in future development)


## Start curious George

To start curious George simply download the docker container `gcis/curious-george`, and run it providing the following env variables

- **AWS_ACCESS_KEY_ID**: *string* (AWS access key)
- **AWS_SECRET_ACCESS_KEY**: *string* (AWS secret access key)
- **REGION**: *string* (AWS region)
- **TAG**: *string* (AWS resource tag-value, see http://boto3.readthedocs.io/en/latest/reference/services/ec2.html#EC2.Client.describe_instances)
- **PROBABILITY**: *int* [0-100] (the probability that after a loop an instance is terminated)
- **LOOP_TIME**: *int* (time in seconds, duration of each loop - min 15s)

In the following example every 1h and the probability that an instance is terminated will be 75%

    docker run -d \
    -e AWS_ACCESS_KEY_ID=YOURACCESSKEY \
    -e AWS_SECRET_ACCESS_KEY=YOURSECRETKEY \
    -e REGION=eu-west-1 \
    -e TAG=YOUR_TARGET_TAG_VALUE \
    -e PROBABILITY=75 \
    -e LOOP_TIME=3600

####
#### N.B.
AWS credentials (except REGION) can be replaced by linking the container local credentials
to your local aws config by launching the container using

    -v /Users/name/.aws:/root/.aws

or you can even omit them if using an `instance role` on AWS.


