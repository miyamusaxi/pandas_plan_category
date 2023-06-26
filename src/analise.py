import pandas as pd
import numpy as np
from datetime import datetime

def tratar_key(key):
    key = str(key).strip('dict_keys')
    key = key.strip("[(')]")
    return key

def criar_dicionario(lista, cat):
    lista2 = []
    for produto, categoria in lista:
        if categoria == cat:
            lista2.append(produto)
    return {cat: lista2}

def tratar_str(string, remover):
    string = str(string)
    string = string.strip(remover)
    string = string.strip()
    string = string.replace("'", "")
    return string

def categorizar(row, prod, key,conteudo,prod2):
    if conteudo and prod.lower() in key.lower():
        conteudo = [str(conte).lower() for conte in conteudo]
        if 'serra' in prod2 and 'moto' not in prod2:
            return pd.DataFrame({
                    'id' :row['id'],
                    'codigo interno': row['Código interno'],
                    'produto':row['Titulo'],
                    'preco':row['Preço'],
                    'categoria':'Serra',
                    'ativo':row['Ativo']
                    },index=[0])
        elif ((prod.lower()in conte) for conte in conteudo) or ((prod2.lower() in conte) for conte in conteudo):
            return pd.DataFrame({
                    'id' :row['id'],
                    'codigo interno': row['Código interno'],
                    'produto':row['Titulo'],
                    'preco':row['Preço'],
                    'categoria':key,
                    'ativo':row['Ativo']
                    },index=[0])
    elif not prod.lower() in key.lower():
        return pd.DataFrame({
                    'id' :row['id'],
                    'codigo interno': row['Código interno'],
                    'produto':row['Titulo'],
                    'preco':row['Preço'],
                    'categoria':CAT_CORINGA,
                    'ativo':row['Ativo']
                    },index=[0])




if __name__ == '__main__':
    CAT_CORINGA = 'Cama, Mesa e Banho'
    listadics = []
    listaitens = []
    cont = 0
    
    #Cria uma base de dados para categorização
    df = pd.read_csv(
        r"C:\export_produtos\categorias.csv", encoding='utf-8')
    tipo = type(df)
    
    df = df.drop(columns=['departamento', 'grupo'])
    
    lista = df.values.tolist()

    df = df.drop(columns=['titulo'])

    df = df.drop_duplicates()

    listacat = df.values.tolist()

    for i in listacat:
        cat = tratar_str(str(i),'['']')
        cat = cat.strip()
        cat = cat.replace('"','')
        x = criar_dicionario(lista=lista, cat=cat)
        listaitens.append(x)

    df = pd.read_excel(
        r"C:\py_projects\data_analise\doc\Categorias J2D DISTRIBUIDORA.xlsx").replace({np.nan: None}).to_dict(orient='records')

    cats = [tratar_key(str(key.keys())) for key in listaitens]
    conteudo = [dic.get(cats[i]) for i, dic in enumerate(listaitens)]
    for i, row in enumerate(df):
        if row['Ativo'] == 'Sim' and row['Nova Categoria'] == None:
        #TRATAMENTO DE STRING
            newstring = row['Titulo'].split('-')
            prod = newstring[0].split()
            prod = [str(produto).lower() for produto in prod]
            prodComp = ' '.join(prod)
            produto = prod[0]    
            for i, key in enumerate(cats):
                temp = (categorizar(row,produto,key,conteudo[i],prodComp))
                if type(temp) == tipo :
                    listadics.append(temp)
                    break
    #exportando pra planilha
    if listadics:
        now = datetime.now()
        result = pd.concat(listadics)
        result.to_excel(f'C:\py_projects\data_analise\doc\categorizado-{now:%d%m%y-%H%M%S}.xlsx')
        print('success')
