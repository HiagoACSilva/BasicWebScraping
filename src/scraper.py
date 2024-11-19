from bs4 import BeautifulSoup
import requests
import pandas as pd
link4 = 'https://sigaa.ufpi.br/sigaa/public/programa/equipe.jsf?lc=pt_BR&id=1080'
link3 = 'https://sigaa.ufma.br/sigaa/public/programa/equipe_stricto.jsf?lc=pt_BR&idPrograma=1453'
link2 = 'https://sigaa.ufma.br/sigaa/public/programa/equipe_stricto.jsf?lc=pt_BR&idPrograma=1117'
link = 'https://sigaa.ufpi.br/sigaa/public/programa/equipe.jsf?lc=pt_BR&id=615'

def webscraper(link, name):
    dados = []
    html = requests.get(link).content
    soup = BeautifulSoup(html, 'html.parser', from_encoding='utf-8')

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
            dupla = [(texto_cor, href_lattes)]
            dados += dupla

    df = pd.DataFrame(dados, columns=["Nome", "Lattes"])
    df.to_csv(f"data/{name}.csv", index=False)


#link = input("url: ")
#name = input("name whitout .csv: ")
webscraper(link, "PPGCC_UFPI")
webscraper(link2, "PPGCC_UFMA")
webscraper(link3, "DCCMAPI_UFMA")
webscraper(link4, "DCCMAPI_UFPI")

