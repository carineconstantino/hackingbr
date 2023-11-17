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
                                            Exemplo: python3 html_dir_scan.py --target https://example.com.br ''')
                                                        
    argumentos_parser = program_name.parse_args()
    base_url = argumentos_parser.url

def search_dir_in_html():

     req = requests.get(base_url)
     response = req.text	
     soup = BeautifulSoup(response, 'html.parser')
     search_dir = set(re.findall(r'/[a-zA-Z]+/', response))
     print('[+] Directories Found in HTML:\n', search_dir)
     print('-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_')
     print('[+] Testing Directories Access & Brute-Force\n')
     for x in search_dir:
     	req_dir = requests.get(base_url + x)
     	print('-->Send: ', req_dir.url)
     	print('-->Status: ', req_dir.status_code)
     	
     	file_path = 'small.txt'
     	open_file = open(file_path, 'r')
     	if 'req_dir.status_code == 200 || 404':
     		for i in open_file.readlines():
     			headers = {'Accept-Encoding': 'gzip'}
     			req_brute = requests.get(req_dir.url + i, headers=headers)
     			print('-->Request: ', req_brute.url)
     			print('<--Response: ', req_brute.status_code)
     		
     	


search_dir_in_html()
