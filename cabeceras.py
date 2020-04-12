import argparse
import requests

parser= argparse.ArgumentParser(description="detector")
parser.add_argument('-t','--target',help ="objetivo")
parser= parser.parse_args()

def main():
    if parser.target:
        try:
            url=requests.get(url=parser.target)
            url=dict(url.headers)
            for x in url:
                print(x+">>>"+url[x] )
          
        except:
            print("no se pudo conectar")
    else:
        print("no hay objetivo")
if __name__ == "__main__":
    main()
    
