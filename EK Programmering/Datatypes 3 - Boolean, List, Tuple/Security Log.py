#After processing an access log with a tool, you have generated the above list of IP addresses that has accessed the system. This list is chronologically sorted. 

#Write a script that does the following:

#1. You received an e-mail telling you that the IP ‘8.8.8.8’ is the latest to access the system. You need to add this manually.

#2. How many entries are in the log?

#3. What are the latest 5 IPs that accessed the system?

#4. How many times did ‘3.100.186.196’ access the system?

#Security access log (chronologically sorted)
from collections import Counter


access_log = [
    '189.19.202.26', '124.124.86.154', '111.123.147.92', '191.194.49.89',
    '191.194.49.89', '3.100.186.196', '17.102.131.131', '170.40.162.9',
    '66.23.103.242', '203.207.124.71', '3.100.186.196', '170.194.124.70',
    '3.100.186.196', '161.240.120.16', '37.161.17.14', '3.100.186.196',
    '144.182.46.41', '3.100.186.196', '67.180.5.237', '182.44.178.202'
]

# 1. Add the latest IP manually
access_log.append('8.8.8.8')

# 2. Number of entries in the log
print("Total log entries:", len(access_log))

# 3. Latest 5 IPs
print("Latest 5 IPs:", access_log[-5:])

# 4. Count how many times a specific IP appears
print(
    "Times 3.100.186.196 accessed the system:",
    access_log.count('3.100.186.196')
)

# --- Bonus: Frequency statistics for all IPs ---

# Count occurrences of each IP
ip_counts = Counter(access_log)


# Sort IPs by frequency (most common first)
sorted_ip_counts = ip_counts.most_common()  # Returns list of tuples: (IP, count)

#
print() #"\nIP access frequency (most to least):"
for ip, count in sorted_ip_counts:
    print(f"{ip}: {count}")