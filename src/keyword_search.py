import csv
import datetime

def search_and_store(results_file, url, soup, selector, keywords):
    elements = soup.select(selector)
    for element in elements:
        if any(keyword.lower() in element.text.lower() for keyword in keywords):
            with open(results_file, mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), url])
            return True
    return False
