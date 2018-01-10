#!/usr/bin/python

import requests
import time
import os
import notify


#current_ip = ""
IP_FILE="ip.txt"
TWITTER="twitter"
PUSHBULLET="pushbullet"
TIME_SLEEP=30


def get_nofication_method():
    return os.environ.get('NOTIFY', TWITTER)

def get_public_ip():
    r = requests.get(r'http://jsonip.com')
    return r.json()['ip']

def write_ip_to_disk(ip):
    with open(IP_FILE,'w') as fo:
        fo.write(ip)
        fo.close()

def get_ip_from_disk(ip):
    disk_ip=""
    with open(IP_FILE,'r') as fo:
        disk_ip = fo.read(ip)
        fo.close()
    return disk_ip

def notify_user(ip):
    msg="this is a dummy tweet of ip: %s. " % ip
    print msg
    #notify.send_tweet(msg)


def run():
    current_ip="0.0.0.0"
    while True:
        public_ip = get_public_ip()
        if not public_ip == current_ip:
            # update ip var
            current_ip = public_ip
            notify_user(current_ip)
        else:
            print "[sleep] no change. sleeping"

        time.sleep(TIME_SLEEP)



if __name__ == "__main__":
    run()