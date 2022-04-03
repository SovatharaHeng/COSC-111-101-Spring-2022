print("In a given string you should reverse every word, but the words should stay in their places.") 
def backward_string_by_word(strings):
    lil_chunk=[]
    encryption=""
    k=0
    for i in strings:
        if i!= " ":
            lil_chunk.append (i)
        elif i==" ":
            lil_chunk.reverse()
            if k<1: 
                encryption+="".join(lil_chunk)
                k+=1
                lil_chunk=[]
            else:
                encryption+=" "
                encryption+="".join(lil_chunk)
                lil_chunk=[]
    lil_chunk.reverse()
    encryption+=" "
    encryption+="".join(lil_chunk)
    return encryption
print (backward_string_by_word('hello world') )
