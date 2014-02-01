#A program to implement List using Graph#
import graph
 def_init_(self):
  self.vertList={}
  self.numVertices=0
 def addvertex(self,key):
  self.numVertices=self.numvertices+
  newVertex=Vertex(key)
  self.vertList[key]=newVertex
  return newVertex
 def getVertex(self,n):
  if n in self.vertList
   return self.vertList[n]
  else:
   return None
 def getVertices(self):
   return self.vertList.keys()
   g=graph()
   for i in range(3):
    g.addVertex(i)
   g.vertList
   g.addEdge(0,1,2)
   g.addEdge(1,0,2)
   g.addEdge(2,4,5)
   print()

#A program to implement Dict using Graph#   
import graph
 gr=graph()
  gr.add_nodes(['portugal','spain','France','a','b'])
  gr.add_nodes(['india','US','3','4'])
   gr.add_edge(['portugal','a'])
   gr.add_edge(['spain','b'])
   gr.add_edge(['indian','3'])
 print()
 
#A program to implement tuples in Graph#
tup1.add_node=('python','network security')
tup2.add_node=(py,se)
 tup.add_edge('python':'programming lang')
 tup.add_edge('network security':'cse')
print tup()
