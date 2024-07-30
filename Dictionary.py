d = {}
print(type(d))   #<class 'dict'>

d={'a':1}

d1 = {'name':'sudh'}
print(d1['name'])           #sudh

d2 = {2343: 'sudh'}
print(d2[2343])             #sudh

# d2 = {$2343: 'sudh}   ---- no special characters should be used

# d4 = {[1,2,3]: 'sudh'}    --- TypeError: unhashable type: 'list'

d5 = {(1,2,3): 'sudh'}          # tuples can be used 
print(d5[(1,2,3)])

#d6 = {{1,2,3}: 'sudh'}          --TypeError: unhashable type: 'set'

d7 = {True: 'sudh'}

#d8 = {{'name': 'su'}: 'sudh'}           ---- TypeError: unhashable type: 'dict'

d9 = {'name':'sudh','name':'pwskills'}       #the key are unique if a key repeats then its value is overwritten
print(d9)                                #{'name': 'pwskills'}

d10 = {'name': 'Bld','email':'Bld@gmail.com','subject': ['dsa','big data','programming','sql']}
print('dsa' in d10["subject"])      #True

d11 = {'name': 'Bld','email':'Bld@gmail.com','subject': ['dsa','big data','programming','sql'],'batch': ('DSM','java','full stack web'),'mentor': {'sudhanshu','krish','vishwa mohan','sanket','hyder','nitin','vishwa mohan'},'Date': {
    'FSDS': '29th april 23','DSM':"25th june 23"}}

print(d11)
print(d11["Date"]["DSM"])

d11["batches"] = "Binary 2.0"
print(d11)

del d11["email"]
print(d11)

print(d11.keys())
print(d11.values())
print(d11.items())

print(d11.clear())
