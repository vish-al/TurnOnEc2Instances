# TurnOnEc2Instances
This project gives a lambda python function to turn on all Amazon EC2 instances with the tag value as Environment: QA

Imagine the number of compute hours wasted by running all the dev instances over night, if you need a quick python function to shutdown all your ec2 instances with a specific tag ex: Environment:QA, copy this funciton and schedule the same using lambda with cloud watch trigger.
