#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

import requests
from bs4 import BeautifulSoup

region_bindings = {
    'US East N. Virginia': 'us-east-1',
    'US East Ohio': 'us-east-2',
    'US West N. California': 'us-west-1',
    'US West Oregon': 'us-west-2',
    'Asia Pacific Mumbai': 'ap-south-1',
    'Asia Pacific Seoul': 'ap-northeast-2',
    'Asia Pacific Singapore': 'ap-southeast-1',
    'Asia Pacific Sydney': 'ap-southeast-2',
    'Asia Pacific Tokyo': 'ap-northeast-1',
    'Canada Central': 'ca-central-1',
    'EU Frankfurt': 'eu-central-1',
    'EU Ireland': 'eu-west-1',
    'EU London': 'eu-west-2',
    'EU Paris': 'eu-west-3',
    'South America São Paulo': 'africa',
    'China Beijing': 'china',
    'AWS GovCloud': 'gov'
}
region_bindings_inv = {v: k for k, v in region_bindings.items()}

machines = {
    'HVM (SSD) EBS-Backed 64-bit': 'hvm-ebs',
    'HVM Instance Store 64-bit': 'hvm-is',
    'PV EBS-Backed 64-bit': 'pv-ebs',
    'PV Instance Store 64-bit': 'pv-is',
    'HVM (NAT) EBS-Backed 64-bit': 'hvm-ebs-nat',
    'HVM (Graphics) EBS-Backed 64-bit': 'hvm-ebs-gfx'
}
machines_inv = {v: k for k, v in machines.items()}


def get_site(url="https://aws.amazon.com/amazon-linux-ami/"):
    page = requests.get(url)
    if page.status_code == 200:
        return page.content
    else:
        print("Site response status code is: " + page.status_code)
        exit(1)


def strip_site(bs_site):
    output = {}
    soup = BeautifulSoup(bs_site, "html.parser")
    table = soup.find('tbody')
    rows = table.find_all('tr')[1:]
    for row in rows:
        key = ''
        val = []
        col = row.find_all('td')
        for idx, c in enumerate(col):
            if idx == 0:
                key = c.get_text()
            else:
                val.append(c.get_text())
        output[key] = val
    return output


formated_data = strip_site(get_site())

if len(sys.argv) < 3:
    print('AVAILABLE REGIONS:')
    print('=======================')
    for region in formated_data.keys():
        print(region + ' (' + region_bindings[region] + ')')
    print('')
    print('AVAILABLE AMI TYPES:')
    print('=======================')
    for ami_type in machines.keys():
        print(ami_type + ' (' + machines[ami_type] + ')')
    print('')
    print('USAGE:')
    print('=======================')
    print(sys.argv[0] + ' region ami-type')
    print('')
    print('EXAMPLE:')
    print('=======================')
    print(sys.argv[0] + ' ap-south-1 hvm-ebs')
else:
    try:
        ami_type = None
        for k, v in enumerate(machines_inv):
            if v == sys.argv[2]:
                ami_type = k
        try:
            selected_region = region_bindings_inv[sys.argv[1]]
        except:
            print('[ERR] FIRST PARAM IS WRONG')
            exit(1)

        if ami_type is None:
            print('[ERR] SECOND PARAM IS WRONG')
            exit(1)

        print(formated_data[selected_region][ami_type])
        exit(0)
    except Exception as e:
        print('[ERR] SOMETHING WENT WRONG')
        print(e.message)
        exit(1)
