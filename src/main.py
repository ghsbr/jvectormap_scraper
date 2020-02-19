import json
import requests
from string import ascii_lowercase

special = ["it_regions", "fr_regions"]
error404 = b'<html>\r\n<head><title>404 Not Found</title></head>\r\n<body bgcolor="white">\r\n<center><h1>404 Not Found</h1></center>\r\n<hr><center>nginx/1.10.3</center>\r\n</body>\r\n</html>\r\n'
def main():
    for a in ascii_lowercase:
        for b in ascii_lowercase:
            try:
                url = f'https://jvectormap.com/js/jquery-jvectormap-{a}{b}-merc.js'
                print(url)
                resp = requests.get(url)
                if resp.content != error404:
                    print(resp.content)
                    with open(f'../output/{a}{b}_merc.js', 'wb') as f:
                        s = resp.content
                        f.write(s)
            except KeyboardInterrupt:
                sys.exit()
            except:
                pass
    for a in special:
        try:
            url = f'https://jvectormap.com/js/jquery-jvectormap-{a}-merc.js'
            print(url)
            resp = requests.get(url)
            if resp.content != error404:
                print("success")
                with open(f'../output/{a}_merc.js', 'wb') as f:
                    s = resp.content
                    f.write(s)
        except KeyboardInterrupt:
            sys.exit()
        except:
            pass
if __name__ == '__main__':
    main()