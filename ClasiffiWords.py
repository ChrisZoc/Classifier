import json,io
with io.open('data.txt', 'w', encoding='utf-8') as f:
    f.write("[")
    with open('sdal.json') as data_file:    
        jsonfile = json.load(data_file)
        
        for data in jsonfile:
            if(jsonfile[data]["obj"]=="V"):
                s="{"+data+","+jsonfile[data]["pleasantness"]+"},\n"
                f.write(s)

    f.write("]")
f.close            