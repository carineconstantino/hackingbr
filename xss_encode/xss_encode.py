#!/usr/bin/python3

import urllib.parse
import requests
import re
import argparse
import pyfiglet

titulo = pyfiglet.figlet_format("XSS Encode")
print(titulo)
print('Criado por @hackingbr\n')
print('-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_')

if __name__ == '__main__':

    program_name  = argparse.ArgumentParser(description = 'XSS Encode')
    program_name.add_argument('--url', action='store', dest='url',
                                            required = True, help = ''' Informe uma URL para executar o scan :::
                                            Exemplo: python3 xss_encode.py --target https://example.com ''')
    program_name.add_argument('--param', action='store', dest='param',
                                            required = True, help = ''' Informe uma URL para executar o scan :::
                                            Exemplo: python3 xss_encode.py --target https://example.com''')
                                                        
    argumentos_parser = program_name.parse_args()
    base_url = argumentos_parser.url
    params = argumentos_parser.param


file_path = 'payloads.txt'
open_file = open(file_path, 'r')
for line in open_file.readlines():
    encoded_values = requests.utils.quote(line)
    p = { params: encoded_values}
    req = requests.get(base_url, params=p)
    response = req.text
    search = re.findall('teste-xss', response)
    result_search = search
    if len(search) > 0:
        print('\nPayload Executado - XSS Attack Refleted ', req.status_code)
        print('Payload: ', req.url)
    else:
        print('\nPayload não executado', req.status_code)
        print('Payload enviado: ', req.url)

