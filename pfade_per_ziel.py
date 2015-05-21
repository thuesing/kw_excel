#!/usr/bin/env python 
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 11:25:45 2015

@author: thuesing
"""
from py2neo import Graph
import xlwt, sys, traceback

cols = 'zielA,massnahme,verhalten,ursache,problem,zielB,value,descr'
cols = cols.split(',')
# 1 zu n Ziele
query = "MATCH (z:Ziel {name:{N}}), pfad=(z)-->(m:Massnahme)-->(v:Verhalten)-[vu:Kante]->(u:Ursache)-->(p:Problem)-->(ze:Ziel) \
WHERE vu.value=1 RETURN z.name AS zielA, m.name AS massnahme, \
v.name AS verhalten , u.name AS ursache, p.name AS problem, \
ze.name AS zielB , vu.value AS value, vu.descr AS descr;"
graph = Graph()

def main():
    try:
    	ziele()
    	#spreadsheet_for('POPs - Beendigung / Einschränkung')
    except Exception:
        traceback.print_exc(file=sys.stdout)
    sys.exit(0)

def ziele():
	for ziel in graph.cypher.execute("MATCH (z:Ziel) RETURN z.name AS name"):
		#print ziel.name.encode('utf-8')
		spreadsheet_for(ziel.name.encode('utf-8'))

def spreadsheet_for(name):
	workbook = xlwt.Workbook() 
	sheet = workbook.add_sheet("Pfade") 
	# column names
	for i in range(len(cols)):
		sheet.write(0, i, cols[i]) # row, column, value

	count_rows = 0
	for record in graph.cypher.execute(query, {"N": name}):
			#print record.zielB.encode('utf-8')
			count_rows += 1
			for i in range(len(cols)):
 				sheet.write(count_rows, i, record[cols[i]]) # row, column, value

 	name = name.replace('/', '_')
 	workbook.save('data/' + name + '.Pfade.xls')
 	print 'Wrote ' + name + '.Pfade.xls'

main()