# -*- coding: utf-8 -*- 
import paho.mqtt.client as mqtt
import yaml
import re

f = open("../config.yml", "r+")
confdata = yaml.load(f)

host = confdata['mqtthost']
#'192.168.0.10'
port = confdata['mqttport']
#1883
topic = confdata['topic']
#'/PRISM/SENSOR/'

while True:
    di = input()
    if(di == "Press any key to stop"):
        break

rstrp = r'^\[(\d+),(\d+)\] .*, prob = ([\d\.]+)\s+(\(.*\)).*'
rstrpc = re.compile(rstrp)
rstrg = r'^Predicted g.* = ([MF]),(\d+).*'
rstrgc = re.compile(rstrg)
rstre = r'^Predicted e.* = (\w+).*'
rstrec = re.compile(rstre)
rstrh = r'^Head.* = ([\d\.\-\;]+).*'
rstrhc = re.compile(rstrh)

while True:
    n = 0
    person = []
    di = input()
    print('1:'+di)
    res = rstrpc.match(di)
    if res:
        while True:
            n += 1
            print(res.groups())
            person.append(res.groups())
            di = input()
            print('2:'+di)
            res = rstrpc.match(di)
            if res:
                person.append(res.groups())
            else:
                break
        for i in range(n):
            res = rstrgc.match(di)
            person[i] += res.groups()
            di = input()
            print('3:'+di)
            res = rstrec.match(di)
            person[i] += res.groups()
            di = input()
            print('4:'+di)
            res = rstrhc.match(di)
            person[i] += res.groups()
            if i < n:
                di = input()
        print(person)
