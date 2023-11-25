![1-distributed_web_infrastructure](https://github.com/ElaasriTarik/alx-system_engineering-devops/assets/37253593/d363f77b-01d7-4fc3-b84d-d2068e7a34e2)

1- We have added a new server and a load balancer, those would be usefull because when we have a lot of traffic, the load balancer is 
going to balance the traffic between the two server so we won't have a latency or lagging in response time

2- I have used a Round Robin distribution algorithm in my load balancer because we have limited
resources and round robin seems reasonable for that task.

3- we use an active-passive setup. an active-active setup maximizes the usage of the servers while the A-P saves up on costs and simplifies managment.
an A-A setup would seem more reasonable if we wanted to maximize our resources and have a more efficient work flow.

------------------------

1- we only have one sql node for database and one load balances, if any of those fail the whole service could be lost and therefore downtime.

2- No fire walls were implemented between the client and the application server and that will endanger our servers or the client.
  -> HTTPS are highly recommended for more web browsing serurity and protection of user's data and payment info. That is what this network lacks.
  -> No Monitoring
  
