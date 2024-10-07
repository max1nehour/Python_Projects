
n = int(input())
school = {}
for i in range(n):
    info = str(input()).split() #info:NSYSU NC CT NS NM
    name = info[0]
    element = info[1:]
    school[name] = element

#print("/ninfos",school)
#print("info_items",school.items())


def match(name,element,condition): #element:
    ##print("------------------------------")
    #print("School:{},element:{},condition:{}".format(name,element,condition))# 1st: ['NC', 'CT', 'NS', 'NM']
    c = condition.split(" ")
    #print(c)
    if '+' in c: plus_count=1
    else: plus_count=0
    count=0
    if plus_count==1 :
        or_cond = condition.split('+') 
        #print("or_cond",or_cond)
        for e in or_cond: #except:nm if split --->n,m
            esplit = e.strip().split()
            #print("esplit",esplit)
            if len(esplit)==1:
                for i in esplit:
                    if i in set(element) :
                        #print("or_yes")
                        count+=1
 
            else:
                esplit2 = e.strip().split(" ")
                if set(esplit2)<=set(element):
                    #print("and_yes")
                    count+=1

    else: #condition length only 1
            if condition in set(element) :
                #print("1_yes")
                count+=1

    return count

def match1(name,element,condition): #element:
    c = condition.split(" ")
    #c.remove(" ")
    if '+' in c: c.remove('+')
    #print("c",c)
    or_cond = c
    count=0
    for e in or_cond:
        if len(or_cond)>1:
            #print("e",e)
            if e in set(element) :
                #print("or_yes")
                count+=1

        else:
            if e in set(element) :
                #print("1_yes")
                count+=1
    return count

def print_result(matched,school):
    delete = [key for key, value in matched.items() if value == 0]
    for key in delete:
        del matched[key]
    ranked = sorted(matched, key=lambda x: (matched[x],x))
    result = sorted(ranked, key=lambda x: list(school.keys()).index(x))
    results = list(result)
    print(" ".join(results))
    
def print_result1(matched,school):
    delete = [key for key, value in matched.items() if value == 0] #delete value=0
    for key in delete:
        del matched[key] 
    #if all has same value
    values=set()
    tmp={}
    for key,value in matched.items():
        values.add(value)
    maxvalue = max(values)
    
    for key,value in matched.items():
        if value == maxvalue:
            tmp[key]=value
        
    if len(tmp)>1: #means max has the same value
        ranked = sorted(tmp, key=lambda x: (matched[x]))
        results = sorted(tmp, key=lambda x: list(school.keys()).index(x))
        print(" ".join(results))
    else:
        ranked = sorted(matched, key=lambda x: (matched[x],x))
        results = ranked[-1]
        print(results)
    
m = int(input())
c_list = []
for i in range(m):
    condition = str(input()) #conditin: BC NS + CT HL (" "：且 +：或)
    c_list.append(condition)
b = int(input()) #決定列印的方式

for cond in c_list: #cond: 'BC NS + CT HL'
    matched = {}
    if b==0:
        for name,element in school.items():
            if match(name,element, cond)>0:
                match_count = match(name,element, cond)
                matched[name]=match_count
        #print(matched)
        print_result(matched,school)
        
    elif b==1:
        for name,element in school.items():
            #match_count=0
            if match1(name,element, cond)>0:
                match_count = match1(name,element, cond)
                matched[name]=match_count
        #print(matched)
        print_result1(matched,school)