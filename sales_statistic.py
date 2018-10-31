import json
import collections 
from collections import Counter

def read_file():

    with open('./sales_log.json') as file_with_sales:
        data_from_file = json.loads(file_with_sales.read())
    return data_from_file     
        

def sort_products(data_from_file):
    
    sales_stats = Counter(data_from_file)
    list_of_sales = dict(sales_stats.most_common())
    return list_of_sales


def form_and_output_final_list(list_of_sales, hyphen = ' - '):
    
    final_list_of_sales = []
    for product, qty_of_sales in list_of_sales.items():
        final_list_of_sales.append('{0}{2}{1}'.format(product, 
                                                      qty_of_sales, 
                                                      hyphen))
    print('\n'.join(final_list_of_sales))



if __name__ == '__main__': 

    read_file()
    data_from_file = read_file()
    sort_products(data_from_file)
    list_of_sales = sort_products(data_from_file)
    form_and_output_final_list(list_of_sales)
