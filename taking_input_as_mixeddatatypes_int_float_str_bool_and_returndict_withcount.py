def count_of_type(mixed_datatypes):
    frequency={
               'int':0,
               'float':0,
               'string':0,
               'boolean':0
    }
    for item in mixed_datatypes:
        if isinstance(item,bool):
            frequency['boolean']=frequency['boolean']+1
        elif isinstance(item,int):
            frequency['int']=frequency['int']+1
        elif isinstance(item,float):
            frequency['float']=frequency['float']+1
        elif isinstance(item,str):
            frequency['string']=frequency['string']+1
        else:
            pass
    return frequency
print(count_of_type([True,2,7,8,True,False,12,"virat","rohit",2.76,7.611]))