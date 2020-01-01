# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 00:33:38 2019

@author: Siham chatir
"""

import networkx as nx
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()


def dijkstra(g,s):
    S1=[]
    S2=list(range(len(g)))
    poid=[float("inf") ]*len(g)
    poid[s]=0
    pred=[0]*len(g)
    while S2!=[]:
       #recherche du sommet à retirer de S2 

       min=poid[S2[0]]
       sommet=S2[0]
       for e in S2:
           if poid[e]<min:
               min=poid[e]
               sommet=e
       S2.remove(sommet)
       S1.append(sommet)
       #recherche des voisins (encore dans S2) du sommet retiré
       v=[]
       for j in range(len(g)):
           if g[sommet][j]!=None and j in S2:
               v.append(j)

#recalculer les poids des éléments de v
       for e in v:
           if poid[sommet]+g[sommet][e]<poid[e]:
               poid[e]=poid[sommet]+g[sommet][e]
               pred[e]=sommet
     #Designation du resultat de l'algorithme  
       G = nx.Graph()
       for i in range(0, len(pred)):
           G.add_edge(i, pred[i])
           
       plt.figure()
       nx.draw_networkx(G)
           
    return S1,pred,poid






