class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def addEgde(self, u, v, w):
        self.graph.append([u, v, w])

    def findOrder(self,numCourses, prerequisites):

        output = [ ]
        cycle = set ()

        def findinlst(lst, val):
            for x in range ( 0, len ( lst ) ):
                try:
                    pos = lst[ x ].index ( val )

                    return [ x, pos ]
                except:
                    continue
            return [ False, False ]

        prereq = {c: [ ] for c in range ( numCourses )}
        for crs, pre in prerequisites:
            if pre == '':
                output.append ( crs )
                delete_id = findinlst ( prerequisites, crs )
                print ( delete_id[ 0 ] )
                prerequisites[ delete_id[ 0 ] ].remove ( crs )
                while [ '' ] in prerequisites:
                    prerequisites.remove ( [ '' ] )
                print ( prerequisites )
            else:
                prereq[ crs ].append ( pre )

        visit, cycle = set (), set ()

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True

            cycle.add ( crs )
            for pre in prereq[ crs ]:
                if dfs ( pre ) == False:
                    return False

            cycle.remove ( crs )
            visit.add ( crs )
            if len ( output ) != numCourses:
                print ( "output2", output )
                output.append ( crs )
                print ( "output3", output )
                return True

        for c in range ( numCourses ):
            if dfs ( c ) == False:
                return [ ]
        return result_Sequence( output)

def result_Sequence(output):
    vertices = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h'}
    print(output)
    final = []
    for i in range (len(output)):
        final.append(vertices[output[i]])
    print(final)
vertices = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h'}
graph = Graph(9)
graph.addEgde ( 'A', 'B', vertices )
graph.addEgde ( 'A', 'C', vertices )
graph.addEgde ( 'B', 'D', vertices )
graph.addEgde ( 'B', 'E', vertices )
graph.addEgde ( 'C', 'D', vertices )
graph.addEgde ( 'D', 'E', vertices )
graph.addEgde ( 'G', 'E', vertices )
graph.addEgde ( 'A', 'G', vertices )
graph.findOrder ( numCourses=8,
                  prerequisites=[ [ 4, 1 ], [ 4, 3 ], [ 4, 6 ], [ 3, 1 ], [ 3, 2 ], [ 2, 0 ], [ 1, 0 ], [ 5, '' ],
                                  [ 6, 0 ], [ 7, '']])

