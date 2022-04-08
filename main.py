import requests
import json
#logica: pegar a data de hoje, menos 6 meses para obter a data de 6 meses atras

def linha():
    print('-'*100)

def jsonIndentado(obj):
    print(json.dumps(obj, indent=2))

total = 1745

url = 'https://apiintegracao.milvus.com.br/api/dispositivos/listagem/'
tokken = 'eKdpEYqaCUzT3TXTPwGo3xZb2HeEtas24xMK8VmOUi6nGVNoHiQSMVWxyFcA5wJPcQz5pvNRonOw2eVCo2twNRJPbTSpUp7W8F0KY'
headers = {'Authorization' : tokken}
params = {
    'order_by':'id',
    'total_registros':total
    }
data = requests.post(url, headers=headers, params=params).json()

for items in data['lista']:
    if items['sistema_operacional'] != None:
        jsonIndentado(items)


