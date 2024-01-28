# Distributed Web Infrastructure
<hr>

<img src="https://raw.githubusercontent.com/Maddily/alx-system_engineering-devops/master/0x09-web_infrastructure_design/0-simple_web_stack.png" alt="Distributed Web Infrastructure">

## Description
<hr>

This is a two-server web infrastructure that hosts the website www.foobar.com.

## Specifications and Details
<hr>

#### Load Balancer Distribution Algorithm
Round Robin distribution algorithm is used. It passes each new connection request to the next server in line, eventually distributing connections evenly across the array of machines being load balanced.

#### Active-Active or Active-Passive setup?
The load balancer is configured with an active-active setup. It maximizes resource utilization and distributes traffic across multiple servers, which is suitable for handling higher loads and achieving scalability. Unlike active-passive which underutilizes resources during normal operation, as only one server actively handles traffic.

#### Master-Replica
The MySQL Master-Replica cluster uses replication to keep data synchronized by continuously copying and applying changes (transactions) from the master database to the replica database. The Master database reads and writes data while the Replica can only read.

#### SPOF
The Load Balancer is considered a Single Point of Failure (SPOF) because if it fails, the incoming traffic distribution among servers will be disrupted, potentially leading to service unavailability.
##### To address this:
Redundant load balancers or failover mechanisms can be implemented to minimize the risk of a single point of failure.
