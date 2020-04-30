import sqlite3
conn = sqlite3.connect('diona.db')

c = conn.cursor()

c.execute("""CREATE TABLE Asset (
                 assetID integer,
				 assetName text,
				 assetPurchaseDate text,
				 notes blob,
				 assetType_type_id integer,
				 assetMobile_asset_id integer,
				 assetTablets_asset_id integer,
				 assetLaptop_asset_id integer,
                 assetDetails_asset_id integer 
                 )""")

c.execute("INSERT INTO Asset VALUES (101, 'iPhone8Plus', '10.12.2018', 'some scratches on the screen', 001, 101, null, null, null)")

c.execute("INSERT INTO Asset VALUES (120, 'Apple 11 MacBook Air', '02.10.2016', 'some keyboard buttons faded out', 002, null, null, 120, null)")

c.execute("INSERT INTO Asset VALUES (111, 'Microsoft Surface Pro 7', '01.10.2019', 'in good condition', 003, null, 111, null, null)")

c.execute("INSERT INTO Asset VALUES (112, 'Samsung Galaxy Tab S5e', '26.12.2018', 'some scratches on the screen', 003, null, 112, null, null)")

c.execute("INSERT INTO Asset VALUES (102, 'Google Pixel 4', '05.12.2019', 'in good condition', 001, 102, null, null, null)")

