#!/usr/bin/python
import psycopg2
import csv
import pandas as pd


hostname = ''
username = ''
password = ''
database = ''




df = pd.read_csv('if.csv',sep='\t')
df = df[['ABHY0065001', 'RTGS-HO', 'ABHYUDAYA BANK BLDG., B.NO.71, NEHRU NAGAR, KURLA (E), MUMBAI-400024', 'MUMBAI', 'GREATER MUMBAI', 'MAHARASHTRA', '60']]
df = df.head(9000)
df.to_csv('if1.csv',sep='\t',index=False)





f = open('id1.csv', 'r')

def doQuery( conn ) :
    cur = conn.cursor()
    #x="CREATE TABLE banks1 (name character varying(49),id bigint NOT NULL);"
    #cur.copy_from(f, 'bankapi_bank', sep='\t')
    cur.copy_from(f, 'bankapi_bank', sep='\t')
    f.close()
    #cur.execute(x)
    conn.commit()
    cur.close()



myConnection = psycopg2.connect( host=hostname, user=username, password=password, dbname = database)
doQuery( myConnection )
myConnection.close()





#ifsc, bank_id, branch, address, city, district, state
f = open('if1.csv', 'r')

def doQuery( conn ) :
    cur = conn.cursor()
    cur.copy_from(f, 'bankapi_branch', sep='\t')
    f.close()
    #cur.execute(x)
    conn.commit()
    cur.close()



myConnection = psycopg2.connect( host=hostname, user=username, password=password, dbname = database)
doQuery( myConnection )
myConnection.close()



#
