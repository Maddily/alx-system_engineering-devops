# Secured and Monitored Web Infrastructure
<hr>

<img src="https://raw.githubusercontent.com/Maddily/alx-system_engineering-devops/master/0x09-web_infrastructure_design/2-secured_and_monitored_web_infrastructure.png" alt="Secured and Monitored Web Infrastructure">

## Description
<hr>

This is a three-server web infrastructure that hosts the website www.foobar.com. It's secured, monitored and serves encrypted traffic.

## Specifications and Details
<hr>

#### Firewalls
Firewalls are used in this infrastructure in order to control incoming and outgoing network traffic. They act as a barrier between the servers and the external network, protecting the servers from unauthorized access and potential cyber threats.

#### SSL Certificate
By applying the SSL certificate at the Nginx server, the website is served over HTTPS and the communication is secured between clients and the web server, providing encrypted data transfer. This is crucial for protecting sensitive information transmitted over the network, such as login credentials, personal data, or financial transactions.

#### Monitoring
By monitoring, there is proactive identification of issues, efficient troubleshooting, and optimization of performance across servers.
A monitoring agent is installed on each web server to collect relevant metrics like CPU usage, memory, disk, and specifically, QPS.
QPS stands for "Queries Per Second." It is a metric used to measure the rate at which queries or requests are processed by a system. It indicates how quickly it can respond to incoming queries or requests.
Alerting rules are configured in the monitoring system based on QPS thresholds. The alert is triggered when QPS exceeds a certain value.

#### Why terminating SSL at the load balancer level is an issue
The communication between the load balancer and the web servers occurs over an unencrypted channel. This poses a security risk, as sensitive data, including user credentials, may be transmitted in clear text within the internal network.

#### Why having only one MySQL server capable of accepting writes is an issue
In this setup, only the master MySQL server can write, replica servers can only read. If the master server goes down, there is no active node to handle write operations, causing a write outage and preventing the application from updating the database until the master server is restored.

#### Why having servers with all the same components (database, web server and application server) might be a problem
The servers in this setup have the same components. Servers with identical components may experience uneven resource demands, making it challenging to scale them uniformly. For optimal performance, it's beneficial to allocate resources based on specific needs, such as having more database servers than application servers if required.

Also, servers with identical components may face issues during maintenance because if one component (e.g., database) on a server is undergoing maintenance, it affects other components (e.g., web server, application server) on the same server.

#### SPOF
The Load Balancer is considered a Single Point of Failure (SPOF) in this setup as well, because if it fails, the incoming traffic distribution among servers will be disrupted, potentially leading to service unavailability.
##### To address this:
Redundant load balancers or failover mechanisms can be implemented to minimize the risk of a single point of failure.
