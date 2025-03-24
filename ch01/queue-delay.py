import sys
# Calculate the queue delay given the transmission rate, packet length, and the avg. rate of packets/secs 
# 
# total arguments expected: 3

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

n = len(sys.argv)
if (n != 4):
    print("\nrtt usage: queue-delay.py <transmission rate> <length> <avg packet arrival rate>")
    sys.exit(1)

# Perform simple test of arguments
for i in range(1, n):
    if (not is_numeric(sys.argv[i])):
        print("Unexpected argument: "+sys.argv[i])
        sys.exit(1)

# Grab command line arguments, convert to floats
trans_rate = float(sys.argv[1])
packet_length = float(sys.argv[2])
avg_packet_arr_rate = float(sys.argv[3])

# Traffic Intensity: I = La/R
traffic_intensity = (packet_length * avg_packet_arr_rate) / trans_rate
print("Traffic Intensity (I) is "+str(traffic_intensity)+"\n")

# Queueing Delay: I(L/R)(1 - I) for I < 1
delay = traffic_intensity * (packet_length / trans_rate) * (1 - traffic_intensity)
# Convert to ms
delay_ms = delay * 1000
print("Queueing Delay is: "+ str(delay_ms))
