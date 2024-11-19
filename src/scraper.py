from bs4 import BeautifulSoup
import requests
link4 = 'https://sigaa.ufpi.br/sigaa/public/programa/equipe.jsf?lc=pt_BR&id=1080'
link3 = 'https://sigaa.ufma.br/sigaa/public/programa/equipe_stricto.jsf?lc=pt_BR&idPrograma=1453'
link2 = 'https://sigaa.ufma.br/sigaa/public/programa/equipe_stricto.jsf?lc=pt_BR&idPrograma=1117'
link = 'https://sigaa.ufpi.br/sigaa/public/programa/equipe.jsf?lc=pt_BR&id=615'
html = requests.get(link4).content
soup = BeautifulSoup(html, 'html.parser', from_encoding='utf-8')

dados = []
for tr in soup.find_all('tr'):
    a_cor = tr.find('a', class_='cor')
    a_lattes = tr.find('a', id='endereco-lattes')
    if a_cor:
        texto_cor = a_cor.text.strip()
    else:
        texto_cor = None
    if a_lattes:
        href_lattes = a_lattes['href']
    else:
        href_lattes = None
    if a_cor != None:
        dados.append({texto_cor, href_lattes})

print(*dados, sep='\n')

