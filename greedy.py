# -*- coding: utf-8 -*-
"""
Created on Sun Dec 04 00:57:02 2016

@author: Stephanie
"""

from graph2 import Graph
import time


if __name__ == "__main__":
    
    start = time.time()
    """g = { 1 : [2, 5, 6],
          2 : [1, 3, 8],
          3 : [2, 4, 10],
          4 : [3, 5, 12],
          5 : [1, 4, 14],
          6 : [1, 7, 15],
          7 : [6, 8, 17],
          8 : [2, 7, 9],
          9 : [8, 10, 18],
          10 : [3, 9, 11],
          11 : [10, 12, 19],
          12 : [11, 13, 4],
          13 : [12, 14, 20],
          14 : [13, 15, 5],
          15 : [14, 6, 16],
          16 : [15, 17, 20],
          17 : [7, 16, 18],
          18 : [17, 19, 9],
          19 : [18, 20, 11],
          20 : [13, 16, 19]
          
        }               """
    
    g = { 1: [2, 3, 4],
          2: [1, 5],
          3: [1, 4, 5],
          4: [1, 3, 6],
          5: [2, 3, 6],
          6: [4, 5]
    }
    
    graph = Graph(g)
    vertices = graph.vertices()
    grados = []
    numVertices = 0
    nodosAdyacentes = []
    nodosRecorridos = []
    gradoAdyacentes = []
    hamiltoniano = True
    
    nodoActual = None
    
    #creamos la lista de grados vacía pero 
    #con tantos elementos como vértices
    #Cada entrada contendrá el grado del nodo i, siendo i la posición
    #relativa en la lista
    for item in vertices: 
        grados.append([])
        numVertices = numVertices + 1
    
    
    #rellenamos la lista con los grados de cada vértice    
    for item in vertices:
        gradoVertices = graph.vertex_degree(item)
        grados[item-1] = gradoVertices
    
    #Setup inicial de la matriz de nodos adyacentes
    #Corresponde a todos los nodos
    for item in graph.vertices():
        nodosAdyacentes.append(item)
        
    gradoMaxGrafo = max(grados) + 10 #Valor para discriminación
    print("grados por nodo:", grados)
    print("numVertices:", numVertices)
    print("")
    
     
    
    #Configuramos la matriz de grados de nodos adyacentes
    #Pensando que todos los nodos son adyacentes a un estado inicial
    for item in grados:
        gradoAdyacentes.append(item)
    
    
    #El algoritmo se recorre como máximo tantas veces
    #como nodos tenga el grafo
    for i in range (0, numVertices): 
    
       estaEnNoRecorridos = False
       for item in nodosAdyacentes:
           if item not in nodosRecorridos:
               estaEnNoRecorridos = True
       
       if not estaEnNoRecorridos:
           print("No hay circuito Hamiltoniano")
           hamiltoniano = False
           break    
    
       #buscamos el nodo con grado mínimo de entra la lista
       #de nodos adyacentes
       gradoMinAdyacentes = min(gradoAdyacentes)
       print("Grado menor de los nodos adyacentes:", gradoMinAdyacentes)
              
    
       #buscamos el nodo con grado minimo
       contNodos = 0
       for item in gradoAdyacentes:
           contNodos = contNodos + 1
           if item == gradoMinAdyacentes:
               nodoActual = contNodos
               break
       
       #obtenemos los adyacentes al nodo actual
       nodosAdyacentes = []
       nodosAdyacentes = graph.adjacent(nodoActual)
       print("Nodo actual:", nodoActual)
       print("Nodos Adyacentes al nodo " + str(nodoActual) + ":", nodosAdyacentes)
       
       
       
       
       #agregamos el nodo actual a la lista de recorridos
       nodosRecorridos.append(nodoActual)
       print("Recorridos:", nodosRecorridos)
              
       
       
       #configuramos la matriz de grados adyacentes para que solo sean válidos los adyacentes
       for j in range(0, numVertices):
           
           if j + 1 not in nodosAdyacentes or j + 1 in nodosRecorridos:
               gradoAdyacentes[j] = gradoMaxGrafo
           else:
               gradoAdyacentes[j] = grados[j]
               
       
       #print("grado adyacentes:", gradoAdyacentes)
       print("")
       
         
    if hamiltoniano:
        primerNodo = nodosRecorridos[0]
        if primerNodo in nodosAdyacentes:
            nodosRecorridos.append(primerNodo)
            print("Existe al menos un circuito hamiltoniano:", nodosRecorridos)
        else:
            print("No hay circuito Hamiltoniano")
    
    print("Tarda", time.time()-start,"segundos") 
    
    
