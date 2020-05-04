import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def create_user(conn, user):
    """
    Create a new user into the User table
    :param conn:
    :param user:
    :return: user id
    """
    sql = ''' INSERT INTO User(user_name,user_email)
              VALUES(?,?) '''
    cur = conn.cursor()
    cur.execute(sql, user)
    #return cur.lastrowid


def create_admin(conn, admin):
    """
    Create a new admin into the Admin table
    :param conn:
    :param admin:
    :return:
    """
    sql = ''' INSERT INTO Admin(id,password)
              VALUES(?,?) '''
    cur = conn.cursor()
    cur.execute(sql, admin)

def create_asset_type(conn, asset_type):
    """
    Create a new asset type into the AssetType table
    :param conn:
    :param asset_type:
    :return: asset_type id
    """
    sql = ''' INSERT INTO AssetType(type_name)
              VALUES(?) '''
    cur = conn.cursor()
    cur.execute(sql, [asset_type])
    #return cur.lastrowid

def create_admin(conn, admin):
    """
    Create a new admin into the Admin table
    :param conn:
    :param admin:
    :return:
    """
    sql = ''' INSERT INTO Admin(id,password)
              VALUES(?,?) '''
    cur = conn.cursor()
    cur.execute(sql, admin)

def create_asset_mobile(conn, asset_mobile):
    """
    Create a new asset mobile into the AssetMobiles table
    :param conn:
    :param asset_mobile:
    :return:
    """
    sql = ''' INSERT INTO AssetMobiles(asset_IEMI,asset_SIMPIN,asset_phoneModel)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, asset_mobile)

def create_asset_tablet(conn, asset_tablet):
    """
    Create a new asset tablet into the AssetTablets table
    :param conn:
    :param asset_tablet:
    :return:
    """
    sql = ''' INSERT INTO AssetTablets(asset_device,asset_make,asset_model,asset_serialNumber,asset_tag,asset_IEMI,asset_PIN)
              VALUES(?,?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, asset_tablet)

def create_asset_laptop(conn, asset_laptop):
    """
    Create a new laptop tablet into the AssetLaptops table
    :param conn:
    :param asset_tablet:
    :return:
    """
    sql = ''' INSERT INTO AssetLaptops(asset_hardware,asset_device,asset_make,asset_serialNumber,asset_tag)
              VALUES(?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, asset_laptop)

def create_asset_record(conn, asset_record):
    """
    Create a new asset into the Asset table
    :param conn:
    :param asset_record:
    :return:
    """
    sql = ''' INSERT INTO Asset(asset_name,asset_purchaseDate,Notes,Asset_Type_type_id,Asset_Mobile_asset_id,Asset_Tablets_asset_id,Asset_Laptop_asset_id,Asset_Details_asset_id)
              VALUES(?,?,?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, asset_record)

def create_asset_user_record(conn, asset_user_record):
    """
    Create a new asset_has_user record into the AssetHasUser table
    :param conn:
    :param asset_user_record:
    :return:
    """
    sql = ''' INSERT INTO AssetHasUser(asset_id,user_id,date_rental,date_return,Notes)
              VALUES(?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, asset_user_record)

def main():
    database = r"diona.db"

    # create a database connection
    conn = create_connection(database)
    with conn:
        # create a new user
        user = ('Wendy Smith', 'wednysmith@gmail.com')
        user2 = ('Harry Potter', 'harrypotter@gmail.com')
        user3 = ('Lucy Liu', 'lucyliu@gmail.com')
        user4 = ('Brandon Styles', 'brandonstyles@gmail.com')
        create_user(conn, user)
        #create_user(conn, user2)
        #create_user(conn, user3)
        #create_user(conn, user4)

        #create admin
        #admin = (4552, 'taron1234')
        #create_admin(conn, admin)

         # create an asset type
        asset_type = ('Mobile')
        asset_type2 = ('Laptop')
        asset_type3 = ('Tablet')
        asset_type_id = create_asset_type(conn, asset_type)
        #create_asset_type(conn, asset_type)
        #create_asset_type(conn, asset_type2)
        #create_asset_type(conn, asset_type3)
        
        #create asset mobile
        #asset_mobile = (320659036, 5621890567, 'iPhone8Plus')
        #create_asset_mobile(conn, asset_mobile)

        #create asset tablet
        asset_tablet = ('Microsoft Surface Pro 7' , 'Microsift', 'i5 8GB', 128260, 'JY5635J', 25165, 225)
        create_asset_tablet(conn, asset_tablet)

        #create asset laptops
        #asset_laptop = ('6GB' , 'Apple 11 MacBook Air', 'Apple', 126790, 'JY8632J')
        #create_asset_laptop(conn, asset_laptop)

        #create asset details
        
        #create asset records
        #asset_record = ('iPhone8Plus', '10.12.2018', 'some scratches on the screen', 1, 1, '', '', '')
        #create_asset_record(conn, asset_record)

        #create asset has user
        #asset_user_record = (1, 1, '2020-01-22 09:00:00.000', '2020-02-22 09:00:00.000', 'late return')
        #create_asset_user_record(conn, asset_user_record)

if __name__ == '__main__':
    main()