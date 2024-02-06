from lib.pchomeFetcher import PchomeSpider
from lib.DatabaseManger import DatabaseManager


if __name__ == '__main__':

    pchome_spider = PchomeSpider()
    products = pchome_spider.search_products(keyword='顯示卡')

    
    db_manager = DatabaseManager(host="localhost", user="root", password="user", database="leadtek")

    #寫入DB
    for product in products:
        db_manager.insert_product_info(product)
    db_manager.query_all_products()
    db_manager.export_table_to_csv("gpu", "./gpu.csv")