import requests

def make_request(method, url, data=None):
    try:
        if method.upper() == 'GET':
            response = requests.get(url)
        elif method.upper() == 'HEAD':
            response = requests.head(url)
        elif method.upper() == 'POST':
            response = requests.post(url, data=data)
        elif method.upper() == 'PUT':
            response = requests.put(url, data=data)
        elif method.upper() == 'DELETE':
            response = requests.delete(url)
        elif method.upper() == 'CONNECT':
            response = requests.request('CONNECT', url)
        elif method.upper() == 'OPTIONS':
            response = requests.options(url)
        elif method.upper() == 'TRACE':
            response = requests.request('TRACE', url)
        elif method.upper() == 'PATCH':
            response = requests.patch(url, data=data)
        else:
            raise ValueError("Invalid HTTP method")

        output = f"<p>Response for {method} request to {url}:</p>"
        output += f"<p>Status code: {response.status_code}</p>"
        output += f"<p>Response body: {response.text}</p>"

    except Exception as e:
        output = f"<p>Error making {method} request to {url}: {e}</p>"

    return output

def main():
    url = input("Enter the URL you want to make requests to: ")

    # Send requests with various HTTP methods
    html_output = "<html><head><title>HTTP Request Results</title></head><body>"
    html_output += "<h2>Método GET</h2>"
    html_output += make_request('GET', url)
    html_output += "<h2>Método HEAD</h2>"
    html_output += make_request('HEAD', url)
    html_output += "<h2>Método POST</h2>"
    html_output += make_request('POST', url, data={'key': 'value'})
    html_output += "<h2>Método PUT</h2>"
    html_output += make_request('PUT', url, data={'key': 'value'})
    html_output += "<h2>Método DELETE</h2>"
    html_output += make_request('DELETE', url)
    html_output += "<h2>Método CONNECT</h2>"
    html_output += make_request('CONNECT', url)
    html_output += "<h2>Método OPTIONS</h2>"
    html_output += make_request('OPTIONS', url)
    html_output += "<h2>Método TRACE</h2>"
    html_output += make_request('TRACE', url)
    html_output += "<h2>Método PATCH</h2>"
    html_output += make_request('PATCH', url, data={'key': 'value'})
    html_output += "</body></html>"

    with open("http_request_results.html", "w") as file:
        file.write(html_output)

if __name__ == "__main__":
    main()
