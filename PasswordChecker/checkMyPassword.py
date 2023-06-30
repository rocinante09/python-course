import requests
import hashlib
import sys


def request_api_data(query):
#    'AAF4C61DDCC5E8A2DABEDE0F3B482CD9AEA9434D'
#    'AAF4C61DDCC5E8A2DABEDE0F3B482CD9AEA9434D'
    url = 'https://api.pwnedpasswords.com/range/' + query  # maintain anonymity by passing first 5 chars in hashed password(SHA1)
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching response for {url}. Error: {res.status_code}')
    return res

def get_hacked_pwd_count(hashes, hash_to_check):
# Tail = '61DDCC5E8A2DABEDE0F3B482CD9AEA9434D'

    hashes = (line.split(':') for line in hashes.text.splitlines())
    for hsh, count in hashes:
        if hsh == hash_to_check:
            return count
    return 0


def request_pwned_check(password):

    # needs to be UTF-8 encoded, object is convereted to hex and then upper
    sha1_pwd = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5chars, tail = sha1_pwd[:5], sha1_pwd[5:]
    res = request_api_data(first5chars)
    return get_hacked_pwd_count(res, tail)

def main(args):
    for pwd in args:
        count = request_pwned_check(pwd)
        if count:
            print(f'you should probably change this password: {pwd}\nIt has been copied {count} times' )
        else:
            print(f'{pwd} is ok')
    return "Finished!"

if __name__ == '__main__':
  sys.exit(main(sys.argv[1:]))
#  sys.exit(main(['hello', 'password123']))


