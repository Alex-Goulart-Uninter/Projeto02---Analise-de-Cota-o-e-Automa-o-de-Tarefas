#Importando as Bibliotencas
import yfinance
import time
import pyautogui
import pyperclip
import webbrowser
from time import sleep

#Buscando os Dados de uma Ação Automaticamente
ticker = input("Digite o código da ação: ")
data_inicial = input("Digite data inicial (ano-mês-dia): ")
data_final = input("Digite data final (ano-mês-dia): ")
dados = yfinance.Ticker(ticker)
tabela = dados.history(start=data_inicial, end=data_final)

#Selecionando Apenas a Coluna de Fechamento (Close)
fechamento = tabela.Close

#Gerando as Estatísticas Calculando a Maxima, Minima e Media
maxima = round(fechamento.max(),2)
minima = round(fechamento.min(),2)
media = round(fechamento.mean(),2)

print(maxima)
print(minima)
print(media)

#Adicionando Automaticamente o Destinatario, Assunto, Mensagem e enviando
destinatario = "alex.m.goulart1984@gmail.com"
assunto = "Projeto Analise de Cotações 2023"

mensangem = f"""
Bom dia!

Conforme solicitado segue abaixo a análise das cotações {ticker} do período solicitado {data_inicial} á {data_final}

Cotação máxima: R$ {maxima}
Cotação minima: R$ {minima}
Valor médio: R$ {media}

Dúvidas estou á disposição.

Atte..
"""
# configurar uma pausa entre as ações do pyautogui
pyautogui.PAUSE = 3

# abrir o navegador no gmail
webbrowser.open("https://mail.google.com/mail/u/1/?ogbl#inbox")
sleep(3)

# clicar no botão "Escrever"
pyautogui.click(x=74, y=208)

# Preencher Para
pyperclip.copy(destinatario)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("tab")

# Preencher Assunto
pyperclip.copy(assunto)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("tab")

# Preencher corpo do e-mail
pyperclip.copy(mensangem)
pyautogui.hotkey("ctrl", "v")

# Clicar no botão enviar
pyautogui.click(x=844, y=687)

# fechar a aba
pyautogui.hotkey("ctrl", "fn", "f4")
print("E-mail enviado com sucesso!!!!")