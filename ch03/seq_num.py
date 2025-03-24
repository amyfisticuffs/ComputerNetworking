import sys
def is_numeric(string: str) -> bool:
    # Try to convert the string to a float
    # If the conversion is successful, return True
    try:
        int(string)
        return True
    # If a ValueError is thrown, it means the conversion was not successful
    # This happens when the string contains non-numeric characters
    except ValueError:
        return False

n = len(sys.argv)
if (n != 4):
    print("\nseq_num usage: seq_num.py <initial sequence num> <max segment size> <num segments>")
    sys.exit(1)

# Perform simple test of arguments
for i in range(1, n):
    if (not is_numeric(sys.argv[i])):
        print("Unexpected argument: "+sys.argv[i])
        sys.exit(1)

# Grab command line arguments, convert to floats
initial_seq_num = int(sys.argv[1])
mss = int(sys.argv[2])
num_segments = int(sys.argv[3])

seq_num = initial_seq_num
for i in range(0, num_segments):
    print("TCP Segment "+ str(i+1) +" Sequence Number: "+str(seq_num))
    seq_num += mss

