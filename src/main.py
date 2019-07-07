import requests
import sys
import dxpy


def main():
    print dxpy.whoami()
    resp = requests.get('https://www.python.org')
    print resp.status_code
    print resp.text


if (__name__ == '__main__'):
    sys.exit(main() or 0)