import requests as requests
import json


def json_indentado(obj):
    print(json.dumps(obj, indent=2))


def linha():
    print('-' * 100)


def chamado():
    url = 'https://apiintegracao.milvus.com.br/api/chamado/listagem'
    api_key = 'eKdpEYqaCUzT3TXTPwGo3xZb2HeEtas24xMK8VmOUi6nGVNoHiQSMVWxyFcA5wJPcQz5pvNRonOw2eVCo2twNRJPbTSpUp7W8F0KY'

    payload = dict(filtro_body={
        "assunto": "",
        "codigo": "",
        "nome_contato": "",
        "email_conferencia": "",
        "data_criacao": "",
        "data_solucao": "",
        "status": "Atendendo",
        "tecnico": "",
        "cliente": "",
        "mesa_trabalho": "",
        "categoria_primaria": "",
        "categoria_secundaria": "",
        "total_avaliacao": '',
        "descricao_avaliacao": "",
        "setor": "",
        "tipo_ticket": "",
        "dispositivo": "",
        "possui_avaliacao": '',
        "prioridade": ''
    })

    chamado_response = requests.post(url, headers={'Authorization': api_key}, json=payload)

    if chamado_response.status_code == 201 or chamado_response.status_code == 200:
        print('consulta realizada')
        json_indentado(chamado_response.json()['lista'])
    else:
        print(f'{chamado_response.text}\n{chamado_response.status_code}')


chamado()
