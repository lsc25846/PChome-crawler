import pymysql
import pymysql.cursors
import csv

class DatabaseManager:
    def __init__(self, host="localhost", user="root", password="user", database="leadtek", charset='utf8mb4'):
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
                sql = "INSERT INTO `gpu` (`SID`, `DATETIME`, `ITEM`, `PRICE`) VALUES (%s, %s, %s, %s)"
                cursor.execute(sql, (product['Id'], product['datetime'], product['name'], product['price']))
            connection.commit()
        except Exception as e:
            print(f"Error: {e}")
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
        finally:
            connection.close()
