#coding=utf-8
import json,os

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
                    ij.update(sdd)
                    
                    strr=strr+str(json.dumps(ij,ensure_ascii=False))+'\n'
            with open(lod1+'/zh-db/'+sdr1i[:-4]+'db','w') as test4:
                test4.write(strr)