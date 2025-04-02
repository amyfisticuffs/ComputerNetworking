import sys
import ipaddress
import math

def is_numeric(string: str) -> bool:
    # Try to convert the string to a float
    # If the conversion is successful, return True
    try:
        float(string)
        return True
    # If a ValueError is thrown, it means the conversion was not successful
    # This happens when the string contains non-numeric characters
    except ValueError:
        return False

def get_last_number_in_prefix(net):
    # Convert the network address to a string and split by dots
    return int(str(net.network_address).split('.')[-1])
 

def get_first_three_nums_in_prefix(net):
    l = str(net.network_address).split('.')
    return l[0]+'.'+l[1]+'.'+l[2]+'.'

def get_number_of_bits(number):
    number -= 1
    if number == 0:
        return 0
    if number < 0:
      number = abs(number)
    return math.floor(math.log2(number)) + 1

def max_number_from_bits(n):
    # Calculates the maximum possible number representable by n bits.
    if n < 0:
      raise ValueError("Number of bits cannot be negative")
    return (1 << n) - 1


# User Input
n = len(sys.argv)
if (n < 2):
    print("\nsubnet_addressing usage: <Network Address(CIDR)> <subnets>")
    sys.exit(1)

# Define the original network
cidr_input = sys.argv[1]

# Create an IPv4Network object
net = ipaddress.ip_network(cidr_input, strict=False)
print("When subnetting, you should always allocate the subnet with the largest number ")
print("of hosts first. This strategy is called Variable Length Subnet Masking (VLSM), ")
print("and it helps to minimize wasted IP space while ensuring that all subnets fit properly.\n")

print(f"Network Address: {cidr_input}")
print("Private" if net.is_private else "Public")
# Excluding network & broadcast
print(f"Max Number of Hosts (Excluding Network & Broadcast): {net.num_addresses - 2}\n") 

# Subnets included?
subnet_list = []
subnet_num = 1
for i in range(2, n):
    # Perform simple test of arguments
    if (not is_numeric(sys.argv[i])):
        print("Unexpected argument: "+sys.argv[i])
        sys.exit(1)
    t = (subnet_num, int(sys.argv[i]))
    subnet_num += 1
    subnet_list.append(t)

if len(subnet_list) == 0:
    sys.exit(0)

# Sort subnets from largest to smallest
sorted_subnet_list = sorted(subnet_list, key=lambda x: x[1], reverse=True)
# print(sorted_subnet_list)

first_three_ip = get_first_three_nums_in_prefix(net)
first_addr = get_last_number_in_prefix(net)

#++++++++++++Subnetting+++++++++++++++++++++++
for subnet_num, num_hosts in sorted_subnet_list:
    print(f"SUBNET: {subnet_num}, HOSTS: {num_hosts}")

    subnet_hosts = num_hosts + 2 # Number of hosts + Network Address + Broadcast Address
    print(f"Needs {subnet_hosts} addresses, {num_hosts} hosts + Network Address + Broadcast Address")

    num_bits = get_number_of_bits(subnet_hosts)
    # 49 addresses require 6 bits (64)
    print(f"{subnet_hosts} addresses require {num_bits} bits({max_number_from_bits(num_bits)+1})")
    last_addr = first_addr + max_number_from_bits(num_bits)
    # print(f"First three numbers in the network prefix: {first_three_ip}")

    # Define the address range
    start_ip = ipaddress.IPv4Address(first_three_ip+str(first_addr))
    end_ip = ipaddress.IPv4Address(first_three_ip+str(last_addr))
    print(f"{start_ip} to {end_ip}")
    print('.'.join([bin(int(x)+256)[3:] for x in str(start_ip).split('.')])+ " to")
    print('.'.join([bin(int(x)+256)[3:] for x in str(end_ip).split('.')]))
    starting_addr = ipaddress.IPv4Address(first_three_ip+str(first_addr+1))
    print(f"Subnet {str(subnet_num)} Starting address: {starting_addr}")
    print("     found by adding 1 to the subnet address")
    print(f"Subnet {str(subnet_num)} Broadcast address: {end_ip}")
    ending_addr = ipaddress.IPv4Address(first_three_ip+str(last_addr-1))
    print(f"Subnet {str(subnet_num)} Ending address: {ending_addr}")
    print("     found by subtracting 1 from the broadcast address")

    # Find the smallest set of CIDR blocks covering the range
    cidr_blocks = list(ipaddress.summarize_address_range(start_ip, end_ip))

    # Print the result
    for cidr in cidr_blocks:
        print(f"Subnet {str(subnet_num)} subnet address {cidr}")

    first_addr = last_addr +1
    print("\n\n")
#+++++++++++++++++++++++++++++++++++++++++++++++

