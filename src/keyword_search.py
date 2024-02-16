import csv
from datetime import datetime
import os

def search_and_store(results_file, url, soup, selector):

    results_file =  "./results/" + datetime.now().strftime("%d-%m-%Y") + ".csv"

    elements = soup.select(selector)

    graduate_children = [
        child.text.replace('\n', '').replace('  ', '') for child in elements
        if "Graduate" in child.text
    ]  

    if not os.path.exists('./results'):
        os.makedirs('./results')

    if graduate_children:  # Check if there are any graduate_children before writing
        with open(results_file, mode='a', newline='') as file:
            writer = csv.writer(file)
            # Write each graduate child on a new row
            for grad_child in graduate_children:
                writer.writerow([datetime.now().strftime("%Y-%m-%d %H:%M:%S"), url, grad_child])
    
    return
