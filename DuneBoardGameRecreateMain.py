import random
import time
import copy
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
    "Mentat"
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

sectors = {
    1 : ["place-1","place-2","place-3"],
    2 : ["place-4","place-5","place-6"],
    3 : ["place-7","place-8","place-9"],
    4 : ["place-10","place-11","place-12"],
    5 : ["place-13","place-14","place-15"],
    6 : ["place-16","place-17","place-18"],
    7 : ["place-19","place-20","place-21"],
    8 : ["place-22","place-23","place-24"],
    9 : ["place-25","place-26","place-27"],
    10 : ["place-28","place-29","place-30"],
    11 : ["place-31","place-32","place-33"],
    12 : ["place-34","place-35","place-36"],

}

untouch_sectors = copy.deepcopy(sectors)

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

card_names = []
available_trech_probabilities = []
def select_trechery():
    for c in treachery_deck:
        if treachery_deck[c] != 0:
            treachery_deck_probabilty[c] = 100 * (treachery_deck[c] / (total_trech_cards - treachery_deck[c]))
        
    card_names = list(treachery_deck.keys())
    card_probabilities = list(treachery_deck_probabilty.values())
    available_trech_probabilities = card_probabilities[:]
    
    selected_card_index = random.choices(range(len(card_names)), weights=available_trech_probabilities, k=1)[0]
    selected_card = card_names[selected_card_index]
    return selected_card

def give_treachery(deck):

    selected_card = select_trechery()

    if treachery_deck[selected_card] != 0:
        deck.append(selected_card)
        treachery_deck[selected_card] -= 1
    elif treachery_deck[selected_card] > 0:
        new_selected_card_index = random.choices(range(len(card_names)), weights=available_trech_probabilities, k=1)[0]
        selected_card = card_names[new_selected_card_index]
        print(f"Original card not available, selecting new card: {selected_card}")
        deck.append(selected_card)
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
            give_treachery(players[n].current_trech_c)
        print("Traitors...")
        while players[n].current_traitors_n < 4:
            give_traitor(n)
            
        print(f"{players[n].name} has : \n {len(players[n].current_trech_c)} treachery cards ({players[n].current_trech_c}) \n {players[n].current_traitors_n} traitor cards ({players[n].current_traitors_c}).")
    pick_traitor(n)

storm_cards = [1,2,3,4,5,6]
def draw_storm(current_turn,current_sector,deck,spice_locals,untouch_sectors):
    if current_turn == 1:
        #choosing the first storm starting location
        rand_sector = random.randrange(1,13)
        current_sector = rand_sector
        print(f"main set current sector {current_sector}")
    print("reading the wind...")
    
    if not deck :
        print("storm deck empty...reshufling...")
        deck = [1,2,3,4,5,6]
    
    selected_storm_card = random.choice(deck)
    deck.remove(selected_storm_card)
    
    new_sector = (current_sector + selected_storm_card ) % 12
    print(f"{current_sector} + {selected_storm_card} % 12 == {new_sector}")
    if new_sector == 0:
        new_sector = 12
    current_sector = new_sector

    print(f"Storm moves {selected_storm_card} sectors.")
    print(f"Storm is now at sector: {new_sector}")

    spice_locals_copy = spice_locals.copy()
    
    sect_storm_passed_through = []
    for n in range(selected_storm_card):
        storm_passed = (new_sector - n) % 12
        if storm_passed == 0:
            storm_passed = 12
        sect_storm_passed_through.append(storm_passed)
    print(sect_storm_passed_through)

    places_to_remove = []

    for s in range(len(spice_locals_copy)):
        if spice_locals_copy != []:
            print(spice_locals_copy[s])
            for x in range(len(sect_storm_passed_through)):
                if spice_locals_copy[s] in untouch_sectors[sect_storm_passed_through[x]]:
                    #print(sect_storm_passed_through[x])
                    print(f"should remove {spice_locals_copy[s]}")
                    places_to_remove.append(spice_locals_copy[s])
    
    for places in places_to_remove:
        spice_locals_copy.remove(places)
    return current_sector


spiced_locations = []
available_sectors = []
max_spice_blows = 2
card_name = dict(sectors)
chosen_sector = 0
#print(card_name.keys())
def draw_spice_blow(storm_sector):
    print("feeling the rumble...")
    for blows in range(max_spice_blows):
        available_sectors = list(sectors.keys())
        chosen_sector = random.choice(available_sectors)
        #print(chosen_sector)
        available_places = sectors[chosen_sector]
        while available_places == []:
            #print(f"{chosen_sector} is empty or storm blocked...choosing new location")
            chosen_sector = random.choice(available_sectors)
            available_places = sectors[chosen_sector]
        chosen_place = random.choice(available_places)

        #print(f"first selected location {chosen_place}")
        if chosen_place in spiced_locations or chosen_sector == storm_sector:
            chosen_place = random.choice(available_places)
            print(f"seccond selected location {chosen_place}")
        else:
            spiced_locations.append(chosen_place)
            available_places.remove(chosen_place)
            print(chosen_place)
    print(f"There is spice at {spiced_locations}.")

def choam_charity():
    print("Choam Charity...")
    for n in range(0,len(players)):
        if players[n].current_spice < 2:
            print(f"{players[n].name} says Choam Charity!")
            players[n].current_spice = 2

def get_highest_bidder(bid_list):
    highest_bid = 0
    highest_bidder = None
    for player_name, bid_value in bid_list.items():
        if bid_value > highest_bid:
            highest_bidder = player_name
            highest_bid = bid_value
    return highest_bidder

up_for_auction = []
able_to_bid = []

def can_you_bid():
    for n in range(0, len(players)):
        if len(players[n].current_trech_c) == players[n].max_trech:
            print(f"{players[n].name} already has the maximum number of treachery cards and cannot bid.")
            #able_to_bid.remove(players[n].name)
        else:
            able_to_bid.append(players[n].name)
       
def bidding():
    bids = {}  # Dictionary to store bids with player names
    print('Bidding...')
    up_for_auction.clear()
    actual_bid = 0
    winning_bidder = None
    passed_on_card = False
    
    can_you_bid()    
    print(able_to_bid)
    give_treachery(up_for_auction)
    for x in range(0, len(able_to_bid)):  
        print(up_for_auction)
        can_you_bid()
        current_bid = int(input(f"{able_to_bid[x]}(spice: {players[x].current_spice}) enter a bid "))
        while current_bid > players[x].current_spice and current_bid != 0:
            current_bid = int(input(f"{able_to_bid[x]}(spice: {players[x].current_spice}) enter a bid less than your current spice ({players[x].current_spice}) "))
        if current_bid > actual_bid and current_bid <= players[x].current_spice:
            actual_bid = current_bid
            winning_bidder = able_to_bid[x]
            winning_bidder_index = able_to_bid.index(winning_bidder)

    if winning_bidder:
        print(f"The Auction has {len(up_for_auction)} cards to bid for")
        # print(actual_bid)
        print(f"{winning_bidder} has won the bid.")
        players[winning_bidder_index].current_trech_c.append(up_for_auction[len(up_for_auction) - 1])
        players[winning_bidder_index].current_spice -= actual_bid
        print(players[winning_bidder_index].current_trech_c)
    else:
        print("No bidders today")
    able_to_bid.clear()


game_end = False
def mentat_pause():
    if game_end == True:
        exit()
current_sector = random.randrange(1, 12)
def main(current_phase,current_sector):
    current_turn = 1
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
    
    while current_turn != 11:
        print(f"TURN {current_turn}")
            #time.sleep(2)
        if current_phase == "Storm":
             # Update current_sector with the returned value
            current_sector = draw_storm(current_turn, current_sector, storm_cards, spiced_locations, untouch_sectors)
            current_phase = phase[2]
            #time.sleep(2)
        if current_phase == "Spice Blow":
            draw_spice_blow(current_sector)
            current_phase = phase[3]
            #time.sleep(2)
        if current_phase == "Choam Charity":
            #choam_charity()
            current_phase = phase[4]
            #time.sleep(2)
        if current_phase == "Bidding":
           # bidding()
            current_phase = phase[5]
            #time.sleep(2)
        if current_phase == "Revival":
            #print("Revival...")
            current_phase = phase[6]
            #time.sleep(2)
        if current_phase == "Ship and Move":
            #print("Ship and Move...")
            current_phase = phase[7]
            #time.sleep(2)
        if current_phase == "Battle":
            #print("Battle...")
            current_phase = phase[8]
            #time.sleep(2)
        if current_phase == "Spice Harvest":
            #print("Spice Harvest...")
            current_phase = phase[9]
            #time.sleep(2)
        if current_phase == "Mentat":
            #mentat_pause()
            current_phase = phase[1]
            #time.sleep(1)
        current_turn += 1

main(current_phase,current_sector)