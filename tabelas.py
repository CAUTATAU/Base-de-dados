import pandas as pd
from matplotlib_venn import venn2
from matplotlib_venn import venn3
from matplotlib import pyplot as plt
#ler as planilhas iniciais
tabela_alunos = pd.read_csv("base_aluno.csv", sep=';')
tabela_dengue = pd.read_csv("base_dengue.csv", sep=';')
tabela_onibus = pd.read_csv("base_onibus.csv", sep=';')


alunos_e_dengue = pd.merge(tabela_alunos, tabela_dengue,on="Nome",how="left")#juntar base de alunos com base de dengue
dengue_e_alunos = pd.merge(tabela_dengue, tabela_alunos,on="Nome",how="left")
alunos_e_onibus = pd.merge(tabela_alunos, tabela_onibus, on="Nome", how="left")#juntar base de alunos e base de onibus
onibus_e_alunos = pd.merge(tabela_onibus,tabela_alunos, on='Nome',how='left')
dengue_e_onibus = pd.merge(tabela_onibus, tabela_dengue,on="Nome",how="left")#juntar base de dengue e base de onibus
onibus_e_dengue = pd.merge(tabela_onibus,tabela_dengue, on='Nome',how='left')
alunos_e_dengue = alunos_e_dengue.drop_duplicates(subset=['Nome'], keep='first')
dengue_e_alunos = dengue_e_alunos.drop_duplicates(subset=['Nome'],keep='first')
alunos_e_onibus = alunos_e_onibus.drop_duplicates(subset=['Nome'], keep='first')
onibus_e_alunos = onibus_e_alunos.drop_duplicates(subset=['Nome'],keep='first')
dengue_e_onibus = dengue_e_onibus.drop_duplicates(subset=['Nome'], keep='first')
onibus_e_dengue = onibus_e_dengue.drop_duplicates(subset=['Nome'],keep='first')
total= pd.merge(tabela_onibus,alunos_e_dengue,on="Nome",how="left")#juntar junção anterior com base de onibus
total2= pd.merge(alunos_e_dengue,tabela_onibus, on='Nome',how='left')
total = total.drop_duplicates(subset=['Nome'], keep='first')

alunos_sem_dengue = alunos_e_dengue[alunos_e_dengue['Data da Dengue'].isna()]
com_dengue_sem_nao_onibus = dengue_e_onibus[dengue_e_onibus['onibus'].notna()]
onibus_sem_dengue = dengue_e_onibus[dengue_e_onibus['Data da Dengue'].isna()]
alunos_com_dengue = alunos_e_dengue[~alunos_e_dengue['Data da Dengue'].isna()]
alunos_onibus = alunos_e_onibus[~alunos_e_onibus['onibus'].isna()]
com_dengue_onibus = onibus_e_dengue[onibus_e_dengue['Data da Dengue'].notna()]
#alunos_com_dengue_onibus = total[~total["Data da Dengue"].isna()]
com_dengue_sem_onibus = onibus_e_dengue[onibus_e_dengue['onibus'].isna()]
com_dengue_nao_alunos = pd.merge(com_dengue_sem_onibus,tabela_onibus,on='Nome',how='left')
com_dengue_nao_alunos_sem_onibus = pd.merge(dengue_e_onibus, onibus_e_dengue, on= 'Nome',how='left')





alunos_sem_dengue.to_csv("1) Relatório Educação.csv", index=False,sep=";", encoding="utf-8" )
com_dengue_sem_nao_onibus.to_csv("2) Relatório Saúde.csv", index=False,sep=";", encoding="utf-8")
onibus_sem_dengue.to_csv("3) Relatório Mobilidade.csv", index=False,sep=";", encoding="utf-8")
alunos_com_dengue.to_csv("4) Relatório Educação e Saúde.csv", index=False,sep=";", encoding="utf-8")
alunos_onibus.to_csv("5) Relatório Educação e Mobilidade.csv", index=False,sep=";", encoding="utf-8")
com_dengue_onibus.to_csv("6)  Relatório Saúde e Mobilidade.csv", index=False,sep=";", encoding="utf-8")
#alunos_com_dengue_onibus.to_csv("7) Relatório Saúde, Mobilidade e Educação.csv", index=False,sep=";", encoding="utf-8")
com_dengue_sem_onibus.to_csv("8) Relatorio saude sem mob.csv", index=False,sep=";", encoding="utf-8")
com_dengue_nao_alunos.to_csv("9) Relatorio saude sem educação.csv", index=False,sep=";", encoding="utf-8")
com_dengue_nao_alunos_sem_onibus.to_csv("10) saude sem ed. sem mob.csv", index=False,sep=";", encoding="utf-8")



conjunto_alunos = set(tabela_alunos['Nome'])
conjunto_com_dengue = set(tabela_dengue['Nome'])
conjuto_geral = set(total['Nome'])

plt.figure(figsize=(16, 16))
venn3([conjunto_alunos, conjunto_com_dengue, conjuto_geral], ('Alunos', 'População Geral Com Dengue', 'Onibus'), set_colors=("black","gray", "blue"))
plt.title("Diagrama XPTO")
plt.show()