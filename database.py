import sqlite3
conn = sqlite3.connect('diona.db')

c = conn.cursor()

c.execute("drop table Asset")

c.execute("""CREATE TABLE Asset (
                 assetID integer,
				 assetName text,
				 assetPurchaseDate text,
				 notes text,
				 assetType_type_id integer,
				 assetMobile_asset_id integer,
				 assetTablets_asset_id integer,
				 assetLaptop_asset_id integer,
                 assetDetails_asset_id integer 
                 )""")

c.execute("INSERT INTO Asset VALUES (101, 'iPhone8Plus', '10.12.2018', 'some scratches on the screen', 001, 101, 000, 000, 000)")

