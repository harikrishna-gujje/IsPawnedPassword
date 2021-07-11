import hashlib
import requests


def check_with_api(first5):
    res = requests.get('https://api.pwnedpasswords.com/range/'+first5)
    if(res.status_code!=200):
        raise RuntimeError('check the api again')
    return res


def leak_count_of_our_password(lines, tail):
    for line in lines:
        match, count = line.split(":")
        if match == tail:
            return count
    return 0

def have_i_pawned(password):
    hashed_password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5, tail = hashed_password[:5], hashed_password[5:]
    res = check_with_api(first5)
    lines = (res.text).splitlines()
    c = leak_count_of_our_password(lines, tail)
    return c


if __name__ == '__main__':
    password='Hello123'
    count = have_i_pawned(password)
    print(f'your password has been pawned for {count} times')