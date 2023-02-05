#coding=utf-8
import json,os

def dict_update(raw, new) :
    dict_update_iter( raw, new)
    dict_add(raw, new)

def dict_update_iter(raw, new):
    for key in raw:
        if key not in new. keys():
            continue
        if isinstance( raw[key], dict) and isinstance(new[key], dict):
            dict_update( raw[key], new[key])
        else:
            raw[key] = new [key]
def dict_add(raw, new) :
    update_dict = []
    for key in new :
        if key not in raw.keys() :
            update_dict[key] = new[key]
    raw.update(update_dict)

def cleandb(dbdict):
    del dbdict["ownership"]
    del dbdict["_stats"]
    del dbdict['flags']
    return dbdict

lod1=os.getcwd()
sdr1=os.listdir(lod1+'/json/zh_Hans')
for sdr1i in sdr1:
    with open(lod1+'/json/zh_Hans/'+sdr1i,"r") as test2:
        tts=test2.read()
        ttss=json.loads(tts)
        with open(lod1+'/en-db/'+sdr1i[:-4]+'db',"r") as test3:
            strr=''
            mum=test3.readlines()
            for i in mum:
                ij=json.loads(i)
                if ij['name'] in ttss:
                    sdd=ttss.get(ij['name'])
                    if (sdd['name']!=''):
                        if sdd.__contains__('items')==True:
                            if sdd['name']:
                                for jsonitemsname in sdd['items']:
                                    for dbitemsnum in range(len(ij['items'])):
                                        if ij['items'][dbitemsnum]['name']==jsonitemsname:
                                            dict_update(ij['items'][dbitemsnum],sdd['items'][jsonitemsname])
                                            cleandb(ij['items'][dbitemsnum])        
                            del sdd['items']          
                        dict_update(ij,sdd)
                        ij=cleandb(ij)
                        strr=strr+str(json.dumps(ij,ensure_ascii=False))+'\n'
                    
            with open(lod1+'/zh-db/'+sdr1i[:-4]+'db','w') as test4:
                test4.write(strr)
