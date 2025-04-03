# Python Networking Tools

## Overview
This repository contains Python scripts that serve as tools for solving and understanding networking concepts from the book *Computer Networking: A Top-Down Approach* by Jim Kurose and Keith Ross. The scripts are designed to help with practice problems from the book's website: [Kurose & Ross Interactive](https://gaia.cs.umass.edu/kurose_ross/interactive/).

## Scripts

### Chapter 1
#### `queue-delay.py`
This script calculates the **traffic intensity** and **queueing delay** based on the transmission rate, constant packet length, and average packet arrival rate.

- **Usage:**
  ```sh
  python queue-delay.py <transmission rate> <packet length> <avg packet arrival rate>
  ```
- **Example:**
  ```sh
  $ python queue-delay.py 2000000 8300 38
  Traffic Intensity (I) is 0.1577
  
  Queueing Delay is: 0.5512474465000001
  ```

---

### Chapter 3
#### `tcp-rtt.py`
This script calculates **TCP’s Round-Trip Time (RTT)** and **timeout values** using the provided alpha, beta, previous estimated RTT, and previous deviation. The script then processes a list of measured RTT values.

- **Usage:**
  ```sh
  python tcp-rtt.py <alpha> <beta> <prev estimated RTT> <prev_dev_RTT>
  ```
- **Example:**
  ```sh
  $ python tcp-rtt.py 0.125 0.25 210 12
  Enter RTT List:340 390 200
  RTT1 340.0
  DevRTT is 41.5
  Estimated RTT is 226.25
  TCP Timeout is 392.25
  
  RTT2 390.0
  DevRTT is 72.0625
  Estimated RTT is 246.71875
  TCP Timeout is 534.96875
  
  RTT3 200.0
  DevRTT is 65.7265625
  Estimated RTT is 240.87890625
  TCP Timeout is 503.78515625
  ```

#### `seq_num.py`
This script computes **TCP sequence numbers** given the initial sequence number, maximum segment size (MSS), and the number of segments to be transmitted.

- **Usage:**
  ```sh
  python seq_num.py <initial sequence number> <max segment size> <num segments>
  ```
- **Example:**
  ```sh
  $ python seq_num.py 253 196 5
  TCP Segment 1 Sequence Number: 253
  TCP Segment 2 Sequence Number: 449
  TCP Segment 3 Sequence Number: 645
  TCP Segment 4 Sequence Number: 841
  TCP Segment 5 Sequence Number: 1037
  ```
---

### Chapter 4
#### `subnet_addressing.py`

# Subnet Addressing Script

This script calculates subnet allocations based on user-provided network and host requirements using **Variable Length Subnet Masking (VLSM)**. It ensures efficient IP space utilization by assigning subnets in order of largest to smallest.

- **Usage:**

```sh
python subnet_addressing.py <Network Address(CIDR)> <subnet1_hosts> <subnet2_hosts> ...


python subnet_addressing.py 192.168.1.0/24 50 30 10

  ```
- **Example:**
```sh
python subnet_addressing.py 192.168.1.0/24 50 30 10

Network Address: 192.168.1.0/24
Private

SUBNET: 1, HOSTS: 50
Needs 52 addresses, 50 hosts + Network Address + Broadcast Address
52 addresses require 6 bits(64)
192.168.1.0 to 192.168.1.63
11000000.10101000.00000001.00000000 to
11000000.10101000.00000001.00111111
Subnet 1 Starting address: 192.168.1.1
Subnet 1 Broadcast address: 192.168.1.63
Subnet 1 Ending address: 192.168.1.62
Subnet 1 subnet address 192.168.1.0/26

...
  ```



---

### Requirements
- Python 3.x

## Notes
These scripts were written to reinforce networking concepts and are based on exercises from *Computer Networking: A Top-Down Approach*. Contributions and improvements are welcome!

## License
This project is provided for educational purposes and follows an open-source model. Feel free to modify and use it as needed.

