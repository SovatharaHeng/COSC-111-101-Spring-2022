def chunking_by(array,chunk):
    new_array=[]
    lil_chunk=[]
    c=chunk-1
    k=0
    for i in array:
        if k<c:
            lil_chunk.append(i)
            k+=1
        elif k==c:
            lil_chunk.append(i)
            k=0
            new_array.append(lil_chunk)
            lil_chunk=[]
    if lil_chunk!=[]:
        new_array.append(lil_chunk)    
    return new_array
print (chunking_by([5, 4, 7, 3, 4, 5, 4], 3))
