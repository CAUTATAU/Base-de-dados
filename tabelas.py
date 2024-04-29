import pandas as pd
from matplotlib_venn import venn2
from matplotlib import pyplot as plt
tabela_alunos = pd.read_csv("base_aluno.csv", sep=';')
tabela_dengue = pd.read_csv("base_dengue.csv", sep=';')
tabela_final = pd.merge(tabela_alunos, tabela_dengue,on="Nome",how="left")

alunos_sem_dengue = tabela_final[tabela_final['Data da Dengue'].isna()]
alunos_com_dengue = tabela_final[~tabela_final['Data da Dengue'].isna()]
alunos_com_dengue = alunos_com_dengue.drop_duplicates(subset=['Nome'], keep='first')
alunos_sem_dengue = alunos_sem_dengue.drop_duplicates(subset=['Nome'], keep='first')
alunos_sem_dengue.to_csv("aluno_sem_dengue.csv", index=False, sep=";", encoding="utf-8")
alunos_com_dengue.to_csv("aluno_com_dengue.csv", index=False, sep=";", encoding= "utf-8")

alunos_com_dengue = pd.read_csv("aluno_com_dengue.csv", sep=';')
alunos_sem_dengue = pd.read_csv("aluno_sem_dengue.csv", sep=';')

conjunto_alunos = set(tabela_alunos['Nome'])
conjunto_com_dengue = set(tabela_dengue['Nome'])

plt.figure(figsize=(16, 16))
venn2([conjunto_alunos, conjunto_com_dengue], ('Alunos', 'Com Dengue(não aluno)'), set_colors=("red","blue"))
plt.title("Diagramas para Dengue entre Alunos")
plt.show()