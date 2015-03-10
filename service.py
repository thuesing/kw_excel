#!/usr/bin/env python 
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 11:25:45 2015

@author: thuesing
"""
from py2neo import Graph
graph = Graph()
for record in graph.cypher.execute("MATCH (z:Ziel) RETURN z.name AS name"):
	print(record.name.encode('utf-8'))
