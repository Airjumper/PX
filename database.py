import sqlite3


conn = sqlite3.connect('diona.db')
c = conn.cursor()

c.execute("""CREATE TABLE User (
           userID integer,
           userName text,
           userEmail text
           )""")
		   
c.execute("INSERT INTO User VALUES (101, 'Wendy Smith', 'wednysmith@gmail.com')")

c.execute("INSERT INTO User VALUES (102, 'Harry Potter', 'harrypotter@gmail.com')")

c.execute("INSERT INTO User VALUES (103, 'Lucy Liu', 'lucyliu@gmail.com')")

c.execute("INSERT INTO User VALUES (104, 'Brandon Styles', 'brandonstyles@gmail.com')")

c.execute("""CREATE TABLE AssetType (
             typeID integer,
            
             typeName text
             )""")
			 
c.execute("INSERT INTO AssetType VALUES (001, 'Mobiles')")
c.execute("INSERT INTO AssetType VALUES (002, 'Laptops')")
c.execute("INSERT INTO AssetType VALUES (003, 'Tablets')")

c.execute("""CREATE TABLE Asset (
                 assetID integer,
				 typeID integer,
                 assettype text,
                 assetName text,
                 assetPurchaseDate text
                 )""")

c.execute("INSERT INTO Asset VALUES (101, 001, 'Mobiles', 'iPhone8Plus', '10.12.2018')")

c.execute("INSERT INTO Asset VALUES (120, 002, 'Laptops', 'Apple 11 MacBook Air', '02.10.2016')")

c.execute("INSERT INTO Asset VALUES (111, 003, 'Tablets', 'Microsoft Surface Pro 7', '01.10.2019')")

c.execute("INSERT INTO Asset VALUES (112, 003, 'Tablets', 'Samsung Galaxy Tab S5e', '26.12.2018')")

c.execute("INSERT INTO Asset VALUES (102, 001, 'Mobiles', 'Google Pixel 4', '05.12.2019')")

c.execute("""CREATE TABLE AssetMobile (
                 assetID integer,
                 typeID integer,
                 assetName text,
                 assetIEMI integer,
				 assetSIMPIN integer,
				 assetPhoneModel text
                 )""")

c.execute("INSERT INTO AssetMobile VALUES (101, 001, 'Mobiles', 320659036, 5621890567, 'iPhone8Plus')")

c.execute("INSERT INTO AssetMobile VALUES (102, 001, 'Mobiles', 321659036, 5621890421, 'Google Pixel 4')")

c.execute("INSERT INTO AssetMobile VALUES (103, 001, 'Mobiles', 322659036, 5621890419, 'Samsung Galaxy s10')")

c.execute("INSERT INTO AssetMobile VALUES (104, 001, 'Mobiles', 323659036, 5621890420, 'iPhone 11 Pro')")

c.execute("INSERT INTO AssetMobile VALUES (105, 001, 'Mobiles', 324659036, 5621890421, 'Samsung Galaxy Z Flip')")

c.execute("""CREATE TABLE AssetLaptops (
                 assetID integer,
                 typeID integer,
				 assetName text,
                 assetHardware text,
                 assetDevice text,
				 assetMake text,
				 assetSerialNo integer,
				 assetTag text
                 )""")

c.execute("INSERT INTO AssetLaptops VALUES (120, 002, 'Laptops', '6GB' , 'Apple 11 MacBook Air', 'Apple', 126790, 'JY8632J')")

c.execute("INSERT INTO AssetLaptops VALUES (121, 002, 'Laptops', '8GB' , 'ASUS ZenBook Pro', 'ASUS', 128130, 'JY4023J')")

c.execute("INSERT INTO AssetLaptops VALUES (122, 002, 'Laptops', '9GB' , 'Samsung Galaxy Book S 13.3 inch', 'Samsung', 128756, 'JY3043J')")

c.execute("INSERT INTO AssetLaptops VALUES (123, 002, 'Laptops', '8GB' , 'Microsoft Surface Laptop 3 13.5 inch', 'Microsoft', 126060, 'JY4050J')")

c.execute("INSERT INTO AssetLaptops VALUES (124, 002, 'Laptops', '9GB' , 'Apple 13 inch MacBook Air', 'Apple', 128120, 'JY6035J')")

c.execute("""CREATE TABLE AssetTablets (
                 assetID integer,
                 typeID integer,
				 assetName text,
                 assetDevice text,
				 assetMake text,
				 assetModel text,
				 assetSerialNo integer,
				 assetTag text,
				 assetIEMI integer,
				 assetPIN integer
                 )""")

c.execute("INSERT INTO AssetTablets VALUES (111, 003, 'Tablets', 'Microsoft Surface Pro 7' , 'Microsift', 'i5 8GB', 128260, 'JY5635J', 25165, 225)")

c.execute("INSERT INTO AssetTablets VALUES (112, 003, 'Tablets', 'Samsung Galaxy Tab S5e' , 'Samsung', '64GB 4G Black', 128261, 'JY5634J', 25166, 222)")

c.execute("INSERT INTO AssetTablets VALUES (113, 003, 'Tablets', 'Samsung Galaxy Tab S6 4G' , 'Samsung', '256GB Cloud Blue', 128262, 'JY5633J', 25167, 223)")

c.execute("INSERT INTO AssetTablets VALUES (114, 003, 'Tablets', 'Microsoft Surface Pro 7' , 'Microsift', 'i7 16GB', 128263, 'JY5636J', 25168, 224)")

c.execute("INSERT INTO AssetTablets VALUES (115, 003, 'Tablets', 'iPad Pro ' , 'Apple', '2020 11 inch', 128264, 'JY5632J', 25169, 221)")

c.execute("""CREATE TABLE AssetDetails(
                 assetDetailsID integer,
				 assetName text,
                 assetType text
                 )""")

c.execute("INSERT INTO ASsetDetails VALUES (1, 'iPhone8Plus', 'Mobiles')")

c.execute("INSERT INTO ASsetDetails VALUES (2, 'Microsoft Surface Pro 7', 'Tablets')")

c.execute("INSERT INTO ASsetDetails VALUES (3, 'Apple 11 MacBook Air', 'Laptops')")

c.execute("INSERT INTO ASsetDetails VALUES (4, 'Samsung Galaxy Tab S5e', 'Tablets')")

c.execute("INSERT INTO ASsetDetails VALUES (5, 'Google Pixel 4', 'Mobiles')")
