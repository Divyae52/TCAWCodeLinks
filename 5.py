# THE COMPUTER ALWAYS WINS
# MIT PRESSS
#
# CodeLink 5
# Breadth First Word Ladders
# last revised 12/25/24
#
# This is a working implementation of our breadth-first Word Ladder
# code from Chapter Three. Feel free to add print statements so that
# you can see how the algorithm builds ladders in a particular order.

# WORD BANK

words = ["able", "acid", "acre", "aged", "aide", "akin", "alas", "ally", "also", "alto", "amid", "anal", "anna", "anti",
         "apex", "arch", "area", "army", "atom", "atop", "aunt", "aura", "auto", "avid", "away", "axis", "baby", "bach",
         "back", "bail", "bait", "bake", "bald", "ball", "band", "bang", "bank", "bare", "bark", "barn", "base", "bass",
         "bath", "bats", "beam", "bean", "bear", "beat", "beck", "beef", "been", "beer", "bell", "belt", "bend", "bent",
         "best", "beta", "beth", "bias", "bike", "bill", "bind", "bird", "bite", "blew", "bloc", "blog", "blow", "blue",
         "blur", "boat", "body", "boil", "bold", "bolt", "bomb", "bond", "bone", "book", "boom", "boon", "boot", "bore",
         "born", "boss", "both", "bout", "bowl", "brad", "bred", "brew", "brow", "buck", "bulb", "bulk", "bull", "bump",
         "burn", "bury", "bush", "bust", "busy", "butt", "buzz", "cafe", "cage", "cake", "calf", "call", "calm", "came",
         "camp", "cane", "cape", "card", "care", "carl", "carr", "cart", "case", "cash", "cast", "cave", "cell", "cent",
         "chad", "chap", "chat", "chef", "chic", "chin", "chip", "chop", "cite", "city", "clad", "clan", "clay", "clip",
         "club", "clue", "coal", "coat", "coca", "code", "coil", "coin", "coke", "cola", "cold", "cole", "come", "cone",
         "conn", "cook", "cool", "cope", "copy", "cord", "core", "cork", "corn", "cost", "coup", "cove", "crap", "crew",
         "crop", "crow", "cube", "cult", "curb", "cure", "cute", "dale", "dame", "damn", "damp", "dare", "dark", "dash",
         "data", "date", "dawn", "days", "dead", "deaf", "deal", "dean", "dear", "debt", "deck", "deed", "deep", "deer",
         "dell", "demo", "dent", "deny", "desk", "dial", "dice", "dick", "diet", "dire", "dirt", "disc", "dish", "disk",
         "dive", "dock", "does", "dole", "doll", "dome", "done", "doom", "door", "dose", "dove", "down", "drag", "draw",
         "drew", "drop", "drug", "drum", "dual", "duck", "duff", "duke", "dull", "duly", "dumb", "dump", "dusk", "dust",
         "duty", "each", "earl", "earn", "ease", "east", "easy", "eats", "echo", "edge", "edit", "else", "envy", "epic",
         "euro", "even", "ever", "evil", "exam", "exit", "expo", "eyed", "face", "fact", "fade", "fail", "fair", "fake",
         "fall", "fame", "fare", "farm", "fast", "fate", "fear", "feat", "feed", "feel", "feet", "fell", "felt", "file",
         "fill", "film", "find", "fine", "fire", "firm", "fish", "fist", "five", "flag", "flat", "fled", "flee", "flew",
         "flex", "flip", "flow", "flux", "foam", "foil", "fold", "folk", "fond", "font", "food", "fool", "foot", "ford",
         "fore", "fork", "form", "fort", "foul", "four", "free", "frog", "from", "fuck", "fuel", "full", "fund", "fury",
         "fuse", "fuss", "gain", "gala", "gale", "gall", "game", "gang", "gate", "gave", "gaze", "gear", "gene", "gift",
         "gill", "girl", "give", "glad", "glen", "glow", "glue", "goal", "goat", "goes", "gold", "golf", "gone", "good",
         "gore", "gown", "grab", "gram", "gray", "grew", "grey", "grid", "grim", "grin", "grip", "grow", "gulf", "guru",
         "hail", "hair", "hale", "half", "hall", "halt", "hand", "hang", "hank", "hard", "harm", "hart", "hate", "haul",
         "have", "hawk", "head", "heal", "heap", "hear", "heat", "heel", "heir", "held", "hell", "helm", "help", "herb",
         "herd", "here", "hero", "hers", "hide", "high", "hike", "hill", "hint", "hire", "hold", "hole", "holt", "holy",
         "home", "hood", "hook", "hope", "horn", "hose", "host", "hour", "huge", "hull", "hung", "hunt", "hurt", "hype",
         "icon", "idea", "idle", "idol", "inch", "info", "into", "iris", "iron", "isle", "item", "jack", "jail", "jake",
         "jane", "java", "jazz", "jean", "jeep", "jill", "joey", "john", "join", "joke", "josh", "jump", "junk", "jury",
         "just", "keen", "keep", "kemp", "kent", "kept", "khan", "kick", "kill", "kind", "king", "kirk", "kiss", "kite",
         "knee", "knew", "knit", "knot", "know", "kohl", "Kyle", "lace", "lack", "lady", "laid", "lake", "lamb", "lamp",
         "land", "lane", "lang", "last", "late", "lava", "lawn", "lazy", "lead", "leaf", "leak", "lean", "leap", "left",
         "lend", "lens", "lent", "less", "lest", "levy", "lied", "lien", "life", "lift", "like", "lily", "limb", "lime",
         "limp", "line", "link", "lion", "list", "live", "load", "loan", "lock", "loft", "logo", "lone", "long", "look",
         "loop", "lord", "lose", "loss", "lost", "loud", "love", "luck", "lump", "lung", "lure", "lush", "lust", "made",
         "maid", "mail", "main", "make", "male", "mall", "mama", "many", "marc", "mark", "mart", "mask", "mass", "mate",
         "matt", "mayo", "maze", "mead", "meal", "mean", "meat", "meet", "Mega", "melt", "memo", "menu", "mere", "mesa",
         "mesh", "mess", "mice", "mick", "mike", "mild", "mile", "milk", "mill", "mind", "mine", "mini", "mint", "miss",
         "mist", "mock", "mode", "mold", "monk", "mood", "moon", "more", "moss", "most", "move", "much", "must", "myth",
         "nail", "name", "navy", "near", "neat", "neck", "need", "nest", "news", "next", "nice", "nick", "nine", "node",
         "none", "noon", "norm", "nose", "note", "nova", "nude", "nuts", "oath", "obey", "odds", "odor", "okay", "once",
         "only", "onto", "open", "oral", "otto", "ours", "oval", "oven", "over", "pace", "pack", "pact", "page", "paid",
         "pain", "pair", "pale", "palm", "papa", "para", "park", "part", "pass", "past", "path", "peak", "peat", "peck",
         "peel", "peer", "pest", "pick", "pier", "pike", "pile", "pill", "pine", "pink", "pint", "pipe", "pity", "plan",
         "play", "plea", "plot", "plug", "plus", "poem", "poet", "pole", "poll", "polo", "poly", "pond", "pony", "pool",
         "poor", "pope", "pork", "port", "pose", "post", "pour", "pray", "prep", "prey", "prof", "prop", "pull", "pulp",
         "pump", "punk", "pure", "push", "quid", "quit", "quiz", "race", "rack", "rage", "raid", "rail", "rain", "ramp",
         "rang", "rank", "rape", "rare", "rash", "rate", "rave", "read", "real", "reap", "rear", "reed", "reef", "reel",
         "rely", "rent", "rest", "rice", "rich", "rick", "ride", "ring", "riot", "ripe", "rise", "risk", "rite", "ritz",
         "road", "roar", "rock", "rode", "role", "roll", "roof", "room", "root", "rope", "rose", "ruby", "rude", "ruin",
         "rule", "rush", "rust", "ruth", "sack", "safe", "saga", "sage", "said", "sail", "sake", "sale", "salt", "same",
         "sand", "sang", "sank", "save", "scan", "scar", "scot", "seal", "seat", "seed", "seek", "seem", "seen", "self",
         "sell", "semi", "send", "sent", "sept", "sexy", "shah", "shed", "ship", "shit", "shoe", "shop", "shot", "show",
         "shut", "sick", "side", "sigh", "sign", "silk", "sing", "sink", "site", "size", "skin", "skip", "slab", "slam",
         "slap", "slid", "slim", "slip", "slot", "slow", "snap", "snow", "soap", "soar", "soda", "sofa", "soft", "soil",
         "sold", "sole", "solo", "some", "song", "soon", "sore", "sort", "soul", "soup", "sour", "span", "spin", "spit",
         "spot", "spun", "spur", "star", "stay", "stem", "step", "stir", "stop", "such", "suck", "suit", "sung", "sunk",
         "sure", "surf", "swan", "swap", "sway", "swim", "tack", "tail", "take", "tale", "talk", "tall", "tank", "tape",
         "taps", "task", "taxi", "team", "tear", "tech", "teen", "tell", "tend", "tent", "term", "test", "text", "than",
         "that", "them", "then", "they", "thin", "this", "thou", "thus", "tick", "tide", "tidy", "tier", "tile", "till",
         "tilt", "time", "tiny", "tire", "toby", "told", "toll", "tomb", "tone", "tony", "took", "tool", "tops", "tore",
         "torn", "tort", "toss", "tour", "town", "trap", "tray", "tree", "trek", "trim", "trio", "trip", "troy", "true",
         "tube", "tuck", "tuna", "tune", "turf", "turn", "twin", "type", "ugly", "unit", "upon", "urge", "used", "user",
         "vain", "vary", "vast", "veil", "vein", "verb", "very", "vest", "veto", "vice", "view", "vine", "visa", "void",
         "vote", "wade", "wage", "wait", "wake", "walk", "wall", "want", "ward", "ware", "warm", "warn", "wary", "wash",
         "watt", "wave", "ways", "weak", "wear", "weed", "week", "well", "went", "were", "west", "what", "when", "whip",
         "whom", "wide", "wife", "wild", "will", "wind", "wine", "wing", "wipe", "wire", "wise", "wish", "with", "woke",
         "wolf", "wood", "wool", "word", "wore", "work", "worm", "worn", "wrap", "yang", "yard", "yarn", "yeah", "year",
         "your", "yuan", "zero", "zinc", "zone", "zoom"]


# FUNCTION DEFINITIONS
# ####################

def notLegal(word):
    # can the computer use this word?
    for ctr in range(len(words)):
        if word == words[ctr]:
            return False
    return True

def number(word):
    # convert from the word itself to its number in our list
    for ctr in range(len(words)):
        if word == words[ctr]:
            return ctr
        
def copyList(list):
    # duplicate the list
    newList = []
    for item in list:
        newList.append(item)
    return newList

def isPossible(fromWord, toWord):
    # 'fromWord' is the current word
    # 'toWord' is the proposed next word
    # return True if these words connect legally
    
    changes = 0

    for ctr in range(4):
        if fromWord[ctr] != toWord[ctr]:
            changes += 1
    if changes == 1:
        return True
    else:
        return False

def printList(list):
    for item in list:
        print(item)

def printArray(array):
    for list in array:
        printList(list)
        print("")
    temp = input("Next?")
    print ("")

def breadthFirst(startWord, endWord):

    # this array stores all ladders currently under consideration
    ladders = [[startWord]]

    # helpful debug code
    oldLadderLength = 1

    while (len(ladders)>0):
        # loop until we run out of ladders
        
        # we will start by expanding the very first ladder
        ladderToExpand = ladders[0]
        currentLastWord = ladderToExpand[len(ladderToExpand)-1]
            
        for potentialNextWord in words:
            
            # no repetition allowed
            if potentialNextWord not in ladderToExpand:

                # check if it's a legal step
                if isPossible(currentLastWord, potentialNextWord):

                    # make and store the new, longer ladder
                    newLadder = copyList(ladderToExpand)
                    newLadder.append(potentialNextWord)
                    ladders.append(newLadder)

                    if potentialNextWord == endWord:
                        print("I found the shortest ladder.")
                        print("It is of length %d." % len(newLadder))
                        print()
                        printList(newLadder)
                        return
                    
        # remove the ladder we just expanded
        ladders.remove(ladderToExpand)

        # report status to the user
        if len(ladders[0])>oldLadderLength:
            oldLadderLength = len(ladders[0])
            print("I have generated every possible ladder of length %d." % oldLadderLength)
            print("There are %d such ladders." % (len(ladders)))
            print("")


# THE MAIN PROGRAM
# ################

beginWord = "bold"
endWord = "step"

while notLegal(beginWord):
    beginWord = input("What word should I start with? ")

while notLegal(endWord):
    endWord = input("What word should I end with? ")

print()
print("I will now find the shortest ladder connecting %s to %s." % (beginWord, endWord))
print()

breadthFirst(beginWord, endWord)

            

