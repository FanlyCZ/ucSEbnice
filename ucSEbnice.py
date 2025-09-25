#Package import
import json
import os
import inquirer
import colorama
import time
import random
from unidecode import unidecode

#Program version
ucSEbniceProgramVersion = "v1.0"
ucSEbniceVersionDate = "15.09.2025"

#Menu screen
def Menu():
    os.system('cls')
    print(colorama.Fore.LIGHTBLUE_EX + '''                                                                                          
                                                                                            
                ██  ██                                             ██                        
                ████    ▒████▒   ████████  ██                     ██                        
                ▒██▒   ▒██████   ████████  ██                     ██                        
                        ██▒  ▒█   ██        ██                                               
    ██    ██    ▓████▒  ██        ██        ██░███▒   ██░████    ████       ▓████▒   ░████▒  
    ██    ██   ███████  ███▒      ██        ███████▒  ███████▓   ████      ███████  ░██████▒ 
    ██    ██  ▓██▒  ▒█  ▒█████▒   ███████   ███  ███  ███  ▒██     ██     ▓██▒  ▒█  ██▒  ▒██ 
    ██    ██  ██░        ░█████▒  ███████   ██░  ░██  ██    ██     ██     ██░       ████████ 
    ██    ██  ██            ▒███  ██        ██    ██  ██    ██     ██     ██        ████████ 
    ██    ██  ██░             ██  ██        ██░  ░██  ██    ██     ██     ██░       ██       
    ██▒  ███  ▓██▒  ░█  █▒░  ▒██  ██        ███  ███  ██    ██     ██     ▓██▒  ░█  ███░  ▒█ 
    ▓███████   ███████  ███████▒  ████████  ███████▒  ██    ██  ████████   ███████  ░███████ 
    ▓███░██    ▓████▒  ░█████▒   ████████  ██░███▒   ██    ██  ████████    ▓████▒   ░█████▒ 
                                                                                            
                                                                                            
                                                                                            
                                                                                            
    ''' + colorama.Fore.RESET)
    MenuQ = [inquirer.List("MenuQ", choices=["Vybrat úlohu", "Manuál", f"{ucSEbniceProgramVersion}", "Odejít"])]
    MenuA = inquirer.prompt(MenuQ)
    match MenuA['MenuQ']:
        case str("Vybrat úlohu"):
            TaskSelect()
        case "Manuál":
            Manual()
        case "Odejít":
            os.system('cls')
            exit()
        case __:
            PatchNotes()

#Patch Notes screen
def PatchNotes():
    os.system('cls')
    print(colorama.Fore.LIGHTBLUE_EX + f'Aktuální verze: {ucSEbniceProgramVersion} [{ucSEbniceVersionDate}]' + colorama.Fore.RESET)
    print('''
    - Stabilní verze
''')
    os.system('pause')
    Menu()

#Manual screen
def Manual():
    os.system('cls')
    print(colorama.Fore.LIGHTBLUE_EX + f'To be added...' + colorama.Fore.RESET)
    os.system('pause')
    Menu()

#Task selection screen
def TaskSelect():
    os.system('cls')
    fileContents = os.listdir('data')
    if len(fileContents) != 0:
        fileContents.append(f'{colorama.Back.GREEN}Zpět do menu{colorama.Back.RESET}')
        MenuQ = [inquirer.List(name='MenuQ', message=colorama.Fore.LIGHTBLUE_EX + 'Výběr úloh' + colorama.Fore.RESET, choices=fileContents)]
        MenuA = inquirer.prompt(MenuQ)['MenuQ']
        if MenuA == f'{colorama.Back.GREEN}Zpět do menu{colorama.Back.RESET}':
            Menu()
        MinigameSelect(MenuA)
    else:
        print(f'[{colorama.Fore.YELLOW}?{colorama.Fore.RESET}] {colorama.Fore.LIGHTBLUE_EX}Výběr úloh{colorama.Fore.RESET}:')
        print(colorama.Fore.RED + '     Žádné úlohy nebyly nalezeny. Pokud máte nějaké úlohy, vložte je do složky "/data" \n\n\n\n\n' + colorama.Fore.RESET)
        os.system('pause')
        Menu()

#Minigame selection
def MinigameSelect(file):
    os.system('cls')
    with open(f"data/{file}", "r", encoding="UTF-8") as outfile:
        content = json.load(outfile)
        outfile.close()
    obsah = list(content.keys())
    obsah.append(f'{colorama.Back.GREEN}Zpět do menu{colorama.Back.RESET}')
    MenuQ = [inquirer.List(name='MenuQ', message=colorama.Fore.LIGHTBLUE_EX + 'Výběr miniher' + colorama.Fore.RESET, choices=obsah)]
    MenuA = inquirer.prompt(MenuQ)['MenuQ']
    if MenuA == f'{colorama.Back.GREEN}Zpět do menu{colorama.Back.RESET}':
        Menu()
    match MenuA:
        case 'Jeden ze čtyř':
            JedenZeCtyr(content, file)
        case 'Doplň odpověď':
            DoplnOdpoved(content, file)
        case __:
            print(f'{colorama.Fore.RED}CHYBA: Neplatný formát miniher{colorama.Fore.RESET}')
            os.system('pause')

#'Jeden ze čtyř' Minigame
def JedenZeCtyr(content, file):
    correct = 0
    fail = 0
    os.system('cls')
    content = content["Jeden ze čtyř"]
    otazky = list(content.keys())
    random.shuffle(otazky)
    for otazka in otazky:
        os.system('cls')
        odpovedi = []
        for x in content[otazka]:
            odpovedi.append(x)
        random.shuffle(odpovedi)
        Question = [inquirer.List(name='Answer', message=f'{colorama.Fore.LIGHTBLUE_EX}{otazka}{colorama.Fore.RESET}', choices=odpovedi)]
        Answer = inquirer.prompt(Question)['Answer']
        if Answer == content[otazka][0]:
            correct += 1
            os.system('cls')
            print(f'[{colorama.Fore.YELLOW}?{colorama.Fore.RESET}] {colorama.Fore.LIGHTBLUE_EX}{otazka}{colorama.Fore.RESET}')
            print(f'{colorama.Fore.GREEN}Správně:{colorama.Fore.RESET} {colorama.Fore.GREEN}{Answer}{colorama.Fore.RESET}\n\n')
            input('Stiskni ENTER pro pokračování...')
        else:
            fail += 1
            os.system('cls')
            print(f'[{colorama.Fore.YELLOW}?{colorama.Fore.RESET}] {colorama.Fore.LIGHTBLUE_EX}{otazka}{colorama.Fore.RESET}')
            print(f'{colorama.Fore.RED}Špatná odpověď: {colorama.Fore.RESET} {colorama.Fore.RED}{Answer}{colorama.Fore.RESET}')
            print(f'Správná odpověď: {colorama.Fore.GREEN}{content[otazka][0]}{colorama.Fore.RESET}\n\n')
            input('Stiskni ENTER pro pokračování...')
        os.system('cls')
        print(f'{colorama.Fore.LIGHTBLUE_EX}Postup{colorama.Fore.RESET}\n\n\nSprávně:{colorama.Fore.GREEN}{correct}{colorama.Fore.RESET}\nŠpatně:{colorama.Fore.RED}{fail}{colorama.Fore.RESET}\n\n')
        input('Stiskni ENTER pro pokračování...')
        
    #End Screen
    os.system('cls')
    print(f'{colorama.Fore.LIGHTBLUE_EX}Výsledky{colorama.Fore.RESET}\n\n\nSprávně:{colorama.Fore.GREEN}{correct}{colorama.Fore.RESET}\nŠpatně:{colorama.Fore.RED}{fail}{colorama.Fore.RESET}\nÚspěšnost: {colorama.Fore.YELLOW}{(correct / (correct + fail)) * 100}%{colorama.Fore.RESET}\n\n')
    input('Stiskni ENTER pro pokračování...')
    os.system('cls')
    MenuQ = [inquirer.List('MenuA', choices=['Opakovat', 'Zvolit jinou minihru', 'Ukončit úlohu'])]
    MenuA = inquirer.prompt(MenuQ)['MenuA']
    match MenuA:
        case 'Opakovat':
            with open(f"data/{file}", "r", encoding="UTF-8") as outfile:
                content = json.load(outfile)
                outfile.close()
            JedenZeCtyr(content ,file)
        case 'Zvolit jinou minihru':
            MinigameSelect(file)
        case 'Ukončit úlohu':
            Menu()

#'Doplň odpověď' Minigame
def DoplnOdpoved(content, file):
    correct = 0
    fail = 0
    os.system('cls')
    content = content["Doplň odpověď"]
    otazky = list(content.keys())
    random.shuffle(otazky)
    for otazka in otazky:
        os.system('cls')
        odpovedi = []
        for x in content[otazka]:
            odpovedi.append(x)
        random.shuffle(odpovedi)
        print(f'[{colorama.Fore.YELLOW}?{colorama.Fore.RESET}] {colorama.Fore.LIGHTBLUE_EX}{otazka}{colorama.Fore.RESET}')
        Answer = input(f'\n\n{colorama.Fore.YELLOW}Odpověď:{colorama.Fore.RESET} ')
        Answer = unidecode(Answer)
        SpravnaOdpovedOriginal = content[otazka][0].lower()
        SpravnaOdpovedFixed = content[otazka][0].lower()
        SpravnaOdpovedFixed = unidecode(SpravnaOdpovedFixed)
        if Answer.lower() == SpravnaOdpovedFixed:
            correct += 1
            os.system('cls')
            print(f'[{colorama.Fore.YELLOW}?{colorama.Fore.RESET}] {colorama.Fore.LIGHTBLUE_EX}{otazka}{colorama.Fore.RESET}')
            print(f'{colorama.Fore.GREEN}Správně:{colorama.Fore.RESET} {colorama.Fore.GREEN}{SpravnaOdpovedOriginal}{colorama.Fore.RESET}\n\n')
            input('Stiskni ENTER pro pokračování...')
        else:
            fail += 1
            os.system('cls')
            print(f'[{colorama.Fore.YELLOW}?{colorama.Fore.RESET}] {colorama.Fore.LIGHTBLUE_EX}{otazka}{colorama.Fore.RESET}')
            print(f'{colorama.Fore.RED}Špatná odpověď: {colorama.Fore.RESET} {colorama.Fore.RED}{Answer}{colorama.Fore.RESET}')
            print(f'Správná odpověď: {colorama.Fore.GREEN}{SpravnaOdpovedOriginal}{colorama.Fore.RESET}\n\n')
            input('Stiskni ENTER pro pokračování...')
        os.system('cls')
        print(f'{colorama.Fore.LIGHTBLUE_EX}Postup{colorama.Fore.RESET}\n\n\nSprávně:{colorama.Fore.GREEN}{correct}{colorama.Fore.RESET}\nŠpatně:{colorama.Fore.RED}{fail}{colorama.Fore.RESET}\n\n')
        input('Stiskni ENTER pro pokračování...')
        
    #End Screen
    os.system('cls')
    print(f'{colorama.Fore.LIGHTBLUE_EX}Výsledky{colorama.Fore.RESET}\n\n\nSprávně:{colorama.Fore.GREEN}{correct}{colorama.Fore.RESET}\nŠpatně:{colorama.Fore.RED}{fail}{colorama.Fore.RESET}\nÚspěšnost: {colorama.Fore.YELLOW}{(correct / (correct + fail)) * 100}%{colorama.Fore.RESET}\n\n')
    input('Stiskni ENTER pro pokračování...')
    os.system('cls')
    MenuQ = [inquirer.List('MenuA', choices=['Opakovat', 'Zvolit jinou minihru', 'Ukončit úlohu'])]
    MenuA = inquirer.prompt(MenuQ)['MenuA']
    match MenuA:
        case 'Opakovat':
            with open(f"data/{file}", "r", encoding="UTF-8") as outfile:
                content = json.load(outfile)
                outfile.close()
            DoplnOdpoved(content ,file)
        case 'Zvolit jinou minihru':
            MinigameSelect(file)
        case 'Ukončit úlohu':
            Menu()

#Unintencional start checker
if __name__ == "__main__":
    Menu()

#Doplň odpověď == Přidat tam ascii korekturu