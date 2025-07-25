'''
Counting Organizations
This application will read the mailbox data (mbox.txt) and count the number of email messages 
per organization (i.e. domain name of the email address) using a database with the following 
schema to maintain the counts.

CREATE TABLE Counts (org TEXT, count INTEGER)
When you have run the program on mbox.txt upload the resulting database file above 
for grading.
If you run the program multiple times in testing or with different files, make sure 
to empty out the data before each run.

Python for Everybody: Exploring Data Using Python 3
by Charles R. Severance
'''

import sqlite3

conn = sqlite3.connect('orgdb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox-short.txt' #press enter key to automatically run mbox-short
fh = open(fname)
for line in fh:
    #loop through file
    if not line.startswith('From: '): continue
        #only get orgs
    pieces = line.split('@')
    #no strip, since split takes care of that
    org = pieces[1]
    #grab email part we care about
    
    #start database stuff, kind of like a dict
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org,))
    #? as placeholder, prevents SQL injection, opens record set, reads like file
    row = cur.fetchone()
    #only grab first one, row will be info we get from datab
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count)
                VALUES (?, 1)''', (org,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                    (org,))
        #should always use update w dbs
    conn.commit()
    
# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()
