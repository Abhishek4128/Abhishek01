def return_all_substrings_of_length_k(S,k):
    result=[]
    if k>len(S) or k<=0:
        return result
    for i in range(0,len(S)-k+1):
            sub_string=S[i:i+k]
            result.append(sub_string)
    return result
print(return_all_substrings_of_length_k("pythonlife",4))   