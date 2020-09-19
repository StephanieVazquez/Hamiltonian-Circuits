# -*- coding: utf-8 -*-
"""
Created on Sat Dec 03 14:11:06 2016

@author: Stephanie
"""

import itertools
import time

#from graph2 import Graph

if __name__ == '__main__':
     start = time.time()
     """g = { "1" : ["2", "5", "6"],
          "2" : ["1", "3", "8"],
          "3" : ["2", "4", "10"],
          "4" : ["3", "5", "12"],
          "5" : ["1", "4", "14"],
          "6" : ["1", "7", "15"],
          "7" : ["6", "8", "17"],
          "8" : ["2", "7", "9"],
          "9" : ["8", "10", "18"],
          "10" : ["3", "9", "11"],
          "11" : ["10", "12", "19"],
          "12" : ["11", "13", "4"],
          "13" : ["12", "14", "20"],
          "14" : ["13", "15", "5"],
          "15" : ["14", "6", "16"],
          "16" : ["15", "17", "20"],
          "17" : ["7", "16", "18"],
          "18" : ["17", "19", "9"],
          "19" : ["18", "20", "11"],
          "20" : ["13", "16", "19"]
          
        } """        
     
     
     """g = { "1" : ["2", "4"],
          "2" : ["1", "3"],
          "3" : ["4", "5"],
          "5" : ["3", "4"],
          "4" : ["3"]
          
        }    
     """  
     g = { "1": ["2", "3", "4"],
          "2": ["1", "5"],
          "3": ["1", "4", "5"],
          "4": ["1", "3", "6"],
          "5": ["2", "3", "6"],
          "6": ["4", "5"]
    }
    
     #graph = Graph(g)
     #nodos = list(graph.vertices())
     nodos = list(g.keys())
     
     perm = itertools.permutations(nodos)
     listaPermutaciones = []
     
     for item in perm:
         permutacion = list(item)
         firstNode = permutacion[0]
         permutacion = permutacion + list(firstNode)
         listaPermutaciones.append(permutacion)
         
     
     alMenosUnCamino = False
     for camino in listaPermutaciones:
        #Checar que cada camino sea hamiltoniano
        lenVector = len(camino)
        
        hamilton = True
        
        for x in range(0, lenVector-1):
            nodoInicial = camino[x]
            nodoFinal = camino[x+1]
            if nodoFinal not in g[nodoInicial]:
                hamilton = False
        if hamilton:
            print("Circ. Ham.:", camino)
            alMenosUnCamino = True
            
     if not alMenosUnCamino:
            print("No hay circuitos hamiltonianos")
     print("Tarda", time.time()-start,"segundos")       
