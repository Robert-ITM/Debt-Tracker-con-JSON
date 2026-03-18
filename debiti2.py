import json 
import os


file_debiti = 'debiti.json'
def Creazione_debito():
    if os.path.exists(file_debiti):
        with open(file_debiti, 'r') as f:
             return json.load(f)
    else:
        return {}
def Aggiornamento_debito(debiti):
    with open(file_debiti, 'w') as f:
        json.dump(debiti, f, indent = 2)
def aggiungi_debito() :
    Nome = input('Nome: ').strip().capitalize()
    Debito = float(input('Quanto deve? '))
    if Nome in debiti :
        debiti[Nome] += Debito
    else:
        debiti[Nome] = Debito
    Aggiornamento_debito(debiti)
    print(f'{Nome} deve a Creatore: {debiti[Nome]}€')
def mostra_debito():
    for nome, debito in debiti.items():
        print(f'{nome} deve a Creatore: {debito}€')
def sottrai_debito():
    Nome = input('Nome: ').strip().capitalize()
    Debito = float(input('Quanto ha pagato? '))
    if Nome in debiti:
        debiti[Nome] -= Debito
        Aggiornamento_debito(debiti)
        print(f'{Nome} deve a Creatore: {debiti[Nome]}€')
    else:
        print(f'{Nome} non è nella lista dei debiti.')
def menu():
    while True:
        print('1. Aggiungi debito')
        print('2. Mostra debiti')
        print('3. Sottrai debito')
        print('4. Esci')
        scelta = input('Scegli un\'opzione: ')
        if scelta == '1':
            aggiungi_debito()
        elif scelta == '2':
            mostra_debito()
        elif scelta == '3':
            sottrai_debito()
        elif scelta == '4':
            break
        else:
            print('Scelta non valida. Riprova.')
debiti = Creazione_debito()
menu()