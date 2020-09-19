# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 11:16:09 2016

@author: Stephanie
"""
import time
 
class Vertex(object):
    def __init__(self, node, *nodeList):
        self.i = node
        self.nodeList = list(nodeList)
 
    def __hash__(self):
        return self.i
 
    def reaches(self, vertex):
        ''' Can receive an integer or a Vertex
        '''
        if isinstance(vertex, int):
            return vertex in self.nodeList
 
        return self.reaches(vertex.i)
 
    def __str__(self):
        return '<' + str(self.i) + '>'
 
    def __repr__(self):
        return self.__str__()
 
 
class Graph(object):
    def __init__(self):
        self.vList = {}
 
    def add(self, node, *nodeList):
        vertex = Vertex(node, *nodeList)
        self.vList[node] = vertex
 
    def hamiltonian(self, current = None, pending = None, destiny = None):
        ''' Returns a list of nodes which represent
        a hamiltonian path, or None if not found
        ''' 
        
        ##print("vList.values():", self.vList.values())
        print("Nodo Actual", current)        
        print("Nodos pend.:",pending)
        
        
        if pending is None:
            pending = self.vList.values()
 
        result = None
 
        if current is None:
            iteracion = 1
            
            for current in pending: # Este ciclo recorre los nodos de inicio
                #print("iteracion:", iteracion)
                iteracion = iteracion + 1
                
                #print("primera vuelta")
                result = self.hamiltonian(current, [x for x in pending if x is not current], current)
                #print("primer bloque")
                if result is not None:
                    #print("lo quebre")
                    break
        else:
            if pending == []: ## Si ya no quedan nodos pendientes de recorrer
                print("Nodo Inicial:", destiny)
                print("Nodo actual:", current)
                if current.reaches(destiny): ## Si el nodo actual se conecta con el de origen
                    print("cierra circuito")
                    print("")
                    return [current]
                else:
                    print("No cierra circuito")
                    print("")
                    return None
           
            for x in [self.vList[v] for v in current.nodeList]: ##por cada uno de los adyacentes
                if x in pending: ## si el adyacente no está visitado
                    #print("segundo bloque")
                    result = self.hamiltonian(x, [y for y in pending if y is not x], destiny)
                    if result is None:
                        
                        print("Regreso al nodo:", current)
                    if result is not None:
                        #print("result:", result)
                        result = [current] + result
                        break    
            #print("regreso uno")
        
        return result
 
if __name__ == '__main__':
    start = time.time()
  
    G = Graph() 
    """G.add(1, 184, 86, 137, 191, 167, 3, 147, 143, 109)
    G.add(2, 1, 3, 8)
    G.add(3, 2, 4, 10)
    G.add(4, 3, 5, 12)
    G.add(5, 1, 4, 14)
    G.add(6, 1, 7, 15)
    G.add(7, 6, 8, 17)
    G.add(8, 2, 7, 9)
    G.add(9, 8, 10, 18)
    G.add(10, 3, 9, 11)
    G.add(11, 10, 12, 19)
    G.add(12, 11, 13, 4)
    G.add(13, 12, 14, 20)
    G.add(14, 13, 15, 5)
    G.add(15, 14, 6, 16)
    G.add(16, 15, 17, 20)
    G.add(17, 7, 16, 18)
    G.add(18, 17, 19, 9)
    G.add(19, 18, 20, 11)
    G.add(20, 13, 16, 19 )"""
    
    """ G.add(1, 3, 5)
    G.add(2, 3, 5)
    G.add(3, 1, 2, 4)
    G.add(4, 3, 6)
    G.add(5, 1, 2, 6)
    G.add(6, 4, 5)"""
    
    G.add(1, 2, 3, 4)
    G.add(2, 1, 5)
    G.add(3, 1, 4, 5)
    G.add(4, 1, 3, 6)
    G.add(5, 2, 3, 6)
    G.add(6, 5, 4)
    
    """G.add(1, 2)
    G.add(2, 3)
    G.add(3, 4)
    G.add(4, 1)"""
    
    
    """G.add('a','b')
    G.add('b','c')
    G.add('c','d')
    G.add('d','a')"""
    
    """G.add(1, 2, 3, 4)
    G.add(2, 1, 5)
    G.add(3, 1, 4, 5)
    G.add(4, 1, 3, 6)
    G.add(5, 2, 3, 6)
    G.add(6, 4, 5)"""
    
     
    
    print ("Circ. Ham.:", G.hamiltonian())
    print("Tarda", time.time()-start,"segundos")  