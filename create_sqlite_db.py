import sqlite3

def create_tables():
    conn = sqlite3.connect('sqlite.db')
    c = conn.cursor()

    # PR_Project_Definition
    c.execute('''
    CREATE TABLE IF NOT EXISTS PR_Project_Definition (
        PR_Project_ID INTEGER PRIMARY KEY,
        PR_Contract_No TEXT,
        PR_Project_Name TEXT,
        PR_Project_Type TEXT,
        PR_Owner_Name TEXT,
        PR_Start_Date TEXT,
        PR_Finish_Date TEXT,
        PR_Status TEXT,
        PR_Remark TEXT
    )
    ''')

    # SD_System_Definition
    c.execute('''
    CREATE TABLE IF NOT EXISTS SD_System_Definition (
        SD_System TEXT,
        SD_Sub_System TEXT,
        SD_System_Name TEXT,
        SD_Subsystem_Name TEXT,
        SD_Type TEXT,
        SD_Status TEXT,
        SD_Priority TEXT,
        SD_Doc_Path TEXT,
        SD_Remark TEXT
    )
    ''')

    # WP_Work_Packages
    c.execute('''
    CREATE TABLE IF NOT EXISTS WP_Work_Packages (
        WP_ID INTEGER PRIMARY KEY,
        WP_Discipline_code TEXT,
        WP_TYPE_Code TEXT,
        WP_WBS_Code TEXT,
        WP_Planning_Cat TEXT,
        WP_Name TEXT,
        WP_Description TEXT,
        WP_Title TEXT,
        WP_Sub_System TEXT,
        WP_Priority TEXT,
        WP_Responsible TEXT,
        WP_Status TEXT,
        WP_Location TEXT,
        WP_Remark TEXT,
        WP_Doc_Path TEXT
    )
    ''')

    # WPT_Work_Packages_Types
    c.execute('''
    CREATE TABLE IF NOT EXISTS WPT_Work_Packages_Types (
        WPT_ID INTEGER PRIMARY KEY,
        WPT_Type TEXT,
        WPT_Prefix_Code TEXT,
        WPT_Description TEXT,
        WPT_Remark TEXT
    )
    ''')

    # AC_Activities
    c.execute('''
    CREATE TABLE IF NOT EXISTS AC_Activities (
        AC_ID INTEGER PRIMARY KEY,
        AC_WP_ID INTEGER,
        AC_ACT_ID INTEGER,
        AC_Responsibility_Discipline TEXT,
        AC_Description TEXT,
        AC_PLAN_Date TEXT,
        AC_FIN_NO TEXT,
        AC_FIN_Issue_Date TEXT,
        AC_FIN_Date TEXT,
        AC_Report_No TEXT,
        AC_Report_Date TEXT,
        AC_Result TEXT,
        AC_Report_Scan TEXT,
        AC_Document_Path TEXT,
        AC_Remark TEXT
    )
    ''')

    # ACT_Activity_Types
    c.execute('''
    CREATE TABLE IF NOT EXISTS ACT_Activity_Types (
        ACT_ID INTEGER PRIMARY KEY,
        ACT_Phase TEXT,
        ACT_Form_Code TEXT,
        ACT_Weight TEXT,
        ACT_Man_Hour TEXT,
        ACT_Activity_Name TEXT,
        ACT_Remark TEXT
    )
    ''')

    # Discipline_Definition
    c.execute('''
    CREATE TABLE IF NOT EXISTS Discipline_Definition (
        DS_ID INTEGER PRIMARY KEY,
        Discipline_Code TEXT,
        Discipline_Name TEXT
    )
    ''')

    # HP_Hold_Points
    c.execute('''
    CREATE TABLE IF NOT EXISTS HP_Hold_Points (
        HP_ID INTEGER PRIMARY KEY,
        HP_ACT_ID INTEGER,
        HP_Type TEXT,
        HP_Description TEXT,
        HP_Plan_Date TEXT,
        HP_Required_Action TEXT,
        HP_Status TEXT,
        HP_Punch_Type TEXT,
        HP_Respnsible TEXT,
        HP_Remark TEXT
    )
    ''')

    # PL_Punch_List
    c.execute('''
    CREATE TABLE IF NOT EXISTS PL_Punch_List (
        PL_Punch_ID INTEGER PRIMARY KEY,
        PL_Task_ID INTEGER,
        PL_Punch_Phase TEXT,
        PL_Punch_Description TEXT,
        PL_Punch_Date TEXT,
        PL_Issue_Date TEXT,
        PL_Plan_Date TEXT,
        PL_Plan_Status TEXT,
        PL_Plan_Description TEXT,
        PL_Plan_Done_date TEXT,
        PL_Release_By TEXT,
        PL_Remark TEXT
    )
    ''')

    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_tables()
    print("SQLite database 'sqlite.db' with tables created successfully.")
