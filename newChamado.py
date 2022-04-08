import requests as requests
import json

def jsonIndentado(obj):
    print(json.dumps(obj, indent=2))

def linha():
    print('-' * 100)


def novo_ticket(tokken, assunto, descricao=' ', email=' ', telefone=' ', nome=' '):
    url = 'https://apiintegracao.milvus.com.br/api/chamado/criar'
    url_teste = 'https://624476ba39aae3e3b75060ab.mockapi.io/kevin/Chamado'
    api_key = 'eKdpEYqaCUzT3TXTPwGo3xZb2HeEtas24xMK8VmOUi6nGVNoHiQSMVWxyFcA5wJPcQz5pvNRonOw2eVCo2twNRJPbTSpUp7W8F0KY'

    payload = dict(cliente_id=tokken, chamado_assunto=assunto, chamado_descricao=descricao,
                   chamado_email=email, chamado_telefone=telefone, chamado_contato=nome,
                   chamado_tecnico=" ", chamado_mesa="Mesa padrão", chamado_setor="Setor padrão",
                   chamado_categoria_primaria=" ", chamado_categoria_secundaria=" ")

    ticket_response = requests.post(url_teste, headers={'Authorization': api_key}, json=payload)

    if ticket_response.status_code == 201 or ticket_response.status_code == 200:
        #print('Ticket Criado com sucesso')
        #jsonIndentado(ticket_response)
        return ticket_response.json()['id']
    else:
        print(f'{ticket_response.text}\n{ticket_response.status_code}')



#ticket = novo_ticket('6YRGGA', 'Teste', 'teste@teste', '27 988850129', 'Kevin')
#print(ticket)

