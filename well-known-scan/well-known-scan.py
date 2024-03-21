import requests
import pyfiglet

titulo  = pyfiglet.figlet_format("Well-Known Scan")
print(titulo)
print('Criado por @hackingbr\n')
print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ')


filename = "/path/well-known-urls.txt"

def directory_discovery(url, filename):
    try:
        with open(filename, 'r') as f:
            wordlist = f.readlines()

        for directory in wordlist:
            directory = directory.strip()  # Remove any leading/trailing whitespace
            full_url = url + "/" + directory
            response = requests.get(full_url)
            if response.status_code == 200:
                print("[+] Directory found:", full_url)
    except FileNotFoundError:
        print("File not found:", filename)
    except requests.exceptions.RequestException as e:
        print("Error occurred:", e)

if __name__ == "__main__":
    url = input("Enter the URL to perform directory discovery: ")    
    directory_discovery(url,filename)
