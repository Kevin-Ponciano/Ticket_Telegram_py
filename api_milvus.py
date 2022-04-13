import requests as requests

api_key = 'eKdpEYqaCUzT3TXTPwGo3xZb2HeEtas24xMK8VmOUi6nGVNoHiQSMVWxyFcA5wJPcQz5pvNRonOw2eVCo2twNRJPbTSpUp7W8F0KY'
headers = {'Authorization': api_key}


def pesquisar_contatos(celular):
    url = 'https://apiintegracao.milvus.com.br/api/cliente/contato/pesquisar'
    params = {'telefone': f'{celular}'}

    pesquisa_response = requests.get(url, headers=headers, params=params)

    if pesquisa_response.status_code == 201 or pesquisa_response.status_code == 200:
        # Realizar tratamento caso não encontre o numero
        print(pesquisa_response.text)
        # print(pesquisa_response.json())
        # print(pesquisa_response.json()[0]['cliente_nome'])
        # print(pesquisa_response.json()[0]['cliente_id'])
    else:
        print(pesquisa_response.text)


def novo_ticket(tokken, assunto, descricao=' ', email=' ', telefone=' ', nome=' '):
    # Realizar tratamento caso os paramentros obrigatorios nao sejam fornecidos
    url = 'https://apiintegracao.milvus.com.br/api/chamado/criar'
    url_teste = 'https://624476ba39aae3e3b75060ab.mockapi.io/kevin/Chamado'

    payload = dict(cliente_id=tokken, chamado_assunto=assunto, chamado_descricao=descricao,
                   chamado_email=email, chamado_telefone=telefone, chamado_contato=nome,
                   chamado_tecnico=" ", chamado_mesa="Mesa padrão", chamado_setor="Setor padrão",
                   chamado_categoria_primaria=" ", chamado_categoria_secundaria=" ")

    ticket_response = requests.post(url_teste, headers=headers, json=payload)

    if ticket_response.status_code == 201 or ticket_response.status_code == 200:
        # print('Ticket Criado com sucesso')
        # jsonIndentado(ticket_response)
        return ticket_response.json()['id']
    else:
        print(f'{ticket_response.text}\n{ticket_response.status_code}')


def pesqueisar_chamado(numero_ticket):
    url = 'https://apiintegracao.milvus.com.br/api/chamado/listagem'

    payload = dict(filtro_body={
        "assunto": "",
        "codigo": f'{numero_ticket}',
        "nome_contato": "",
        "email_conferencia": "",
        "data_criacao": "",
        "data_solucao": "",
        "status": " ",
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
        print(chamado_response.json()['lista'])
    else:
        print(f'{chamado_response.text}\n{chamado_response.status_code}')


pesquisar_contatos(27988850129)
pesqueisar_chamado(18949)
