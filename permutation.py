from itertools import permutations 
  
def permu(str): 
     x = permutations(str) 
     for x in list(x): 
         print (''.join(x))
         #print(len(perm))

permu('protosem')          
        

#if __name__ == "__main__": 
    #str = 'ABC'
    #allPermutations(str) 