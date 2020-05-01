import sqlite3
from _sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn

def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def main():

    sql_create_user_table = """ CREATE TABLE IF NOT EXISTS `User` (
                                        `user_id` integer,
                                        `user_name` TEXT NULL,
                                        `user_email` TEXT NULL,
                                        PRIMARY KEY (`user_id`)
                                    ); """

    sql_create_asset_type_table = """CREATE TABLE IF NOT EXISTS `AssetType` (
                                        `type_id` integer,
                                        `type_name` TEXT NULL,
                                        PRIMARY KEY (`type_id`)
                                );"""

    sql_create_asset_mobile_table = """ CREATE TABLE IF NOT EXISTS `AssetMobiles` (
                                    `asset_id` integer,
                                    `asset_IEMI` TEXT NULL,
                                    `asset_SIMPIN` TEXT NULL,
                                    `asset_phoneModel` TEXT NULL,
                                    PRIMARY KEY (`asset_id`)); """

    sql_create_asset_tablets_table = """ CREATE TABLE IF NOT EXISTS `AssetTablets` (
                                            `asset_id` integer,
                                            `asset_device` TEXT NULL,
                                            `asset_make` TEXT NULL,
                                            `asset_model` TEXT NULL,
                                            `asset_serialNumber` TEXT NULL,
                                            `asset_tag` TEXT NULL,
                                            `asset_IEMI` TEXT NOT NULL,
                                            `asset_PIN` TEXT NOT NULL,
                                            PRIMARY KEY (`asset_id`)); """

    sql_create_asset_laptops_table = """ CREATE TABLE IF NOT EXISTS `AssetLaptops` (
                                            `asset_id` integer,
                                            `asset_hardware` TEXT NULL,
                                            `asset_device` TEXT NULL,
                                            `asset_make` TEXT NULL,
                                            `asset_serialNumber` integer,
                                            `asset_tag` TEXT NULL,
                                            PRIMARY KEY (`asset_id`)); """

    sql_create_asset_details_table = """ CREATE TABLE IF NOT EXISTS `AssetDetails` (
                                            `asset_id` integer,
                                            PRIMARY KEY (`asset_id`)); """

    sql_create_asset_table = """ CREATE TABLE IF NOT EXISTS `Asset` (
                                    `asset_id` integer,
                                    `asset_name` TEXT NULL,
                                    `asset_purchaseDate` TEXT NULL,
                                    `Notes` BLOB NULL,
                                    `Asset_Type_type_id` integer NOT NULL,
                                    `Asset_Mobile_asset_id` integer NULL,
                                    `Asset_Tablets_asset_id` integer NULL,
                                    `Asset_Laptop_asset_id` integer NULL,
                                    `Asset_Details_asset_id` integer NULL,
                                    PRIMARY KEY (`asset_id`),
                                    CONSTRAINT `fk_Asset_Asset Type1`
                                        FOREIGN KEY (`Asset_Type_type_id`)
                                        REFERENCES `AssetType` (`type_id`)
                                        ON DELETE NO ACTION
                                        ON UPDATE NO ACTION,
                                    CONSTRAINT `fk_Asset_Asset Mobile1`
                                        FOREIGN KEY (`Asset_Mobile_asset_id`)
                                        REFERENCES `AssetMobiles` (`asset_id`)
                                        ON DELETE NO ACTION
                                        ON UPDATE NO ACTION,
                                    CONSTRAINT `fk_Asset_Asset Tablets1`
                                        FOREIGN KEY (`Asset_Tablets_asset_id`)
                                        REFERENCES `AssetTablets` (`asset_id`)
                                        ON DELETE NO ACTION
                                        ON UPDATE NO ACTION,
                                    CONSTRAINT `fk_Asset_Asset Laptop1`
                                        FOREIGN KEY (`Asset_Laptop_asset_id`)
                                        REFERENCES `AssetLaptops` (`asset_id`)
                                        ON DELETE NO ACTION
                                        ON UPDATE NO ACTION,
                                    CONSTRAINT `fk_Asset_Asset Details1`
                                        FOREIGN KEY (`Asset_Details_asset_id`)
                                        REFERENCES `AssetDetails` (`asset_id`)
                                        ON DELETE NO ACTION
                                        ON UPDATE NO ACTION); """

    sql_create_admin_table = """ CREATE TABLE IF NOT EXISTS `Admin` (
                                    `id` integer NOT NULL,
                                    `password` TEXT NULL,
                                    PRIMARY KEY (`id`)); """

    sql_create_asset_has_user_table = """ CREATE TABLE IF NOT EXISTS AssetHasUser (
                                            `asset_id` integer NOT NULL,
                                            `user_id` integer NOT NULL,
                                            `date_rental` TEXT NULL,
                                            `date_return` TEXT NULL,
                                            `Notes` BLOB NULL,
                                            PRIMARY KEY (`asset_id`, `user_id`),
                                            FOREIGN KEY (`asset_id`) REFERENCES `Asset` (`asset_id`),
                                            FOREIGN KEY (`user_id`) REFERENCES `User` (`user_id`)); """    

    

    # create a database connection
    conn = create_connection(r"diona.db")
    # create tables
    if conn is not None:
        # create user table
        create_table(conn, sql_create_user_table)
        # create asset type table
        create_table(conn, sql_create_asset_type_table)
        # create asset mobile table
        create_table(conn, sql_create_asset_mobile_table)
        # create asset tablets table
        create_table(conn, sql_create_asset_tablets_table)
        # create asset laptops table
        create_table(conn, sql_create_asset_laptops_table)
        #   create asset details table
        create_table(conn, sql_create_asset_details_table)
        # create asset table
        create_table(conn, sql_create_asset_table)
        # create admin table
        create_table(conn, sql_create_admin_table)
        # create asset has user table
        create_table(conn, sql_create_asset_has_user_table)
    else:
        print("Error! cannot create the database connection.")


if __name__ == '__main__':
    main()