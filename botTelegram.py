import telebot
from telebot import types
import telegram

import newChamado as nw
api_Kevin_Bot_bot = '5273052420:AAGDUK0qZc1Sx_0mg2fjIbA9S7ISJ2PQQcI'
api_Kevin_Pot_Bot = '2113338109:AAEvNb4iqeueL7c4w2hoZAbcBkmMBO8CwQA'


bot = telebot.TeleBot(api_Kevin_Pot_Bot)

user_dict = {}

error = f'Erro durante a criação do Chamado...\nInsira o comando para iniciar novamente:\n/novo_chamado'

def userInput(message):
    print(f'{message.from_user.first_name}: {message.text}')

class User:
    def __init__(self, assunto):
        self.assunto = assunto
        self.nome = None
        self.desc = None
        self.confirm = None


@bot.message_handler(commands=['start', 'novo_chamado'])
#Verificar primeiro se o numero do cliente pertence a base de dados, depois de comparar abre o chamado para este numero, se não adiciona este numero para a impresa da pessoa
# verificando se o cliente esta cadastrado

# cadastrando o cliente no milvus

def send_welcome(message):
    msg = bot.send_message(message.chat.id, text="""*
Iniciando abertura de chamado...*
Insira o assunto: 
""", parse_mode=telegram.ParseMode.MARKDOWN)
    userInput(message)
    bot.register_next_step_handler(msg, process_assunto_step)


def process_assunto_step(message):
    try:
        chat_id = message.chat.id
        assunto = message.text
        if assunto == '/novo_chamado':
            send_welcome(message)
        else:
            user = User(assunto)
            user_dict[chat_id] = user
            msg = bot.send_message(chat_id, 'Nome: ')
            userInput(message)
            bot.register_next_step_handler(msg, process_nome_step)
    except Exception as e:
        bot.reply_to(message, error)


def process_nome_step(message):
    try:
        chat_id = message.chat.id
        nome = message.text
        if nome == '/novo_chamado':
            send_welcome(message)
        else:
            user = user_dict[chat_id]
            user.nome = nome
            msg = bot.send_message(chat_id, 'Descrição: ')
            userInput(message)
            bot.register_next_step_handler(msg, process_desc_step)
    except Exception as e:
        bot.reply_to(message, error)


def process_desc_step(message):
    try:
        chat_id = message.chat.id
        desc = message.text
        if desc == '/novo_chamado':
            send_welcome(message)
        else:
            user = user_dict[chat_id]
            user.desc = desc
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=2,selective=True,
                                               input_field_placeholder='Sim ou Não')
            markup.add('Sim', 'Não')
            msg = bot.send_message(chat_id,
                                   'Confirma abertura de chamado com estes dados?\n\n*Assunto:* ' + user.assunto + '\n*Nome:* ' + user.nome + '\n*Descrição:* ' + user.desc,
                                   reply_markup=markup, parse_mode=telegram.ParseMode.MARKDOWN)
            userInput(message)
            bot.register_next_step_handler(msg, process_confirm_step)
    except Exception as e:
        bot.reply_to(message, error)


def process_confirm_step(message):
    try:
        chat_id = message.chat.id
        confirm = message.text
        if confirm == '/novo_chamado':
            send_welcome(message)
        else:
            userInput(message)
            if (confirm == u'Sim') | (confirm == u'sim'):
                user = user_dict[chat_id]
                user.confirm = confirm
                ticket = nw.novo_ticket(tokken='6YRGGA',assunto=user.assunto,descricao=user.desc,nome=user.nome)
                bot.send_message(chat_id,f'Chamado #{ticket} aberto com sucesso...\nAssunto: ' + user.assunto + '\nNome: ' + user.nome + '\nDescrição: ' + user.desc)
            elif (confirm == u'Não') | (confirm == u'não'):
                # Menu para selecionar o que mudar
                bot.send_message(chat_id, 'Abertura de Chamado Cancelado.\nInsira o comando para iniciar abertura de Ticket:\n/novo_chamado')
            else:
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=2,
                                                   selective=True,
                                                   input_field_placeholder='Sim ou Não')
                markup.add('Sim', 'Não')
                msg = bot.reply_to(message, 'Opção não encontrada.')
                bot.send_message(chat_id,'Confirmar abertura de Ticket?',reply_markup=markup)
                bot.register_next_step_handler(msg, process_confirm_step)
                return

    except Exception as e:
        bot.reply_to(message, error)


# Enable saving next step handlers to file "./.handlers-saves/step.save".
# Delay=2 means that after any change in next step handlers (e.g. calling register_next_step_handler())
# saving will hapen after delay 2 seconds.
bot.enable_save_next_step_handlers(delay=2)

# Load next_step_handlers from save file (default "./.handlers-saves/step.save")
# WARNING It will work only if enable_save_next_step_handlers was called!
bot.load_next_step_handlers()

print('Rodando...')
bot.infinity_polling()
print('Parando...')