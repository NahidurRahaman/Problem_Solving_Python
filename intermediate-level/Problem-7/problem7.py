from collections import Counter

def top_ips_from_log(file_path, top_n=3):
    ip_counter = Counter()

    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split()
            if parts:
                ip = parts[0]
                ip_counter[ip] += 1

    return ip_counter.most_common(top_n)


log_file = 'access.log'  
top_ips = top_ips_from_log(log_file)
print("Top IPs:")
for ip, count in top_ips:
    print(f"{ip}: {count} requests")
