import csv
import datetime

def search_and_store(results_file, url, soup, selector, keywords):
    elements = soup.select('#content > div > form > div.js-openings-list.opening-list.col-md-9 > div')

    found = False  

    graduate_children = [
        child.text.replace('\n', '').replace('  ', '') for child in elements
        if "Graduate" in child.text
    ]  

    with open(results_file, mode='a', newline='') as file:
        writer = csv.writer(file)
        # Now storing element_text which has no newlines
        writer.writerow([datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), url, graduate_children])
        found = True

    return found
