import sys
import ipaddress

def is_numeric(string: str) -> bool:
    try:
        float(string)
        return True
    except ValueError:
        return False

# User Input
n = len(sys.argv)
if n < 2:
    print("\nsubnet_addressing usage: <Network Address(CIDR)> <subnets>")
    sys.exit(1)

# Subnets included?
subnet_list = []
subnet_num = 1
for i in range(2, n):
    if not is_numeric(sys.argv[i]):
        print("Unexpected argument: " + sys.argv[i])
        sys.exit(1)
    subnet_list.append((subnet_num, int(sys.argv[i])))
    subnet_num += 1

# Define the original network
cidr_input = sys.argv[1]
network = ipaddress.IPv4Network(cidr_input, strict=False)
print("When subnetting, you should always allocate the subnet with the largest number ")
print("of hosts first. This strategy is called Variable Length Subnet Masking (VLSM), ")
print("and it helps to minimize wasted IP space while ensuring that all subnets fit properly.\n")

print(f"🌐 Network {network}")
print(f"{network.network_address} → {network.broadcast_address}")
print("Private" if network.is_private else "Public")
# Excluding network & broadcast
print(f"Max Number of Hosts (Excluding Network & Broadcast): {network.num_addresses - 2}\n")

if not subnet_list:
    sys.exit(0)

# Sort subnets from largest to smallest
sorted_subnet_list = sorted(subnet_list, key=lambda x: x[1], reverse=True)

# Track remaining network space
remaining_networks = [network]

def allocate_subnet(subnet_ident, subnet_hosts):
    """ Allocates a subnet with the given number of hosts from remaining space. """
    global remaining_networks

    needed_prefix = 32 - (subnet_hosts - 1).bit_length()

    for i, net in enumerate(remaining_networks):
        # Find a network that can fit this subnet
        if net.prefixlen <= needed_prefix:
            subnets = list(net.subnets(new_prefix=needed_prefix))
            allocated_subnet = subnets[0]

            # Update remaining space
            remaining_networks[i:i+1] = subnets[1:]  # Replace used network with remaining
            return allocated_subnet

    raise ValueError(f"Not enough space for subnet {subnet_ident} with {subnet_hosts} hosts.")

# Process each subnet request
for subnet_ident, subnet_hosts in sorted_subnet_list:
    allocated = allocate_subnet(subnet_ident, subnet_hosts)

    print(f"🌐 Subnet {subnet_ident}, {subnet_hosts} hosts:", allocated)  
    print(f"{allocated.network_address} → {allocated.broadcast_address}")
    print('.'.join([bin(int(x)+256)[3:] for x in str(allocated.network_address).split('.')])+ " to")
    print('.'.join([bin(int(x)+256)[3:] for x in str(allocated.broadcast_address).split('.')]))
    print(f"Broadcast Address: {allocated.broadcast_address}")
    print(f"First Address:     {allocated.network_address + 1}")
    print(f"Last Address:      {allocated.broadcast_address - 1}\n")
