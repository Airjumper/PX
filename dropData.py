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


#Delete a user from User Table by user id
def delete_user(conn, user_id):
    """
    Delete a user by user_id 
    :param conn:  Connection to the SQLite database
    :param id: user_id  of the user
    :return:
    """
    sql = 'DELETE FROM User WHERE user_id=?'
    cur = conn.cursor()
    cur.execute(sql, (user_id,))
    conn.commit()

#Delete an asset type from Asset Type Table by type_id
def delete_asset_type(conn, type_id):
    """
    Delete an asset type by type_id 
    :param conn:  Connection to the SQLite database
    :param id: type_id  of the asset_type
    :return:
    """
    sql = 'DELETE FROM AssetType WHERE type_id=?'
    cur = conn.cursor()
    cur.execute(sql, (type_id,))
    conn.commit()

def main():
    database = r"diona.db"

    # create a database connection
    conn = create_connection(database)
    with conn:
        #delete the user from the User Table that the user_id is 4
        #delete_user(conn, 4);

        #delete the asset type from the AssetType Table
        delete_asset_type(conn, 4);

if __name__ == '__main__':
    main()