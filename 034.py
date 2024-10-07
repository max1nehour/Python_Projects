graph = {}
n = int(input())
#輸入人與人之間的關係
while True:
    relation = input().split()
    if relation[0] == '-1':
        break
    if relation[0] not in graph:
        graph[relation[0]] = {}
        graph[relation[0]][relation[1]] = int(relation[2])
    else:
        graph[relation[0]][relation[1]] = int(relation[2])
    print(graph)
    
graph_items = graph.items()
print(graph_items)
list =[]
for key,value in graph_items:
  for k,v in value.items():
    tmp = (key,k,v)
    list = list.append(tmp)
print(list)

def checkWord(a,word):
  if a == word:
    return 1
  else: return 0


def candidateLoop(c,list,summary):
  loop =[]
  print("c",c)
  for i in range(len(c)):
    for l in range(len(list)):
      if c[i][1]== list[l][0]: #看第二格是否吻合list中第一格
        print("c{},l:{}".format(c[i][1],list[l])) #有的話看是哪一對list[l]
        loop = loop.append(list[l])
  print("loop",loop)
  print("------------------")
  check(loop,c,summary)

def check(loop,c,summary):

  result =[]

  for i in range(len(loop)):
    print("list[i][1]:",loop[i][1])
    tmp = checkWord(loop[i][1],'B')
    result = result.append(tmp)
  print("res",result)

  if 1 in result:
    summary = summary.append(c[0][0])
    idx = result.index(1)
    summary = summary.append(loop[idx][0])
    summary = summary.append('B')
    print("relation",len(summary)-1)
    summary_ = " ".join(summary)
    print("the end:{}".format(summary_))
    return summary
  else:
    print("back again")
    return candidateLoop(c[1:],list,summary) #去掉最前面的candidate

start_,end_  =[],[]
summary =[]
act = 0
summary = summary.append('A')

for i in range(len(list)):
  print(list[i][0],list[i][1],list[i][2])
  idx0, idx1, idx2= list[i][0],list[i][1],list[i][2]
  if checkWord(idx0,'A') == 1: #遍歷整個列表 找到a開頭
    start_.append(list[i])
    if list[i][1]== 'B':
        summary.append('B')
        print(len(summary)-1)
        summary_ = " ".join(summary)
        print("end",summary_)
        act+=1
        break
  if checkWord(idx1,'B') == 1: #遍歷整個列表 找到b開頭
    end_.append(list[i])
  print("start_",start_ )
  print("end_",end_ )

while act==1:
    for s in range (len(start_)):
        candidate =[]
    for i in range(len(list)):
        if start_[0][1]==list[i][0]:
            if checkWord(list[i][1],'A')==0:
                candidate.append(list[i])

    print("------------------------------")
    candidateLoop(candidate,list,summary)