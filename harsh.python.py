import json


dict_obj = {'states data':[
    {
        'state':'uttar pradesh',
        'capital':'lucknow'
        },

    {
        'state':'manipur',
        'capital':'imphal'
        },

    {
        'state':'nagaland',
        'capital':'kohima'
        },

    {
        'state':'rajasthan',
        'capital':'jaipur'
        },

    {
        'state':'punjab',
        'capital':'chandigarh'
        },

    {
        'state':'sikkim',
        'capital':'gangtok'
        },

    {
        'state':'jharkhand',
        'capital':'ranchi'
        }
]
    }

write_file = open('C:/Users/LENOVO/AppData/Local/Programs/Python/Python311/state.json','w')
json.dump(dict_obj,write_file)
