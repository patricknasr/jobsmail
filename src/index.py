from fetch_and_parse import fetch_and_parse
from keyword_search import search_and_store
from send_email import send_email

def main():
    soup = fetch_and_parse(url='https://thequantiumgroup.hire.trakstar.com/')
    if soup is None:
        raise ValueError('url not accessed')
    search_and_store(results_file='./results/quantium.csv', url='https://thequantiumgroup.hire.trakstar.com/', soup=soup, selector='#content > div > form > div.js-openings-list.opening-list.col-md-9 > div')
    send_email(to_email='pnasrwork@gmail.com')
if __name__ == "__main__":
    main()