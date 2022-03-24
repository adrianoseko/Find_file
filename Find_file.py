import os
import pandas as pd 
import shutil


pasta = 'C:/Users/admin/Desktop/Adriano/Projetos_SW/xml/xml_mes_09_11'
ex = pd.read_excel('C:/Users/admin/Desktop/Adriano/Projetos_SW/acha arquivo/IDMOV.xlsx')
nf = ex.NF.values
lista_nf= []
index = 0
for n in nf:
    lista_nf.append(str(f"<nNF>{n}</nNF>"))
    
  

for diretorio, subpastas, arquivos in os.walk(pasta):
    for arquivo in arquivos:
        with open(f"{pasta}/{arquivo}", "r", encoding='utf-8') as xml:
            x = xml.read()
            for n in lista_nf:
                if n in x: 
                   
                    source = f"C:/Users/admin/Desktop/Adriano/Projetos_SW/xml/xml_mes_09_11/{arquivo}"
                    destination = f"C:/Users/admin/Desktop/Adriano/Projetos_SW/xml/Nova pasta/{arquivo}"
                    shutil.move(source, destination) 
                    print(n)
                    xml.close()
                xml.close()
        
