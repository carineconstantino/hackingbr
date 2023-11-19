import argparse
import requests
from bs4 import BeautifulSoup
import pyfiglet
import re
import datetime


titulo  = pyfiglet.figlet_format("HTML DIR SCAN")
print(titulo)
print('Criado por @hackingbr\n')
print('-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_')

if __name__ == '__main__':

    program_name  = argparse.ArgumentParser(description = 'HTML DIR SCAN')
    program_name.add_argument('-url', action='store', dest='url',
                                            required = True, help = ''' Informe uma URL para executar o scan :::
                                            Exemplo: python3 html_dir_scan.py -url https://example.com.br ''')
    
    program_name.add_argument('-w', action='store', dest='wordlist',
                                            required = True, help = ''' Informe uma URL para executar o scan :::
                                            Exemplo: python3 html_dir_scan.py -url https://example.com.br ''')
                                                        
    argumentos_parser = program_name.parse_args()
    base_url = argumentos_parser.url
    base_wordlist = argumentos_parser.wordlist

def search_dir_in_html():

     req = requests.get(base_url)
     response = req.text	
     soup = BeautifulSoup(response, 'html.parser')
     search_dir = set(re.findall(r'/[a-zA-Z]+/', response))
     d = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
     print('[+] Data do Scan: ', d)
     print('[+] Directories Found in HTML:\n', search_dir)
     print('-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_')
     print('[+] Testing Directories Access & Brute-Force\n')
     for x in search_dir:
     	req_dir = requests.get(base_url + x)
     	print('-->Send: ', req_dir.url)
     	print('-->Status: ', req_dir.status_code)
     	
     	file_path = base_wordlist
     	open_file = open(file_path, 'r')
     	if 'req_dir.status_code == 200':
     		for i in open_file.readlines():
     			headers = {'Accept-Encoding': 'gzip'}
     			req_brute = requests.get(req_dir.url + i, headers=headers)
            
def search_result():
    if 'req_brute == 200':
        print('-->Request: ', req_brute.url)
        print('<--Response: ', req_brute.status_code)

     	


search_dir_in_html()
search_result()
