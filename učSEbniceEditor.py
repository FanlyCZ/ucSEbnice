#Package import
import json
import os
import inquirer
import colorama
import time


#Program version
ucSEbniceProgramVersion = "v1.0"
ucSEbniceVersionDate = "24.09.2025"
ucSEbniceMinigames = ['Jeden ze čtyř', 'Doplň odpověď']

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
    print(colorama.Fore.LIGHTRED_EX + '''
                                                                                            
                                ▄▄▄▄▄▄▄▄        ▄▄     ██                                  
                                ██▀▀▀▀▀▀        ██     ▀▀       ██                         
                                ██         ▄███▄██   ████     ███████    ▄████▄    ██▄████ 
                                ███████   ██▀  ▀██     ██       ██      ██▀  ▀██   ██▀     
                                ██        ██    ██     ██       ██      ██    ██   ██      
                                ██▄▄▄▄▄▄  ▀██▄▄███  ▄▄▄██▄▄▄    ██▄▄▄   ▀██▄▄██▀   ██      
                                ▀▀▀▀▀▀▀▀    ▀▀▀ ▀▀  ▀▀▀▀▀▀▀▀     ▀▀▀▀     ▀▀▀▀     ▀▀      
                                                                                                                            
                                                                                                                            
                                                                                                                            
                                                                                            
''' + colorama.Fore.RESET)
    MenuQ = [inquirer.List('MenuQ', choices=['Vytvořit novou úlohu', 'Upravit úlohu', 'Vymazat úlohu', f"{ucSEbniceProgramVersion}", "Odejít"])]
    MenuA = inquirer.prompt(MenuQ)
    match MenuA['MenuQ']:
        case 'Vytvořit novou úlohu':
            TaskCreation()
        case 'Upravit úlohu':
            TaskEdit()
        case 'Vymazat úlohu':
            TaskDelete()
        case 'Odejít':
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

#Task creation screen
def TaskCreation():
    os.system('cls')
    check = False
    while check == False:
        TaskName = input(f'{colorama.Fore.LIGHTBLUE_EX}Pojmenujte novou úlohu: {colorama.Fore.RESET}')
        if len(TaskName.replace(' ', '-')) != 0 and TaskName.startswith(' ') != True:
            check = True

    with open(f"data/{TaskName}.json", 'w', encoding='UTF-8') as outfile:
        outfile.close()
    
    #Minigames
    check = False
    while check == False:
        os.system('cls')
        print(f'{colorama.Fore.LIGHTBLUE_EX}Úloha: {colorama.Fore.LIGHTGREEN_EX}{TaskName}.json{colorama.Fore.RESET}\n')
        print(f'''{colorama.Fore.LIGHTBLUE_EX}Minihry:
        {colorama.Fore.YELLOW}- Jeden ze čtyř [Vybírání jedné správné odpovědi mezi třemi špatnými. Pořadí odpovědí je vždy náhodné]
        {colorama.Fore.GREEN}- Doplň odpověď [Textové doplňování odpovědí na otázky] #Přidat "To nebo ono"
{colorama.Fore.RESET}''')
        TaskGamesQ = [inquirer.Checkbox('TaskGamesQ', message='Vyber minihry pro úlohu (použij šipky)', choices=ucSEbniceMinigames)]
        TaskGamesA = inquirer.prompt(TaskGamesQ)
        if len(TaskGamesA['TaskGamesQ']) != 0:
            check = True

    #Save minigames values
    content = {}
    for x in TaskGamesA['TaskGamesQ']:
        content.update({str(x) : {}})  

    with open(f"data/{TaskName}.json", 'w', encoding='UTF-8') as outfile:
        json.dump(content, outfile, indent=4)
        outfile.close()

    Loading(TaskName)

#Task edit screen
def TaskEdit():
    os.system('cls')
    fileContents = os.listdir('data')
    fileContents.append('Odejít zpět do menu')
    if len(fileContents) != 0:
        MenuQ = [inquirer.List(name='MenuQ', message=colorama.Fore.LIGHTBLUE_EX + 'Výběr úloh' + colorama.Fore.RESET, choices=fileContents)]
        MenuA = inquirer.prompt(MenuQ)['MenuQ']
    else:
        print(f'[{colorama.Fore.YELLOW}?{colorama.Fore.RESET}] {colorama.Fore.LIGHTBLUE_EX}Výběr úloh{colorama.Fore.RESET}:')
        print(colorama.Fore.RED + '     Žádné úlohy nebyly nalezeny. Pokud máte nějaké úlohy, vložte je do složky "/data" \n\n\n\n\n' + colorama.Fore.RESET)
        os.system('pause')
        Menu()
    if MenuA == "Odejít zpět do menu":
        Menu()
    else:
        Loading(MenuA.replace(".json", ""))

#Loading minigame function
def Loading(TaskName):
    #Minigame: 'Jeden ze čtyř'
    with open(f"data/{TaskName}.json", 'r', encoding='UTF-8') as outfile:
        data = json.load(outfile)
        outfile.close()
    if 'Jeden ze čtyř' in data.keys():
        os.system('cls')
        input(f'{colorama.Fore.YELLOW}Stiskni ENTER pro načtení Tvořivých nástrojů...{colorama.Fore.RESET}')
        content = JedenZeCtyrMaker(TaskName, data)
    if 'Doplň odpověď' in data.keys():
        os.system('cls')
        input(f'{colorama.Fore.YELLOW}Stiskni ENTER pro načtení Tvořivých nástrojů...{colorama.Fore.RESET}')
        content = DoplnOdpovedMaker(TaskName, data)

    # Minigame: 'Jeden ze čtyř'
    # with open(f"data/{TaskName}.json", 'r', encoding='UTF-8') as outfile:
    #     data = json.load(outfile)
    #     outfile.close()
    # if 'Jeden ze čtyř' in data.keys():
    #     pass

#Task delete screen
def TaskDelete():
    while True:
        os.system('cls')
        fileContents = os.listdir('data')
        fileContents.append('Odejít zpět do menu')
        if len(fileContents) != 0:
            MenuQ = [inquirer.List(name='MenuQ', message=colorama.Fore.LIGHTBLUE_EX + 'Výběr úloh' + colorama.Fore.RESET, choices=fileContents)]
            MenuA = inquirer.prompt(MenuQ)['MenuQ']
        else:
            print(f'[{colorama.Fore.YELLOW}?{colorama.Fore.RESET}] {colorama.Fore.LIGHTBLUE_EX}Výběr úloh{colorama.Fore.RESET}:')
            print(colorama.Fore.RED + '     Žádné úlohy nebyly nalezeny. Pokud máte nějaké úlohy, vložte je do složky "/data" \n\n\n\n\n' + colorama.Fore.RESET)
            os.system('pause')
            Menu()
        if MenuA == "Odejít zpět do menu":
            Menu()
        else:
            os.remove(f"data/{MenuA}")

#"Jeden ze čtyř" maker function
def JedenZeCtyrMaker(Name, content):
    while True:
        os.system('cls')
        print(f'{colorama.Fore.LIGHTBLUE_EX}Úloha: {colorama.Fore.LIGHTGREEN_EX}{Name}.json')
        print(f'{colorama.Fore.YELLOW}Minihra:{colorama.Fore.RESET} {colorama.Fore.GREEN}Jeden ze čtyř{colorama.Fore.RESET}')
        print(f'{colorama.Fore.LIGHTRED_EX}Počet otázek: {colorama.Fore.LIGHTMAGENTA_EX}{len(content['Jeden ze čtyř'])}{colorama.Fore.RESET}\n\n\n')
        MakerQ = [inquirer.List('MakerQ', choices=['Vytvořit novou otázku', 'Upravit otázku', 'Smazat otázku', 'Uložit a odejít'])]
        MakerA = inquirer.prompt(MakerQ)
        match MakerA['MakerQ']:

            case 'Vytvořit novou otázku':
                questionName = f'{colorama.Fore.RED}___'
                questionAnswer = f'{colorama.Fore.RED}___'
                questionWrongAnswer1 = f'{colorama.Fore.RED}___'
                questionWrongAnswer2 = f'{colorama.Fore.RED}___'
                questionWrongAnswer3 = f'{colorama.Fore.RED}___'

                while questionWrongAnswer3 == f'{colorama.Fore.RED}___':
                    os.system('cls')
                    print(f'''{colorama.Fore.LIGHTBLUE_EX}Úloha: {colorama.Fore.LIGHTGREEN_EX}{Name}.json\n\n\n
    {colorama.Fore.LIGHTBLUE_EX}Zadání otázky:{colorama.Fore.RESET} {questionName}
    {colorama.Fore.LIGHTBLUE_EX}Správná odpověď:{colorama.Fore.RESET} {questionAnswer}
    {colorama.Fore.LIGHTBLUE_EX}Špatná odpověď 1:{colorama.Fore.RESET} {questionWrongAnswer1}
    {colorama.Fore.LIGHTBLUE_EX}Špatná odpověď 2:{colorama.Fore.RESET} {questionWrongAnswer2}
    {colorama.Fore.LIGHTBLUE_EX}Špatná odpověď 3:{colorama.Fore.RESET} {questionWrongAnswer3}
    {colorama.Fore.RESET}''')
                    
                    if questionName == f'{colorama.Fore.RED}___':
                        questionName = input(f'{colorama.Fore.LIGHTBLUE_EX}Zadání otázky:{colorama.Fore.RESET} ')
                        if questionName != '' and len(questionName.replace(' ','')) != 0:
                            continue
                        else:
                            questionName = f'{colorama.Fore.RED}___'
                            continue
                    if questionAnswer == f'{colorama.Fore.RED}___':
                        questionAnswer = input(f'{colorama.Fore.LIGHTBLUE_EX}Správná odpověď:{colorama.Fore.RESET} ')
                        if questionAnswer != '' and len(questionAnswer.replace(' ','')) != 0:
                            continue
                        else:
                            questionAnswer = f'{colorama.Fore.RED}___'
                            continue
                    if questionWrongAnswer1 == f'{colorama.Fore.RED}___':
                        questionWrongAnswer1 = input(f'{colorama.Fore.LIGHTBLUE_EX}Špatná odpověď 1:{colorama.Fore.RESET} ')
                        if questionWrongAnswer1 != '' and len(questionWrongAnswer1.replace(' ','')) != 0:
                            continue
                        else:
                            questionWrongAnswer1 = f'{colorama.Fore.RED}___'
                            continue
                    if questionWrongAnswer2 == f'{colorama.Fore.RED}___':
                        questionWrongAnswer2 = input(f'{colorama.Fore.LIGHTBLUE_EX}Špatná odpověď 2:{colorama.Fore.RESET} ')
                        if questionWrongAnswer2 != '' and len(questionWrongAnswer2.replace(' ','')) != 0:
                            continue
                        else:
                            questionWrongAnswer2 = f'{colorama.Fore.RED}___'
                            continue
                    if questionWrongAnswer3 == f'{colorama.Fore.RED}___':
                        questionWrongAnswer3 = input(f'{colorama.Fore.LIGHTBLUE_EX}Špatná odpověď 3:{colorama.Fore.RESET} ')
                        if questionWrongAnswer3 != '' and len(questionWrongAnswer3.replace(' ','')) != 0:
                            continue
                        else:
                            questionWrongAnswer3 = f'{colorama.Fore.RED}___'
                            continue

                os.system('cls')
                print(f'''{colorama.Fore.LIGHTBLUE_EX}Úloha: {colorama.Fore.LIGHTGREEN_EX}{Name}.json\n\n\n
    {colorama.Fore.LIGHTBLUE_EX}Zadání otázky:{colorama.Fore.RESET} {questionName}
    {colorama.Fore.LIGHTBLUE_EX}Správná odpověď:{colorama.Fore.RESET} {questionAnswer}
    {colorama.Fore.LIGHTBLUE_EX}Špatná odpověď 1:{colorama.Fore.RESET} {questionWrongAnswer1}
    {colorama.Fore.LIGHTBLUE_EX}Špatná odpověď 2:{colorama.Fore.RESET} {questionWrongAnswer2}
    {colorama.Fore.LIGHTBLUE_EX}Špatná odpověď 3:{colorama.Fore.RESET} {questionWrongAnswer3}
    {colorama.Fore.RESET}''')
                MakerQ = [inquirer.List('MakerQ', choices=['Uložit otázku', 'Zahodit otázku'])]
                MakerA = inquirer.prompt(MakerQ)
                match MakerA['MakerQ']:
                    case 'Uložit otázku':
                        content['Jeden ze čtyř'].update({questionName : [questionAnswer,questionWrongAnswer1,questionWrongAnswer2,questionWrongAnswer3]})
                    case 'Zahodit otázku':
                        pass

            case 'Upravit otázku':
                os.system('cls')
                otazky = list(content['Jeden ze čtyř'].keys())
                otazky.append('Odejít zpět do menu')
                EditQ = [inquirer.List('EditQ', message='Kterou otázku chcete upravit?', choices=otazky)]
                EditA = inquirer.prompt(EditQ)['EditQ']
                if EditA == 'Odejít zpět do menu':
                    break
                else:
                    try:
                        content['Jeden ze čtyř'].pop(str(EditA))
                    except:
                        print(f'\n\n{colorama.Fore.RED}CHYBA: Otázka nenalezena\n{colorama.Fore.RESET}')
                        os.system('pause')
                print(EditA)
                questionName = f'{EditA}'
                questionAnswer = f'{colorama.Fore.RED}___'
                questionWrongAnswer1 = f'{colorama.Fore.RED}___'
                questionWrongAnswer2 = f'{colorama.Fore.RED}___'
                questionWrongAnswer3 = f'{colorama.Fore.RED}___'

                while questionWrongAnswer3 == f'{colorama.Fore.RED}___':
                    os.system('cls')
                    print(f'''{colorama.Fore.LIGHTBLUE_EX}Úloha: {colorama.Fore.LIGHTGREEN_EX}{Name}.json\n\n\n
    {colorama.Fore.LIGHTBLUE_EX}Zadání otázky:{colorama.Fore.RESET} {questionName}
    {colorama.Fore.LIGHTBLUE_EX}Správná odpověď:{colorama.Fore.RESET} {questionAnswer}
    {colorama.Fore.LIGHTBLUE_EX}Špatná odpověď 1:{colorama.Fore.RESET} {questionWrongAnswer1}
    {colorama.Fore.LIGHTBLUE_EX}Špatná odpověď 2:{colorama.Fore.RESET} {questionWrongAnswer2}
    {colorama.Fore.LIGHTBLUE_EX}Špatná odpověď 3:{colorama.Fore.RESET} {questionWrongAnswer3}
    {colorama.Fore.RESET}''')

                    if questionAnswer == f'{colorama.Fore.RED}___':
                        questionAnswer = input(f'{colorama.Fore.LIGHTBLUE_EX}Správná odpověď:{colorama.Fore.RESET} ')
                        if questionAnswer != '' and len(questionAnswer.replace(' ','')) != 0:
                            continue
                        else:
                            questionAnswer = f'{colorama.Fore.RED}___'
                            continue
                    if questionWrongAnswer1 == f'{colorama.Fore.RED}___':
                        questionWrongAnswer1 = input(f'{colorama.Fore.LIGHTBLUE_EX}Špatná odpověď 1:{colorama.Fore.RESET} ')
                        if questionWrongAnswer1 != '' and len(questionWrongAnswer1.replace(' ','')) != 0:
                            continue
                        else:
                            questionWrongAnswer1 = f'{colorama.Fore.RED}___'
                            continue
                    if questionWrongAnswer2 == f'{colorama.Fore.RED}___':
                        questionWrongAnswer2 = input(f'{colorama.Fore.LIGHTBLUE_EX}Špatná odpověď 2:{colorama.Fore.RESET} ')
                        if questionWrongAnswer2 != '' and len(questionWrongAnswer2.replace(' ','')) != 0:
                            continue
                        else:
                            questionWrongAnswer2 = f'{colorama.Fore.RED}___'
                            continue
                    if questionWrongAnswer3 == f'{colorama.Fore.RED}___':
                        questionWrongAnswer3 = input(f'{colorama.Fore.LIGHTBLUE_EX}Špatná odpověď 3:{colorama.Fore.RESET} ')
                        if questionWrongAnswer3 != '' and len(questionWrongAnswer3.replace(' ','')) != 0:
                            continue
                        else:
                            questionWrongAnswer3 = f'{colorama.Fore.RED}___'
                            continue

                os.system('cls')
                print(f'''{colorama.Fore.LIGHTBLUE_EX}Úloha: {colorama.Fore.LIGHTGREEN_EX}{Name}.json\n\n\n
    {colorama.Fore.LIGHTBLUE_EX}Zadání otázky:{colorama.Fore.RESET} {questionName}
    {colorama.Fore.LIGHTBLUE_EX}Správná odpověď:{colorama.Fore.RESET} {questionAnswer}
    {colorama.Fore.LIGHTBLUE_EX}Špatná odpověď 1:{colorama.Fore.RESET} {questionWrongAnswer1}
    {colorama.Fore.LIGHTBLUE_EX}Špatná odpověď 2:{colorama.Fore.RESET} {questionWrongAnswer2}
    {colorama.Fore.LIGHTBLUE_EX}Špatná odpověď 3:{colorama.Fore.RESET} {questionWrongAnswer3}
    {colorama.Fore.RESET}''')
                content['Jeden ze čtyř'].update({questionName : [questionAnswer,questionWrongAnswer1,questionWrongAnswer2,questionWrongAnswer3]})
          
            case 'Smazat otázku':
                while True:
                    os.system('cls')
                    otazky = list(content['Jeden ze čtyř'].keys())
                    otazky.append('Odejít zpět do menu')
                    DeleteQ = [inquirer.List('DeleteQ', message='Kterou otázku chcete vymazat?', choices=otazky)]
                    DeleteA = inquirer.prompt(DeleteQ)['DeleteQ']
                    if DeleteA == 'Odejít zpět do menu':
                        break
                    else:
                        try:
                            content['Jeden ze čtyř'].pop(str(DeleteA))
                        except:
                            print(f'\n\n{colorama.Fore.RED}CHYBA: Otázka nenalezena\n{colorama.Fore.RESET}')
                            os.system('pause')

            case 'Uložit a odejít':
                with open(f"data/{Name}.json", 'w', encoding='UTF-8') as outfile:
                    json.dump(content, outfile, indent=4)
                    outfile.close()
                return

#"Doplň odpověď" maker function
def DoplnOdpovedMaker(Name, content):
    while True:
        os.system('cls')
        print(f'{colorama.Fore.LIGHTBLUE_EX}Úloha: {colorama.Fore.LIGHTGREEN_EX}{Name}.json')
        print(f'{colorama.Fore.YELLOW}Minihra:{colorama.Fore.RESET} {colorama.Fore.GREEN}Doplň odpověď{colorama.Fore.RESET}')
        print(f'{colorama.Fore.LIGHTRED_EX}Počet otázek: {colorama.Fore.LIGHTMAGENTA_EX}{len(content['Doplň odpověď'])}{colorama.Fore.RESET}\n\n\n')
        MakerQ = [inquirer.List('MakerQ', choices=['Vytvořit novou otázku', 'Upravit otázku', 'Smazat otázku', 'Uložit a odejít'])]
        MakerA = inquirer.prompt(MakerQ)
        match MakerA['MakerQ']:

            case 'Vytvořit novou otázku':
                questionName = f'{colorama.Fore.RED}___'
                questionAnswer = f'{colorama.Fore.RED}___'

                while questionAnswer == f'{colorama.Fore.RED}___':
                    os.system('cls')
                    print(f'''{colorama.Fore.LIGHTBLUE_EX}Úloha: {colorama.Fore.LIGHTGREEN_EX}{Name}.json\n\n\n
    {colorama.Fore.LIGHTBLUE_EX}Zadání otázky:{colorama.Fore.RESET} {questionName}
    {colorama.Fore.LIGHTBLUE_EX}Správná odpověď:{colorama.Fore.RESET} {questionAnswer}
    {colorama.Fore.RESET}''')
                    
                    if questionName == f'{colorama.Fore.RED}___':
                        questionName = input(f'{colorama.Fore.LIGHTBLUE_EX}Zadání otázky:{colorama.Fore.RESET} ')
                        if questionName != '' and len(questionName.replace(' ','')) != 0:
                            continue
                        else:
                            questionName = f'{colorama.Fore.RED}___'
                            continue
                    if questionAnswer == f'{colorama.Fore.RED}___':
                        questionAnswer = input(f'{colorama.Fore.LIGHTBLUE_EX}Správná odpověď:{colorama.Fore.RESET} ')
                        if questionAnswer != '' and len(questionAnswer.replace(' ','')) != 0:
                            continue
                        else:
                            questionAnswer = f'{colorama.Fore.RED}___'
                            continue
                os.system('cls')
                print(f'''{colorama.Fore.LIGHTBLUE_EX}Úloha: {colorama.Fore.LIGHTGREEN_EX}{Name}.json\n\n\n
    {colorama.Fore.LIGHTBLUE_EX}Zadání otázky:{colorama.Fore.RESET} {questionName}
    {colorama.Fore.LIGHTBLUE_EX}Správná odpověď:{colorama.Fore.RESET} {questionAnswer}
    {colorama.Fore.RESET}''')
                MakerQ = [inquirer.List('MakerQ', choices=['Uložit otázku', 'Zahodit otázku'])]
                MakerA = inquirer.prompt(MakerQ)
                match MakerA['MakerQ']:
                    case 'Uložit otázku':
                        content['Doplň odpověď'].update({questionName : [questionAnswer]})
                    case 'Zahodit otázku':
                        pass

            case 'Upravit otázku':
                os.system('cls')
                otazky = list(content['Doplň odpověď'].keys())
                otazky.append('Odejít zpět do menu')
                EditQ = [inquirer.List('EditQ', message='Kterou otázku chcete upravit?', choices=otazky)]
                EditA = inquirer.prompt(EditQ)['EditQ']
                if EditA == 'Odejít zpět do menu':
                    break
                else:
                    try:
                        content['Doplň odpověď'].pop(str(EditA))
                    except:
                        print(f'\n\n{colorama.Fore.RED}CHYBA: Otázka nenalezena\n{colorama.Fore.RESET}')
                        os.system('pause')
                print(EditA)
                questionName = f'{EditA}'
                questionAnswer = f'{colorama.Fore.RED}___'

                while questionAnswer == f'{colorama.Fore.RED}___':
                    os.system('cls')
                    print(f'''{colorama.Fore.LIGHTBLUE_EX}Úloha: {colorama.Fore.LIGHTGREEN_EX}{Name}.json\n\n\n
    {colorama.Fore.LIGHTBLUE_EX}Zadání otázky:{colorama.Fore.RESET} {questionName}
    {colorama.Fore.LIGHTBLUE_EX}Správná odpověď:{colorama.Fore.RESET} {questionAnswer}
    {colorama.Fore.RESET}''')

                    if questionAnswer == f'{colorama.Fore.RED}___':
                        questionAnswer = input(f'{colorama.Fore.LIGHTBLUE_EX}Správná odpověď:{colorama.Fore.RESET} ')
                        if questionAnswer != '' and len(questionAnswer.replace(' ','')) != 0:
                            continue
                        else:
                            questionAnswer = f'{colorama.Fore.RED}___'
                            continue

                os.system('cls')
                print(f'''{colorama.Fore.LIGHTBLUE_EX}Úloha: {colorama.Fore.LIGHTGREEN_EX}{Name}.json\n\n\n
    {colorama.Fore.LIGHTBLUE_EX}Zadání otázky:{colorama.Fore.RESET} {questionName}
    {colorama.Fore.LIGHTBLUE_EX}Správná odpověď:{colorama.Fore.RESET} {questionAnswer}
    {colorama.Fore.RESET}''')
                content['Doplň odpověď'].update({questionName : [questionAnswer]})
          
            case 'Smazat otázku':
                while True:
                    os.system('cls')
                    otazky = list(content['Doplň odpověď'].keys())
                    otazky.append('Odejít zpět do menu')
                    DeleteQ = [inquirer.List('DeleteQ', message='Kterou otázku chcete vymazat?', choices=otazky)]
                    DeleteA = inquirer.prompt(DeleteQ)['DeleteQ']
                    if DeleteA == 'Odejít zpět do menu':
                        break
                    else:
                        try:
                            content['Doplň odpověď'].pop(str(DeleteA))
                        except:
                            print(f'\n\n{colorama.Fore.RED}CHYBA: Otázka nenalezena\n{colorama.Fore.RESET}')
                            os.system('pause')

            case 'Uložit a odejít':
                with open(f"data/{Name}.json", 'w', encoding='UTF-8') as outfile:
                    json.dump(content, outfile, indent=4)
                    outfile.close()
                Menu()

#Unintencional start checker
if __name__ == "__main__":
    Menu()