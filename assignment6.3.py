import re

def find_and_calculate_average(file_name):
    total_sum = 0
    count = 0

    try:
        with open(file_name, 'r') as file:
            for line in file:
                match = re.search(r'^X-DSPAM-Confidence:\s+([0-9.]+)', line)
                if match:
                    confidence = float(match.group(1))
                    total_sum += confidence
                    count += 1

        if count == 0:
            print("No matching lines found in the file.")
        else:
            average = total_sum / count
            print(f"Sum of numbers: {total_sum}")
            print(f"Average value: {average}")

    except FileNotFoundError:
        print(f"Error: The file '{file_name}' does not exist.")

if __name__ == "__main__":
    file_name = input("Enter the file name: ")
    find_and_calculate_average(file_name)
