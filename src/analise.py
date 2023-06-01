import pandas as pd
#import plotly.express as px

def criar_dicionario(lista, depart):
    lista2 =[]
    for categoria, grupo, departamento in lista:
        # print(f'{categoria} - {grupo} - {departamento}')
        # breakpoint()
        if departamento == depart:
            lista2.append(categoria)
            lista2.append(grupo)
    dic = {depart: lista2}
    return dic

def tratar_item_lista(string, remover):
    string = str(string)
    string = string.strip(remover)
    string = string.strip() 
    string = string.replace("'","")    
    return string


if __name__ == '__main__':
    lista_dicionarios=[]    
    df = pd.read_csv(r"C:\export_produtos\produtos_proxpect_.csv", encoding='utf-8')
    lista = df.values.tolist()
    df = df.drop(columns=['categoria','grupo'])
    df = df.drop_duplicates()
    lista_depart = df.values.tolist()
    # print(len(lista_depart))
    for i in lista_depart:
        depart = tratar_item_lista(i,'[]')
        x =criar_dicionario(lista=lista, depart=depart)
        lista_dicionarios.append(x) 
    print(lista_dicionarios)
# lista = df.values.tolist()

# for i in lista:
#     total, produtos_total, data, semana = i
#     if semana == 1:
#         tot_1 = tot_1 + total
#     elif semana == 2:
#         tot_2 = tot_2 + total        

# df = pd.read_csv(r"C:\export_produtos\analise_abrasivos_.csv", encoding='latin-1')
# df = df.drop(columns= 'id.1')
# lista = df.values.tolist()

# lista_ = []

# for i in lista:
#     id_, emp, cnpj, data, total, produto = i
#     if 'GRANALHA' not in produto:
#         dicionario = {'empresa':emp, 'cnpj':cnpj, 'data':data, 'total_venda':total, 'produto':produto}
#         lista_.append(dicionario)

# data_frame = pd.DataFrame(lista_)
# data_frame.to_csv(r"C:\export_produtos\analise_abrasivos.csv", index=False, encoding='latin-1')

# #print(df.head())