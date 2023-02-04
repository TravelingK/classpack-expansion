#coding:utf-8
import json,os
import sys

jjson={}


lod1=os.getcwd()
for nnmaame in os.listdir(lod1+'/en-db/'):
    with open(lod1+'/en-db/'+nnmaame) as readmoster:
        masterreadline=readmoster.readlines()
        n=0
        for i in masterreadline:
            aas={}
            ijson=json.loads(i)
            aas['name']=ijson['name']
            aas.update({'prototypeToken':{'name':ijson['prototypeToken']['name']},'system':{'details':{'alignment':ijson['system']['details']['alignment'],'biography':{'value':ijson['system']['details']['alignment']}}}})
            aas['items']={}
                
            for key in ijson['items']:
                    
                aas['items'].update({key['name']:{'name':key['name'],'system':{'description':{'value':key['system']['description']['value']}}}})
                jjson[ijson['name']]=aas

    with open(lod1+'/json/en/'+nnmaame[:-3]+'.json','w') as mubiao:
        mubiao.write(json.dumps(jjson))
