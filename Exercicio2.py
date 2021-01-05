a = ["T", "G", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
chamadas = {1: [0,0],
            2: [2, 9],
            3: [7, 0],
            4: [11, 0],
            }
i_list=[]

def elevador(chamadas):
    for x in chamadas:
        andar_origem = chamadas[x][0]
        andar_destino = chamadas[x][1]
        index = andar_origem
        sobe_desce(andar_origem,andar_destino,index,i_list) 
        if x < chamadas.__len__():
            intervalo_destino = chamadas[x+1][0]
            index = andar_destino 
            sobe_desce(andar_destino,intervalo_destino,index,i_list)
    imprimir(i_list)


def sobe_desce(origem,destino,index,i_list):
    andar = origem
    if origem < destino:
        index = origem + 1
        while andar < destino:
            i_list.append(index) 
            index += 1
            andar += 1
        return i_list
    else:
        index=origem-1
        while andar > destino:
            i_list.append(index)
            andar -= 1
            index -= 1
        return i_list

def imprimir(i_list):
    i = 0
    for t in range(len(i_list)):
        print("O elevador está no andar", a[i_list[i]], "no tempo", t)
        i += 1
        
elevador(chamadas)
