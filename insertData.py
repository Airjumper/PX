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
    return cur.lastrowid


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

def create_asset(conn, asset):
    """
    Create a new asset into the Asset table
    :param conn:
    :param asset:
    :return: asset_id
    """
    sql = ''' INSERT INTO Asset(asset_name,asset_type)
              VALUES(?,?) '''
    cur = conn.cursor()
    cur.execute(sql, asset)
    return cur.lastrowid

def create_asset_details(conn, asset_details):
    """
    Create a new asset details into the Asset Details table
    :param conn:
    :param asset_details:
    :return:
    """
    sql = ''' INSERT INTO AssetDetails(asset_id,asset_IEMI, asset_make,asset_model,asset_pin,asset_serialNo,asset_phNo,asset_hardware,asset_tag,asset_device,asset_status,asset_purchaseDate,Notes)
              VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, asset_details)

def create_rent(conn, rent):
    """
    Create a new rent into the Rent table
    :param conn:
    :param rent:
    :return:
    """
    sql = ''' INSERT INTO rent(user_id,asset_id,date_rental,date_return)
              VALUES(?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, rent)

def create_site(conn, site):
    """
    Create a new site into the Site table
    :param conn:
    :param site:
    :return:
    """
    sql = ''' INSERT INTO site(site_location,site_address,site_device,device_name,serial,ip_address,mobile_no,sim,computer,PC_username,PC_password,printer,projectManager)
              VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, site)


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

        #create admin
        admin = (4552, 'password')
        create_admin(conn, admin)

        # create an asset
        asset = ('iPhone8Plus','Mobile')
        asset1 = ('Apple 11 MacBook Air', 'Laptop')
        asset2 = ('Microsoft Surface Pro 7','Tablet')

        asset_id = create_asset(conn, asset)

        #create asset details
        asset_details = (asset_id, 5621, 'Apple', 'iPhone8Plus', 321,'', '0452398568', '', '','iPhone8Plus Silver', 'rented for 3 times', 'repaired', '12/12/2019')
        create_asset_details(conn, asset_details)

        user_id = create_user(conn, user)

        #create Rent
        rent = (user_id, asset_id, '13/12/2019', '20/12/2019')
        create_rent(conn, rent)

        #create Site
        site = ('NSW' , '3 rose st, Merryland', 'iPhone8Plus 4 inch', 'iPhone8Plus Silver', '','61.69.208.121','0452398568',211,1234,'Taron','taron1234', 311, 'Taron')
        create_site(conn, site)

        
       
if __name__ == '__main__':
    main()