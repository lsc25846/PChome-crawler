import tkinter as tk
from tkinter import ttk
from lib.pchomeFetcher import PchomeSpider
from lib.DatabaseManger import DatabaseManager
import logging

def search_and_display():
    keyword = entry_keyword.get()
    products = pchome_spider.search_products(keyword=keyword)
    for product in products:
        db_manager.insert_product_info(product)    
    for product in products:
        tree.insert('', 'end', values=(product['Id'], product['name'], product['price']))

if __name__ == '__main__':
    # 配置日誌
    logging.basicConfig(filename='application.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    logger = logging.getLogger(__name__)

    pchome_spider = PchomeSpider(logger)
    db_manager = DatabaseManager(host="localhost", user="root", password="user", database="leadtek", logger=logger)
    

    root = tk.Tk()
    root.title("GPU Search")

    frame = ttk.Frame(root)
    frame.pack(side=tk.BOTTOM, fill=tk.X)

    ttk.Label(frame, text="Keyword:").pack(side=tk.LEFT)
    entry_keyword = ttk.Entry(frame)
    entry_keyword.pack(side=tk.LEFT)

    search_button = ttk.Button(frame, text="Search", command=search_and_display)
    search_button.pack(side=tk.LEFT)

    columns = ('id', 'name', 'price')
    tree = ttk.Treeview(root, columns=columns, show='headings')
    tree.heading('id', text='ID')
    tree.heading('name', text='Name')
    tree.heading('price', text='Price')
    tree.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    root.mainloop()
