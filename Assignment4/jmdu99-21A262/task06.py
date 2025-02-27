# -*- coding: utf-8 -*-
"""Task06.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hSv61ejXESrp34CUz1PqZCsoA43tzc8y

**Task 06: Modifying RDF(s)**
"""

# !pip install rdflib 
github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2020-2021/master/Assignment4"

"""Leemos el fichero RDF de la forma que lo hemos venido haciendo"""

from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS
g = Graph()
g.namespace_manager.bind('ns', Namespace("http://somewhere#"), override=False)
g.namespace_manager.bind('vcard', Namespace("http://www.w3.org/2001/vcard-rdf/3.0#"), override=False)
g.parse(github_storage+"/resources/example5.rdf", format="xml")

"""Create a new class named Researcher"""

ns = Namespace("http://somewhere#")
g.add((ns.Researcher, RDF.type, RDFS.Class))
for s, p, o in g:
  print(s,p,o)

# **TASK 6.1: Create a new class named "University"

print("\nTASK 6.1: Create a new class named University")
g.add((ns.University, RDF.type, RDFS.Class))
for s, p, o in g:
  print(s,p,o)
  
# **TASK 6.2: Add "Researcher" as a subclass of "Person"**

print("\nTASK 6.2: Add Researcher as a subclass of Person")
g.add((ns.Researcher,RDFS.subClassOf,ns.Person))
for s, p, o in g:
  print(s,p,o)

# **TASK 6.3: Create a new individual of Researcher named "Jane Smith"**

print("\nTASK 6.3: Create a new individual of Researcher named Jane Smith")
g.add((ns.JaneSmith,RDF.type,ns.Researcher))
for s, p, o in g:
  print(s,p,o)
  
# **TASK 6.4: Add to the individual JaneSmith the fullName, given and family names**

print("\nTASK 6.4: Add to the individual JaneSmith the fullName, given and family names")
vcard = Namespace("http://www.w3.org/2001/vcard-rdf/3.0/")
g.add((ns.JaneSmith,vcard.FN,Literal("Jane Smith")))
g.add((ns.JaneSmith,vcard.Given,Literal("Jane")))
g.add((ns.JaneSmith,vcard.Family,Literal("Smith")))
for s, p, o in g:
  print(s,p,o)

# **TASK 6.5: Add UPM as the university where John Smith works**
print("\nTASK 6.5: Add UPM as the university where John Smith works")
g.add((ns.UPM,RDF.type,ns.University))
g.add((ns.UPM,vcard.FN,Literal("Universidad Politécnica de Madrid")))
g.add((ns.JohnSmith,ns.worksAt,ns.UPM))
for s, p, o in g:
  print(s,p,o)