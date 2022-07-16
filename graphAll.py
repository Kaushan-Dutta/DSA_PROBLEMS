#do DFS and BFS seperately, otherwise it will show error because of .visted attribute
class Node():
    def __init__(self,data):
        self.data=data
        self.datas=[]
        self.visited=False
class Graph():

    def BFS(self,node1):

     queue=[node1]
     traversal=[]
     while(len(queue)!=0):
        hold=queue.pop(0)

        traversal.append(hold.data)
        for i in hold.datas:

            if(i.visited==False):
                queue.append(i)
                i.visited=True
     return(traversal)

    def DFS(self,node,traversal):
     if(node is None):
        return
     traversal.append(node.data)
     for i in node.datas:

        if(i.visited==False):


            i.visited=True
            self.DFS(i,traversal)
     return traversal

node1=Node(8)
node2=Node(6)
node3=Node(5)
node4=Node(4)
node5=Node(3)
node6=Node(2)
node7=Node(1)

node1.datas=[node2,node3,node4]
node2.datas=[node5,node6]
node4.datas=[node7]

graph=Graph()
print(graph.BFS(node1))
print(graph.DFS(node1,[]))
