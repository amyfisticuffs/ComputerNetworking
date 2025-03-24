import sys
# Calculate the Estimated RTT given the data point, alpha and the previous smoothed value 
# Calculate the DevRTT given the previous DevRTT, Beta, the data point, and the Estimated RTT
# Calculate TCP Timeout given the EstimatedRTT and DevRTT
# Round results to two decimal places and return results
# total arguments expected: 6

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
if (n != 5):
    print("\nrtt usage: tcp-rtt.py <alpha> <beta> <prev estimated rtt> <prev_dev_rtt>")
    sys.exit(1)

# Perform simple test of arguments
for i in range(1, n):
    if (not is_numeric(sys.argv[i])):
        print("Unexpected argument: "+sys.argv[i])
        sys.exit(1)

# Grab command line arguments, convert to floats
alpha = float(sys.argv[1])
beta = float(sys.argv[2])
prev_smoothed_rtt = float(sys.argv[3])
prev_dev_rtt = float(sys.argv[4])

txt = input("Enter RTT List:")
list = txt.split()
n = len(list)
rtt_list = []
for i in range(0, n):
    if (not is_numeric(list[i])):
        print("Unexpected argument: "+sys.argv[i])
        sys.exit(1)
    else:
        rtt_list.append(float(list[i]))

for i in range(0, n):
    rtt_data_point = rtt_list[i]

    # DevRTT = ( 1 - β ) * PrevDevRTT + β * | SampleRTT - EstimatedRTT|
    # PrevDevRTT is the previous DevRTT
    # SampleRTT latest data point
    # EstimatedRTT is the previous smoothed value
    # β is the smoothing constant
    dev_rtt = ((1 - beta) * prev_dev_rtt) + beta * abs(rtt_data_point - prev_smoothed_rtt)

    # EstimatedRTT = Sn = ⍺Xn + ( 1- ⍺ ) Sn-1
    # Sn is the new smoothed value
    # Xn is the latest data point
    # Sn-1 is the previous smoothed value
    # ⍺ is the smoothing constant
    estimated_rtt = (alpha * rtt_data_point) + (1 - alpha) * prev_smoothed_rtt

    # TCP Timeout = EstimatedRTT + 4(DevRTT)
    tcp_timeout = estimated_rtt + (4 * dev_rtt)

    print("RTT"+str(i+1)+" "+str(rtt_data_point))
    print("DevRTT is "+str(dev_rtt))
    print("Estimated RTT is "+str(estimated_rtt))
    print("TCP Timeout is "+str(tcp_timeout)+"\n")

    prev_smoothed_rtt = estimated_rtt
    prev_dev_rtt = dev_rtt

