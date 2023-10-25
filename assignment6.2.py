import re

def extract_email_hosts(file_name):
    host_count = 0
    unique_hosts = set()

    try:
        with open(file_name, 'r') as file:
            for line in file:
                if line.startswith('From:'):
                    email_match = re.search(r'From:\s+(\S+@\S+)', line)
                    if email_match:
                        email = email_match.group(1)
                        _, host = email.split('@')
                        print(host)
                        unique_hosts.add(host)
                        host_count += 1

    except FileNotFoundError:
        print(f"Error: The file '{file_name}' does not exist.")

    return host_count

if __name__ == "__main__":
    file_name = "mbox.txt"  
    count = extract_email_hosts(file_name)
    print(f"Number of unique hosts found: {count}")
