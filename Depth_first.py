# list the nodes in dect 
adj_list={
    'a':['b','c'],
    'b':['d','e'],
    'c':['b','f'],
    'd':[],
    'e':['f'],
    'f':[]
}

color={}
parent={}
traverse_time={}
dfs_traverse_out =[]
for node in adj_list.keys():
        color[node]='W'
        parent[node]=None
        traverse_time[node]=[-1,-1]
print(color)
print(parent)
print(traverse_time)

time=0 
def dfs(u):   #a 
    global time
    color[u]='G'
    traverse_time[u][0]=time
    dfs_traverse_out.append(u)    #[a , ]
    for v in adj_list[u]: #b
        if color[v]=='W':
            parent[v]=u
            dfs(v)
        color[u]='B'
        traverse_time[u][1]=time
        time +=1   

       
dfs('a')

print(color)
print(parent)
print(traverse_time)
print(dfs_traverse_out)       
