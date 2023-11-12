import argparse
import requests
from bs4 import BeautifulSoup
import pyfiglet
import re
import datetime


titulo  = pyfiglet.figlet_format("HTML SCAN")
print(titulo)
print('Criado por Carine Constantino Contato: carineconstantino@hotmail.com\n')
print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ')

def extrair_links_do_html(html_conteudo):
    soup = BeautifulSoup(html_conteudo, 'html.parser')
    links = set(a.get('href') for a in soup.find_all('a', href=True))
    return links

def extrair_links_do_js(js_conteudo):
    js_links = set(re.findall(r'(?:https?|ftp)://[^\s/$.?#].[^\s]*', js_conteudo))
    return js_links

def search_links(url):
    try:
        # Envia o HTTP request para a URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses

        # Extrai links do conteudo HTML
        html_links = extrair_links_do_html(response.text)

        # Extrai links do conteudo JavaScript
        js_links = extrair_links_do_js(response.text)

    	# Extrair datetime
        d = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Convert a data em string para usar no titulo do relatorio
        str_current_datetime = str(d)
        
        # Print o relatorio com os links separados por categoria
        print("Data do Scan", d)
        print("Scan executado em", url)
        print("\nHTML Links:")
        print("")
        for link in html_links:
            print("[+] ",link)

        print("\nJavaScript Links:")
        print("")
        for link in js_links:
            print("[+] ",link)
            
        # Genera o relatorio em HTML
        html_report = f"""
        <html>
        <head>
            <title>HTML SCAN</title>
        </head>
        <body>
            <h1>HTML SCAN</h1>
            
            <h2>Scan executado na url {url}</h2>
            <h2>Data do Scan {d}</h2>
            
            <h3>HTML Links:</h3>
            <ul>
                {"".join(f'<li><a href="{link}">{link}</a></li>' for link in html_links)}
            </ul>

            <h3>JavaScript Links:</h3>
            <ul>
                {"".join(f'<li><a href="{link}">{link}</a></li>' for link in js_links)}
            </ul>
        </body>
        </html>
        """

        # Salva o relatorio HTML em um arquivo
        file_name = open(str_current_datetime + ' relatorio_do_scan.html', 'w', encoding='utf-8')
        file_name.write(html_report)
        
	
        print("\n[**] Resultado salvo no arquivo HTML")

    except requests.exceptions.RequestException as e:
        print("Erro! Faltou a URL para o scan:", e)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Procura por links em arquivos HTML e JavaScript")
    parser.add_argument("-url", action='store', required=True, dest='url', help="URL para executar o scan")

    args = parser.parse_args()
    search_links(args.url)
