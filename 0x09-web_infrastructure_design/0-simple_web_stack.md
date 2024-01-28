# Simple Web Stack

<img src="https://raw.githubusercontent.com/Maddily/alx-system_engineering-devops/master/0x09-web_infrastructure_design/0-simple_web_stack.png" alt="Simple Web Stack">

## Description

This is a one-server web infrastructure that hosts the website that is reachable via www.foobar.com.

## Specifications and Details

#### What is a server?
It’s a software or program that runs on an operating system on a computer in a data center. The word server sometimes refers to a physical computer or the server software running on a computer.

#### What is the role of a domain name?
A domain name is used to access a website from a web browser. It maps to the IP address of the server hosting the website.

#### What type of DNS record is www in www.foobar.com?
The DNS record for www is CNAME (Canonical Name) record. It redirects the domain's "www" subdomain to the main domain (Acting as an alias for foobar.com), ensuring that both variations point to the same thing. It is commonly used for website accessibility, allowing users to reach a website with or without the "www" prefix.

#### What is the role of the web server?
The web server receives HTTP requests from a web browser, retrieves requested files and data (static content such as html, css, js, images,...) then sends it to the browser using HTTP. After that, the browser displays the requested web page.

#### What is the role of the application server?
The application server is responsible for executing and managing the dynamic content of web applications.
It receives requests from a client where a user is accessing the web application, and executes server-side code, processing dynamic content written in languages such as PHP, Python, or Ruby. This includes tasks like interacting with databases, performing calculations, and generating dynamic HTML content.

#### What is the role of the database?
The database allows for data storage, retrieval and modification.

#### What is the server using to communicate with the computer of the user requesting the website?
The server is using HTTP (Hyper Text Transfer Protocol). HTTP defines the rules for how messages are formatted and transmitted between the server and the user's computer.

#### What is the SPOF in this infrastructure?
The server is the SPOF.
Because this is a single-server setup without redundancy, there’s no backup. If the server goes down for any reason, there is no alternative system to take over, leading to service downtime.

#### When new code is deployed and the web server needs to be restarted, a temporary downtime may occur because:
- While the web server is restarting, it temporarily stops serving requests and existing connections may be interrupted.
- If the code deployment involves changes to application components or dependencies, the application may need to restart as well. This can contribute to the overall downtime.
- If the code deployment includes changes to the database schema, database connections or migrations might be required. This can contribute to downtime.
##### To minimize downtime during code deployment:
- Use backup servers, ensuring that at least some of the servers remain operational at all times.
- Use a load balancer to distribute traffic across multiple servers. During deployment, the load balancer can redirect requests to healthy servers while the others are being updated.

#### Why can this infrastructure not scale and handle traffic that would exceed the server capacity?
- A single server has finite resources (CPU, memory, disk I/O). It may not efficiently scale to meet the demands of a growing user base.
- Scaling by upgrading the server's hardware has limitations.
##### To address these limitations:
- Add more servers to the infrastructure to handle increased demand and use a load balancer.
- Employ auto-scaling solutions that dynamically adjust the number of servers based on traffic patterns.
