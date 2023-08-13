# Questao 2

v = [[1, 5, 0], [2.0, 3, 5.5, 9], [4]]    
                                          
def igualarlista(L):                      
    lista = L                          
    maior = L[0]                          
    for i in lista:                       
        if len(i) > len(maior):           
            maior = i                     
    for i in range(len(lista)):           
        while len(lista[i]) < len(maior): 
            lista[i].append(0)            
    return(lista)                         
                                          
print(igualarlista(v))  