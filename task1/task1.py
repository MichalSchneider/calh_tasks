import requests
import xml.etree.ElementTree as ET



def task1_solution():

    response = requests.get('https://coding-academy.pl/all_customers')
    root = ET.fromstring(response.text)

    for customer in root.findall('./customer'):
        line_to_write = customer.text
        #print(line_to_write)

        with open("task1_solution.txt", "a") as f:
            f.write(line_to_write + "\n")


if __name__ == '__main__':
    task1_solution()