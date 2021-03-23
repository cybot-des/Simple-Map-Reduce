import re  # To remove any special characters and numbers

print("MAP REDUCE PROGRAM TO RETURN ALPHABET COUNT\n")

n=int(input("enter no. of documents: "))
vocab=[]
mapper=[]
reducer=set()
for _ in range(n):
    doc=input().replace(' ','')
    doc=doc.upper()
    doc=re.sub('[^A-Za-z]','',doc) #remove all non-alphabet characters            
    doc_list=list(doc)
    vocab.append(doc_list)

#print(vocab)

###############_________MAP PHASE__________#############
for i in vocab:
    for j in i:
        mapper.append((j,1))
#print(mapper)


##############__________SHUFFLE & SORT_________############
mapper=sorted(mapper)
#print(mapper)


##############__________REDUCE PHASE__________############
prev_cnt = 0
for i in range(len(mapper)):
    cnt = mapper.count(mapper[i])
    if(cnt>1):
        reducer.add((mapper[i][0],cnt))        
    else:
        reducer.add((mapper[i][0],1))    
for i in sorted(reducer):
    print(i)
