#!/usr/bin/python
import psycopg2
import csv


hostname = 'ec2-54-243-47-196.compute-1.amazonaws.com'
username = 'belcxwhmvoskmv'
password = 'aed79670385686eadee6afe4d13efac16bf37cb196d32cf2dbf833d31037e37f'
database = 'd5bt2r3nq1onrl'


"""

f = open('id.csv', 'r')

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


"""


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
