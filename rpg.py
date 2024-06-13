mob_list = []

player = {
    "nome": "Carlinhos",
    "nivel": 1,
    "exp": 0,
    "exp_max": 50,
    "HP": 100,
    "HP_max": 100,
    "dano": 20,
}

def create_mob(nivel):
    
    newmob = {
        "Nome":f"Monstro {nivel}",
        "Nivel": nivel,
        "Dano": 5 * nivel,
        "HP": 100 * nivel,
        "HP_max": 100 * nivel,
        "EXP": 7 * nivel,
    }
    return newmob

def number_mob(n_mob):
    for x in range(n_mob):
        new_char = create_mob(x + 1)
        mob_list.append(new_char)

def show_moblist():
    for mobs in mob_list:
        show_mob(mobs)

def show_mob(mobs):
     print(
         f"nome: {mobs['Nome']}//Nivel: {mobs['Nivel']}//dano: {mobs['Dano']}//HP:{mobs['HP']}//HP_max:{mobs['HP_max']}//EXP: {mobs['EXP']}"
              )

def show_player():
    print(
         f"Nome: {player['nome']}//Nivel: {player['nivel']}//dano: {player['dano']}//HP:{player['HP']}/{player['HP_max']}//EXP: {player['exp']}/{player['exp_max']}"
              )
        
def start_battle(mobs):
    while player["HP"] > 0 and mobs["HP"] > 0:
        attack_mob(mobs)
        attack_player(mobs)
        show_info_battle(mobs)

    if player['HP'] > 0:
        print(f"{player['nome']} venceu e ganhou {mobs['EXP']} de EXP")
        print("--------------------------------------------")
        player['exp'] += mobs['EXP']
        show_player()
    else:
        print(f"O {mobs['Nome']} abateu o {player['nome']}")

    level_up()
    reset_player()
    reset_mob(mobs)

def level_up():
    if player['exp'] >= player['exp_max']:
        player['nivel'] += 1
        player['exp'] = 0
        player['exp_max'] *= 2
        player['HP_max'] += 20
        player['dano'] += 5

def attack_mob(mobs):
    mobs["HP"] -= player["dano"]


def attack_player(mobs):
    player["HP"] -= mobs["Dano"]


def show_info_battle(mobs):
    print("-----------------------------------------------------------------")
    print(f"PLAYER: {player['nome']} // {player['HP']} // {player['HP_max']}")
    print(f"NPC: {mobs['Nome']} // {mobs['HP']} // {mobs['HP_max']}")
    print("------------------------------------------------------------------")

def reset_player():
    player['HP'] = player['HP_max']

def reset_mob(mobs):
    mobs['HP'] = mobs['HP_max']

number_mob(1)
show_moblist()

mob_selecionado = mob_list[0]

for x in range(8):
    start_battle(mob_selecionado)


print()
print("------------LEVEL--UP-------------------")
show_player()












    
