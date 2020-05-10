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
    database = r"diona.db"

    sql_create_user_table = """ CREATE TABLE IF NOT EXISTS `User` (
                                        `user_id` integer,
                                        `user_name` TEXT NOT NULL,
                                        `user_email` TEXT NOT NULL,
                                        PRIMARY KEY (`user_id`)
                                    ); """

    
    sql_create_asset_table = """ CREATE TABLE IF NOT EXISTS `Asset` (
                                            `asset_id` integer,
                                            `asset_name` TEXT NOT NULL,
                                            `asset_type` TEXT NOT NULL,
                                            PRIMARY KEY (`asset_id`)); """

    sql_create_asset_details_table = """ CREATE TABLE IF NOT EXISTS `AssetDetails` (
                                    `asset_detailsID` integer,
                                    `asset_id` integer NOT NULL,
                                    `asset_IEMI` TEXT NULL,
                                    `asset_make` TEXT NULL,
                                    `asset_model` TEXT NULL,
                                    `asset_pin` integer NULL,
                                    `asset_serialNo` integer NULL,
                                    `asset_phNo` integer NULL,
                                    `asset_hardware` TEXT NULL,
                                    `asset_tag` TEXT NULL,
                                    `asset_device` TEXT NULL,
                                    `asset_status` TEXT NULL,
                                    `asset_purchaseDate` TEXT NULL,
                                    `Notes` BLOB NULL,
                                    PRIMARY KEY (`asset_detailsID`),
                                    CONSTRAINT `fk_Asset_asset_id`
                                        FOREIGN KEY (`asset_id`)
                                        REFERENCES `Asset` (`asset_id`)
                                        ON DELETE NO ACTION
                                        ON UPDATE NO ACTION); """

    sql_create_admin_table = """ CREATE TABLE IF NOT EXISTS `Admin` (
                                    `id` integer NOT NULL,
                                    `password` TEXT NULL,
                                    PRIMARY KEY (`id`)); """

    sql_create_rent_table = """ CREATE TABLE IF NOT EXISTS Rent (
                                            `rent_id` integer NOT NULL,
                                            `user_id` integer NOT NULL,
                                            `asset_id` integer NOT NULL,
                                            `date_rental` TEXT NULL,
                                            `date_return` TEXT NULL,
                                            PRIMARY KEY (`rent_id`),
                                            FOREIGN KEY (`asset_id`) REFERENCES `Asset` (`asset_id`),
                                            FOREIGN KEY (`user_id`) REFERENCES `User` (`user_id`)); """    

    sql_create_site_table = """ CREATE TABLE IF NOT EXISTS Site (
                                            `site_id` integer NOT NULL,
                                            `site_location` TEXT NULL,
                                            `site_address` TEXT NULL,
                                            `site_device` TEXT NULL,
                                            `device_name` TEXT NULL,
                                            `serial` INTEGER NULL,
                                            `ip_address` TEXT NULL,
                                            `mobile_no` INTEGER NULL,
                                            `sim` INTEGER NULL,
                                            `computer` TEXT NULL,
                                            `PC_username` TEXT NULL,
                                            `PC_password` TEXT NULL,
                                            `printer` TEXT NULL,
                                            `projectManager` TEXT NULL,
                                            PRIMARY KEY (`site_id`)); """    


    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        # create user table
        create_table(conn, sql_create_user_table)

        # # create asset table
        create_table(conn, sql_create_asset_table)

        # # create asset details table
        create_table(conn, sql_create_asset_details_table)

        # # create admin table
        create_table(conn, sql_create_admin_table)

        # # create rent table
        create_table(conn, sql_create_rent_table)

        #  # create site table
        create_table(conn, sql_create_site_table)
    else:
        print("Error! cannot create the database connection.")


if __name__ == '__main__':
    main()