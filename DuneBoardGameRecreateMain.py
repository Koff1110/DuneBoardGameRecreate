import random
#random.seed("Test2") #Seed Test 2 give Emp a karma, Hark a karma, and Bene a karma because Ghola is not available which it should not
#also Harc and Bene have Lady Margot when only harc should have
decks = {"spice_deck" : 21, "treachery_deck" : 33, "traitor_deck" : 30, "storm_deck" : 6}

phase =[
    "Start",
    "Storm",
    "Spice Blow",
    "Choam Charity",
    "Bidding",
    "Revival",
    "Ship and Move",
    "Battle",
    "Spice Harvest",
    "Mentant"
 ]
current_phase = phase[0]

spice_deck ={
    "place-1" : 2,
    "place-2" : 2,
    "place-3" : 2,
    "place-4" : 1,
    "place-5" : 1,
    "place-6" : 2,
    "place-7" : 4,
    "place-8" : 4,
    "place-9" : 6,
    "place-10" : 8,
}

spiced_locations = []

traitor_deck_reg = {
    "Atraides" : {
        "Dr.Yueh" : 1,
        "Duncan Idaho" : 2,
        "Gurney Halleck" : 4,
        "Lady Jessica" : 5,
        "Thufir Hawat" : 5
    },
    "Harkonen" : {
        "Feyd Rautha" :6,
        "Beast Rabban" : 4,
        "Piter DeVries" : 3,
        "Umman Kudu" : 2,
        "Nefud" : 1
    },
    "Fremen" : {
        "Stilgar" : 7,
        "Chani" : 6,
        "Otheym" : 5,
        "Shadout Mapes" : 3,
        "Jamis" : 2
    },
    "Emperor" : {
        "Count Fenring" : 6,
        "Capt Aramsham" : 5,
        "Burseg" : 3,
        "Caid" : 3,
        "Bashar" : 2
    },
    "Bene Gesserit" : {
        "Alia" : 5,
        "Lady Margot Fenring" : 5,
        "Princess Irulan" : 5,
        "Wanna Yueh" : 5,
        "Reverend Mother Ramllo" : 5
    },
    "Spacing Guild" : {
        "Stabban Tuek" : 5,
        "Esmar Tuek" : 3,
        "Master Bewt" : 3,
        "Soo Soo Suk" : 2,
        "Guild Representative" : 1
    }
}
traitor_deck_ureg = {
    "Dr.Yueh": 1,
    "Duncan Idaho": 2,
    "Gurney Halleck": 4,
    "Lady Jessica": 5,
    "Thufir Hawat": 5,
    "Feyd Rautha": 6,
    "Beast Rabban": 4,
    "Piter DeVries": 3,
    "Umman Kudu": 2,
    "Nefud": 1,
    "Stilgar": 7,
    "Chani": 6,
    "Otheym": 5,
    "Shadout Mapes": 3,
    "Jamis": 2,
    "Count Fenring": 6,
    "Capt Aramsham": 5,
    "Burseg": 3,
    "Caid": 3,
    "Bashar": 2,
    "Alia": 5,
    "Lady Margot Fenring": 5,
    "Princess Irulan": 5,
    "Wanna Yueh": 5,
    "Reverend Mother Ramllo": 5,
    "Stabban Tuek": 5,
    "Esmar Tuek": 3,
    "Master Bewt": 3,
    "Soo Soo Suk": 2,
    "Guild Representative": 1,
    "Cozmo" : 10
}

treachery_deck = {
    "Worthless Card" : 5,
    "Poision weapon" : 4,
    "Projectile weapon" : 4,
    "lasgun" : 1,
    "Shield" : 4,
    "Snooper" : 4,
    "Karma" : 2,
    "Hajar" : 1,
    "Weather Controll" : 1,
    "Ghola" : 1,
    "Cheap Hero" : 3,
    "Family Atomics" : 1,
    "Truthtrance" : 2
    }
total_trech_cards = sum(treachery_deck.values())
treachery_deck_probabilty = {
    "Worthless Card" : 5,
    "Poision weapon" : 4,
    "Projectile weapon" : 4,
    "lasgun" : 1,
    "Shield" : 4,
    "Snooper" : 4,
    "Karma" : 2,
    "Hajar" : 1,
    "Weather Controll" : 1,
    "Ghola" : 1,
    "Cheap Hero" : 3,
    "Family Atomics" : 1,
    "Truthtrance" : 2
}


def give_traitor(n):
    card_names = list(traitor_deck_ureg.keys())
    available_traitors = card_names[:]
   
    if available_traitors:
         selected_card = random.choice(available_traitors)
         for p in range(len(players)):
            if selected_card in traitor_deck_reg[players[p].name]: #Makes sure selected traitor is in the game
                players[n].current_traitors_c.append(selected_card)
         available_traitors.remove(selected_card)
         del traitor_deck_ureg[selected_card]  # Remove the selected card from the deck
         players[n].current_traitors_n = len(players[n].current_traitors_c)
    else:
        print("No traitor cards available.")
        exit()
        

def pick_traitor(n):
    print("Pick Traitor")
    for n in range(0,len(players)):
        picked_traitor = input(f"{players[n].name} Pick a traitor to keep: ")
        while picked_traitor not in players[n].current_traitors_c:
            picked_traitor = input("Please enter a valid Traitor: ")
        while picked_traitor in list(traitor_deck_reg[players[n].name]):
            picked_traitor = input("Please enter a valid Traitor not in your own faction: ")
        players[n].current_traitors_c = picked_traitor
    print(f"{players[n].name} Traitor is: {players[n].current_traitors_c}")

def give_treachery(n):
    for c in treachery_deck:
        if treachery_deck[c] != 0:
            treachery_deck_probabilty[c] = 100 * (treachery_deck[c] / (total_trech_cards - treachery_deck[c]))
        
    card_names = list(treachery_deck.keys())
    card_probabilities = list(treachery_deck_probabilty.values())
    available_trech_probabilities = card_probabilities[:]
    
    selected_card_index = random.choices(range(len(card_names)), weights=available_trech_probabilities, k=1)[0]
    selected_card = card_names[selected_card_index]
    
    if treachery_deck[selected_card] != 0:
        players[n].current_trech_c.append(selected_card)
        treachery_deck[selected_card] -= 1
    elif treachery_deck[selected_card] > 0:
        new_selected_card_index = random.choices(range(len(card_names)), weights=available_trech_probabilities, k=1)[0]
        selected_card = card_names[new_selected_card_index]
        print(f"Original card not available, selecting new card: {selected_card}")
        players[n].current_trech_c.append(selected_card)
        treachery_deck[selected_card] -= 1




class Faction:
    def __init__(self, name, starting_spice, reserve,max_trech,current_traitors_n,current_trech_c,current_traitors_c,max_traitors):
        self.name = name
        self.reserve = reserve
        self.start_spice = starting_spice
        self.current_spice = starting_spice
        self.max_trech = max_trech
        self.current_trech_c = []
        self.current_traitors_n = current_traitors_n
        self.max_traitors = max_traitors
        self.current_traitors_c = []
       

factlist = [
    Faction("Atraides", starting_spice=10, reserve=10,
            max_trech = 4, current_trech_c = "",
            max_traitors = 1, current_traitors_n = 0, current_traitors_c = ""),
    
    Faction("Harkonen", starting_spice=10, reserve=10,
            max_trech = 8, current_trech_c = "",
            max_traitors = 4, current_traitors_n = 0, current_traitors_c = ""),
    
    Faction("Fremen", starting_spice=3, reserve=10,
            max_trech = 4, current_trech_c = "",
            max_traitors = 1, current_traitors_n = 0, current_traitors_c = ""),
    
    Faction("Emperor", starting_spice=10, reserve=20,
            max_trech = 4, current_trech_c = "",
            max_traitors = 1, current_traitors_n = 0, current_traitors_c = ""),
    
    Faction("Bene Gesserit", starting_spice=5, reserve=10,
            max_trech = 4, current_trech_c = "",
            max_traitors = 1, current_traitors_n = 0, current_traitors_c = ""),
    
    Faction("Spacing Guild", starting_spice=5, reserve=15,
            max_trech = 4, current_trech_c = "",
            max_traitors = 1, current_traitors_n = 0, current_traitors_c = "")
]


players = [] #stores players and their faction?

def assign_factions(p):
    available_factions = factlist[:]
    count = 0
    while count < p and available_factions:
        ran = random.randrange(0, len(available_factions)) #picks a faction from list
        faction = available_factions[ran]
        print(f"Player {count + 1}: {faction.name}")
        print(f"{faction.name} has {faction.start_spice} spice and {faction.reserve} units in reserve.")
        players.append(faction)
        del available_factions[ran]
        count += 1

def distribute_cards():
    print("Distributing cards...")
    print("Trechery...")
    for n in range(0,len(players)):
        while len(players[n].current_trech_c) < 1:#players[n].max_trech:
            give_treachery(n)
        print("Traitors...")
        while players[n].current_traitors_n < 4:
            give_traitor(n)
            
        print(f"{players[n].name} has : \n {len(players[n].current_trech_c)} treachery cards ({players[n].current_trech_c}) \n {players[n].current_traitors_n} traitor cards ({players[n].current_traitors_c}).")
    pick_traitor(n)

def draw_storm():
    print("reading the wind...")
    storm_card = random.randrange(0,6)
    print(f"Storm moves {storm_card} sectors.")

def draw_spice_blow():
    print("feeling the rumble...")
    card_name = dict(spice_deck)
    available_locations = list(card_name.keys())
    selected_blow = random.choice(available_locations)
    spiced_locations.append(selected_blow)
    print(f"Spice blow at {selected_blow} with {spice_deck[selected_blow]} spice.")
    print(f"there is spice at :")
    for l in range(len(spiced_locations)):
        print(f"{spiced_locations[l]} : {spice_deck[spiced_locations[l]]} spice.")

def bidding():
    print("bidding...")

def main(current_phase):
    if current_phase == "Start":
        start_game = input("Start Game? y/n: ")
        if start_game == "y":
            player_count = int(input("How many players: "))
            assign_factions(player_count)
            distribute_cards()
        elif start_game == "n":
            quit()
        else:
            start_game = input("Start Game? y/n: ")
        current_phase = phase[1]
    if current_phase == "Storm":
        draw_storm()
        current_phase = phase[2]
    if current_phase == "Spice Blow":
        draw_spice_blow()

main(current_phase)