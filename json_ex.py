import json

# with open('myfile.json','r') as fh:
#     data=json.load(fh)
# for k,v in data.items():
#     print(k +" ===> "+ str(v))

info={'Name':'Python Automation',
      'Duration': 5,
      'Start_Date':'16-05-2022',
      'Class_Room_Session':False,
      'Lab_Info':None}

with open('new_file.json','w') as fh:
    json.dump(info,fh)