from random import sample, shuffle

WORD_LIST = ["above", "aim", "air", "airplane", "Aladdin", "Albert Einstein", "Alice in Wonderland", "alien", "alive",
             "alright", "America", "angle", "angry", "ankle", "apple", "around", "astronaut", "ATM", "attractive",
             "Australia", "autumn", "Back to the Future", "backbone", "baggage", "Bambi", "banister", "bank",
             "bar code", "barber", "Barbie", "baseball", "baseboards", "bathroom", "Batman", "batteries", "battery",
             "bean", "Beauty and the Beast", "bed", "bedroom", "beer", "bicycle", "big", "biscuit", "blinds", "blue",
             "blue jeans", "bomb", "book", "boots", "bored", "bowtie", "box", "boy", "branch", "break ", "broom",
             "bullet", "bumper", "butterfly", "button", "cake", "calendar", "camera", "candle", "candy", "cane",
             "Captain Hook", "car", "carrot", "case", "cash", "catalog", "caught", "ceiling fan", "cell phone",
             "cell phone charger", "center", "Charlie Brown", "chase", "chicken", "chimney", "choclate", "chocolate",
             "church", "Cinderella", "circus", "clog", "coal", "coat", "colds", "coma", "comfy", "commercial",
             "computer", "constellation", "contact", "corn", "cowboy", "crayons", "crib", "crisp", "crowd", "crutch",
             "cry", "cup", "curtains", "darkness", "Darth Vader", "dashboard", "dead", "deep", "deoderant", "desert",
             "desk", "diagonal", "diamond", "different", "digital", "dinner", "directions", "disc", "disheveled",
             "dizzy", "docter", "dog", "dominoes", "door", "door knob", "doorway", "dot", "download", "dress shirt",
             "dripping", "drought", "drug", "Dumbo", "dustpan", "east", "electrical outlet", "electricity", "end",
             "eraser", "exercise", "extra", "eyes", "fabric", "face", "far", "father", "fear", "feel", "Finding Nemo",
             "fire", "fireside", "fireworks", "flower", "flowers", "food", "food rations", "Forest Gump", "fracture",
             "France", "fresh", "friend", "frog", "front porch", "frost", "fruit", "fuel", "garage door", "garbage",
             "hose", "gas", "gingerbread", "girl", "glitter", "goggles", "gold", "golf", "goodbye", "grass", "green",
             "grow", "gun", "guy", "hail", "hair dryer", "hairspray", "half", "hand lotion", "hand soap", "happy",
             "Harry Potter", "hat", "headband", "hear", "hello", "help", "high", "hockey", "hole", "holidays", "hop",
             "horse", "hot", "hot dog", "hot water", "husband", "icon", "Indiana Jones", "inside", "iron",
             "ironing board", "Isaac Newton", "jacket", "jail", "James Bond", "Japan", "jazz", "jeans", "jewelry",
             "jump", "jungle", "junk", "key", "kitchen", "kitchen ", "knife", "ladder", "lady", "laser", "lasses",
             "laundry", "lawnmower", "leader", "leaf", "leash", "left", "leopard", "lick", "lie", "life", "light bulb",
             "light switch", "lightsaber", "Lincoln", "living room", "lobster", "logo", "long", "lotion", "love",
             "Luke Skywalker", "lunch", "lunchbox", "macaroni", "magazine", "magnets", "mailbox", "mailman", "makeup",
             "mall", "man", "markers", "Mary Poppins", "mattress", "mig", "military", "mime", "mirror", "moon",
             "mother", "movie", "music", "myth", "nature", "necktie", "neighborhood", "nervous", "newsletter",
             "newspaper", "nine", "noose", "note", "notebook", "number", "October", "off", "on", "online", "orange",
             "outside", "page", "paint", "palace", "panda", "pants", "paperclip", "park", "password", "peasant",
             "peeping", "pen", "perfume", "period", "Peter Pan", "pharmacist", "photograph", "piano", "picture",
             "picture frame", "pillow", "pinwheel", "pirate", "pizza sauce", "plant", "slam dunk", "poison", "power",
             "praise", "pregnant", "presents", "president", "press", "Princess Leia", "printer paper", "probably",
             "professor", "pumpkin", "purse", "pushups", "quarterback", "queen", "quilt", "raking", "rate", "record",
             "red wagon", "retail", "rewind", "right", "ring", "rock", "rocking chair", "roller blading", "round",
             "rubber", "ruler", "run", "sad", "salt and pepper", "scale", "scarecrow", "scared", "scarf", "scarves",
             "school", "scissors", "Scooby Doo", "scream", "screen ", "September", "shallow", "shampoo", "shirt",
             "shoes", "short", "shower curtain", "Shrek", "sick", "silverware", "sink", "situps", "sixties", "skate",
             "skateboard", "ski", "skip", "skirt", "Sleeping Beauty", "slips", "small", "smart", "smile", "soap",
             "soccer", "socks", "soda", "sofa", "sometime", "song", "sound", "soup", "spare", "speaker", "speakers",
             "spice rack", "Spiderman", "sponge", "spooky", "spray", "spring", "stairs", "stamps", "stapler",
             "Star Wars", "start", "state", "stationery", "stem", "stick", "sticker", "stone", "stool", "strap",
             "submit", "sun", "Sunday", "sung", "Superman", "swallow", "sweater", "sweet", "swing", "t-shirt", "tablet",
             "taco", "teapot", "television", "tender", "tennis shoes", "Texas", "The Beatles", "The Grinch",
             "the internet", "The Lion King", "The Little Mermaid", "The Muppets", "The Wizard of Oz", "thief", "think",
             "third floor", "thought", "tied up", "time", "tissue", "toast", "toilet paper", "tongue", "tonight",
             "toothbrush", "top shelf", "towel", "town", "Toy Story", "trash can", "treasure", "trees", "trip",
             "tropical", "tweet", "ugly", "umbrella", "underneath", "unit", "usually", "vegetarian", "vegtable", "vest",
             "video camera", "Waldo", "walk", "walker", "wallet", "walrus", "warning", "washing machine", "waste",
             "water", "watering can", "wax", "webcam", "website", "wheel", "whisk", "whistle", "Willy Wonka", "wind",
             "wing", "Winnie the Pooh", "witch", "wobble", "woman", "world", "worship", "worst", "wrapper", "wrinkle",
             "yellow", "yesterday", "yolk", "you"]


def words(n):
    if n > 1:
        w = sample(WORD_LIST, n - 1)
        w.append('_______')
        shuffle(w)
        return w
    else:
        return ['_______']