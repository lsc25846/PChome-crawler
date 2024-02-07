import pymysql
import pymysql.cursors
import csv
#import logging


class DatabaseManager:

    #logging.basicConfig(filename='dataBase.log', filemode='w', level=logging.INFO, format='%(name)s - %(levelname)s - %(message)s')

    def __init__(self, host="localhost", user="root", password="user", database="leadtek", charset='utf8mb4', logger=None): 
        self.logger = logger
        self.db_config = {
            "host": host,
            "user": user,
            "password": password,
            "database": database,
            "charset": charset,
            "cursorclass": pymysql.cursors.DictCursor
        }

    def insert_product_info(self, product):
        try:            
            connection = pymysql.connect(**self.db_config)
            with connection.cursor() as cursor:
                # Check if SID already exists
                check_sql = "SELECT COUNT(*) FROM `gpu` WHERE `SID` = %s"
                cursor.execute(check_sql, (product['Id'],))
                if cursor.fetchone()['COUNT(*)'] > 0:
                    # If exists, update the product info
                    self.logger.info(f"Updating product info: {product['Id']}")
                    update_sql = "UPDATE `gpu` SET `DATETIME` = %s, `ITEM` = %s, `PRICE` = %s WHERE `SID` = %s"
                    cursor.execute(update_sql, (product['search_time'], product['name'], product['price'], product['Id']))
                else:
                    # If not exists, insert new product info
                    self.logger.info(f"Inserting new product info: {product['Id']}")
                    insert_sql = "INSERT INTO `gpu` (`SID`, `DATETIME`, `ITEM`, `PRICE`) VALUES (%s, %s, %s, %s)"
                    cursor.execute(insert_sql, (product['Id'], product['search_time'], product['name'], product['price']))
            connection.commit()
        except Exception as e:
            print(f"Error: {e}")
            self.logger.error(f"Error: {e}")
        finally:
            connection.close()

    def query_all_products(self):
        try:
            connection = pymysql.connect(**self.db_config)
            with connection.cursor() as cursor:
                sql = "SELECT * FROM gpu"
                cursor.execute(sql)
                result = cursor.fetchall()
                for product in result:
                    print(product)
        except Exception as e:
            print(f"Query error: {e}")
            self.logger.error(f"Query error: {e}")
        finally:
            connection.close()
    
    def export_table_to_csv(self, table_name, csv_file_path):
        try:
            connection = pymysql.connect(**self.db_config)
            with connection.cursor() as cursor:
                cursor.execute(f"SELECT * FROM {table_name}")
                result = cursor.fetchall()  # Fetch all rows
                
                # Open CSV file for writing
                with open(csv_file_path, 'w', newline='', encoding='utf-8-sig') as file:
                    writer = csv.writer(file)
                    # Assuming you want to include column headers
                    headers = [i[0] for i in cursor.description]
                    writer.writerow(headers)  # Write the headers first
                    
                    for row in result:
                        writer.writerow(row.values())  # Write row data
                        
        except Exception as e:
            print(f"Error exporting table to CSV: {e}")
            self.logger.error(f"Error exporting table to CSV: {e}")
        finally:
            connection.close()
