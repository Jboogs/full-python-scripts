

import sqlite3

conn = sqlite3.connect('file_database.db')
file_list = ('information.docx', 'Hello.txt', 'myImage.png', \
             'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_text_files ( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_file_name TEXT \
        )")
    #this commits the instructions you performed during the db connection
    conn.commit()
# this closes the database after you commit the changes


def txt_finder():
    text_files = []
    for file in file_list:
        if file.endswith('.txt'):
            text_files.append(file)
    return text_files

def add_data():
    txt_file_list = txt_finder()
    for item in txt_file_list:
        cur.execute('INSERT INTO tbl_text_files (col_file_name) VALUES(?)', (item,))
    conn.commit()

def query_function():
    cur.execute('SELECT * FROM tbl_text_files')
    var_file = cur.fetchall() #this will fetch all the information (other wise use fetchone()
    # iterate through the new created tuple and save it in a formated string msg
    for item in var_file:
        print(item)
    conn.close()
        
    
        






if __name__ == '__main__':
    add_data()
    query_function()
