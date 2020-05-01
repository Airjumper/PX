import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

#update Table User
def update_user(conn, user):
    """
    user_id, user_name, and user_email
    :param conn:
    :param user:
    :return: user id
    """
    sql = ''' UPDATE User
              SET user_name = ? ,
                  user_email = ?
              WHERE user_id = ?'''
    cur = conn.cursor()
    cur.execute(sql, user)
    conn.commit()

#Update Table Asset Type
def update_asset_type(conn, asset_type):
    """
    type_id and type_name
    :param conn:
    :param asset_type:
    :return: type_id
    """
    sql = ''' UPDATE AssetType
              SET type_name = ? 
              WHERE type_id = ?'''
    cur = conn.cursor()
    cur.execute(sql, asset_type)
    conn.commit()

#Update Table Asset Mobile
def update_asset_mobile(conn, asset_mobile):
    """
    asset_id, asset_IEMI, asset_SIMPIN and asset_phoneModel
    :param conn:
    :param asset_mobile:
    :return: asset_id
    """
    sql = ''' UPDATE AssetMobiles
              SET asset_IEMI = ?,
                   asset_SIMPIN = ?,
                   asset_phoneModel = ? 
              WHERE asset_id = ?'''
    cur = conn.cursor()
    cur.execute(sql, asset_mobile)
    conn.commit()

#Update Table Asset Tablets
def update_asset_tablets(conn, asset_tablets):
    """
    asset_id, asset_device, asset_make, asset_model, asset_serialNumber, asset_tag, asset_IEMI and asset_PIN
    :param conn:
    :param asset_tablets:
    :return: asset_id
    """
    sql = ''' UPDATE AssetTablets
              SET asset_device = ?,
                   asset_make = ?,
                   asset_model = ?, 
                   asset_serialNumber = ?,
                   asset_tag = ?, 
                   asset_IEMI = ?,
                   asset_PIN = ? 
              WHERE asset_id = ?'''
    cur = conn.cursor()
    cur.execute(sql, asset_tablets)
    conn.commit()

#Update Table Asset Laptops
def update_asset_laptops(conn, asset_laptops):
    """
    asset_id, asset_hardware, asset_device, asset_make, asset_serialNumber and asset_tag
    :param conn:
    :param asset_tablets:
    :return: asset_id
    """
    sql = ''' UPDATE AssetLaptops
              SET asset_hardware = ?,
                   asset_device = ?,
                   asset_make = ?, 
                   asset_serialNumber = ?,
                   asset_tag = ? 
              WHERE asset_id = ?'''
    cur = conn.cursor()
    cur.execute(sql, asset_laptops)
    conn.commit()

#Update Table Asset
def update_asset(conn, asset):
    """
    asset_id, asset_name, asset_purchaseDate, Notes, Asset_Type_type_id, Asset_Mobile_asset_id, 
    Asset_Tablets_asset_id, Asset_Laptop_asset_id, and Asset_Details_asset_id
    :param conn:
    :param asset:
    :return: asset id
    """
    sql = ''' UPDATE Asset
              SET asset_name = ?, 
              asset_purchaseDate = ?, 
              Notes = ?, 
              Asset_Type_type_id = ?, 
              Asset_Mobile_asset_id = ?, 
              Asset_Tablets_asset_id = ?, 
              Asset_Laptop_asset_id = ?,
              Asset_Details_asset_id = ?
              WHERE asset_id = ?'''
    cur = conn.cursor()
    cur.execute(sql, asset)
    conn.commit()

#update Table Admin
def update_admin(conn, admin):
    """
    id and password
    :param conn:
    :param user:
    :return: id
    """
    sql = ''' UPDATE Admin
              SET password = ? 
              WHERE id = ?'''
    cur = conn.cursor()
    cur.execute(sql, admin)
    conn.commit()

#Update Table Asset Has User
def update_asset_has_user(conn, asset_has_user):
    """
    asset_id, user_id, date_rental, date_return and Notes
    :param conn:
    :param asset:
    :return: asset_id
    """
    sql = ''' UPDATE AssetHasUser
              SET 
                  date_rental = ?, 
                  date_return = ?,
                  Notes = ?
              WHERE asset_id = ? AND user_id = ?'''
    cur = conn.cursor()
    cur.execute(sql, asset_has_user)
    conn.commit()
    #return cur.lastrowid

def main():
    database = r"diona.db"

    # create a database connection
    conn = create_connection(database)
    with conn:
        #update_user(conn, ('Wendy Chun', 'wendychun@yahoo.com', 1))

        update_asset_type(conn, ('Tablets', 3))

        #update_asset_mobile(conn, (320659036, 5621890567, 'iPhonePro11', 1))

        #update_asset_tablets(conn, ('Microsoft Surface Pro 7' , 'Microsoft', 'i5 10GB', 128260, 'JY5635J', 25165, 225, 1))

        #update_asset_laptops(conn, ('8GB' , 'Apple 11 MacBook Air', 'Apple', 126790, 'JY8632J', 1))

        #update_asset(conn, ('iPhone10', '10.12.2019', 'few scratches on the screen', 1, 1, '', '', '', 1))

        #update_admin(conn, ('taron1256', 4552))

        #update_asset_has_user(conn, ('2020-01-22 09:00:00.000', '2020-02-22 09:00:00.000', 'late return', 1, 1))

if __name__ == '__main__':
    main()