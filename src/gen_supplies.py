# Builds data/supplies.txt — household supplies, one per line:
#   name|category|unit|tags
# tags: "in" marks things that are staples of an Indian household.
import pathlib, itertools, re

rows = []
def add(name, cat, unit='each', tags=''):
    rows.append((name.strip(), cat, unit, tags))

def spread(cat, items, variants, unit='each', tags=''):
    """items × variants, skipping the empty variant marker '-'."""
    for it in items:
        for v in variants:
            add(it if v == '-' else f'{it}, {v}', cat, unit, tags)

# ── Cleaning ────────────────────────────────────────────────────────────
C = 'Cleaning'
spread(C, [
 'All-purpose cleaner','Floor cleaner (phenyl)','Disinfectant floor cleaner','Glass cleaner',
 'Bathroom cleaner','Toilet bowl cleaner','Tile and grout cleaner','Kitchen degreaser',
 'Stainless steel polish','Wood polish','Furniture polish','Marble cleaner','Carpet shampoo',
 'Upholstery cleaner','Oven cleaner','Drain cleaner','Lime scale remover','Rust remover',
 'Mould and mildew remover','Bleach','Hydrogen peroxide cleaner','White vinegar cleaner',
 'Dish soap','Dishwasher gel','Hand wash refill','Multi-surface spray','Air freshener spray',
 'Odour eliminator spray','Car interior cleaner','Screen cleaner',
], ['250 ml','500 ml','750 ml spray','1 L refill','2 L refill','5 L can'], 'bottle')

spread(C, [
 'Dishwasher tablets','Dishwasher salt','Dishwasher rinse aid','Toilet rim block','Toilet cleaning tablets',
 'Drain unblocking granules','Washing soda','Baking soda (cleaning)','Borax','Oxygen bleach powder',
 'Scouring powder','Bar dish soap','Dish washing powder',
], ['small pack','medium pack','large pack','bulk pack'], 'pack')

spread(C, [
 'Sponge scourer','Non-scratch sponge','Steel wool scrubber','Copper scrubber','Coconut coir scrubber',
 'Microfibre cloth','Cotton cleaning cloth','Glass polishing cloth','Duster cloth','Chamois cloth',
 'Dish cloth','Kitchen wipe','Bathroom scrub pad','Magic eraser sponge',
], ['pack of 2','pack of 3','pack of 6','pack of 12','pack of 24'], 'pack')

spread(C, [
 'Broom (soft)','Broom (hard bristle)','Coconut stick broom','Long-handled brush','Toilet brush',
 'Toilet brush with holder','Bottle brush','Sink brush','Grout brush','Radiator brush',
 'Cobweb brush','Dustpan and brush set','Squeegee','Window squeegee','Floor squeegee',
 'Sponge mop','Spin mop','Flat microfibre mop','String mop','Steam mop pad','Mop refill head',
 'Bucket (10 L)','Bucket (15 L)','Bucket (20 L)','Mop bucket with wringer','Basin tub',
], ['-'], 'each')

spread(C, ['Rubber gloves','Nitrile cleaning gloves','Heavy-duty rubber gloves'],
       ['small','medium','large','extra large'], 'pair')

spread(C, ['Bin bag','Biodegradable bin bag','Heavy-duty bin bag','Compost caddy liner'],
       ['15 L (30)','30 L (30)','50 L (20)','60 L (20)','90 L (10)','120 L (10)'], 'roll')

spread(C, ['Kitchen bin','Pedal bin','Sensor bin','Recycling bin','Compost caddy','Outdoor wheelie bin'],
       ['5 L','12 L','20 L','30 L','50 L'], 'each')

# ── Laundry ─────────────────────────────────────────────────────────────
L = 'Laundry'
spread(L, [
 'Laundry detergent powder','Liquid detergent','Detergent for coloured clothes','Detergent for whites',
 'Baby-safe detergent','Wool and silk wash','Sports wash','Fabric conditioner','Fabric softener',
 'Liquid starch','Stain remover liquid','Pre-wash stain spray','Colour catcher sheets',
], ['500 g','1 kg','2 kg','4 kg','500 ml','1 L','2 L'], 'pack')

spread(L, ['Detergent pods','Bleach sachets','Dryer sheets','Scent booster beads','Washing machine cleaner'],
       ['pack of 12','pack of 24','pack of 40','pack of 60'], 'pack')

spread(L, [
 'Clothes pegs','Wooden clothes pegs','Stainless steel pegs','Peg bag','Clothes line rope',
 'Retractable clothes line','Foldable drying rack','Tower drying rack','Balcony drying rack',
 'Hanging drying net','Ironing board','Ironing board cover','Iron','Steam iron','Garment steamer',
 'Lint roller','Lint roller refill','Fabric shaver','Laundry basket','Laundry hamper',
 'Collapsible laundry bag','Mesh wash bag','Shoe wash bag','Sorting laundry basket','Bra wash ball',
 'Sock organiser clips','Starch spray','Ironing spray',
], ['-'], 'each')

spread(L, ['Clothes hanger (plastic)','Clothes hanger (wooden)','Clothes hanger (velvet)',
           'Trouser hanger','Skirt hanger','Multi-tier hanger'],
       ['pack of 5','pack of 10','pack of 20','pack of 30'], 'pack')

# ── Paper & disposables ─────────────────────────────────────────────────
P = 'Paper & disposables'
spread(P, ['Toilet roll','Toilet roll (recycled)','Toilet roll (3-ply)','Kitchen paper towel','Paper napkin',
           'Facial tissue box','Pocket tissue','Wet wipes','Antibacterial wipes','Baby wipes'],
       ['pack of 2','pack of 4','pack of 6','pack of 9','pack of 12','pack of 24'], 'pack')

spread(P, ['Aluminium foil','Cling film','Baking parchment','Greaseproof paper','Butter paper',
           'Freezer bag','Sandwich bag','Zip-lock bag','Vacuum seal bag','Bin liner (small)'],
       ['small roll','medium roll','large roll','catering roll','box of 25','box of 50','box of 100'], 'each')

spread(P, ['Paper plate','Paper cup','Plastic cup','Disposable bowl','Disposable spoon','Disposable fork',
           'Wooden cutlery set','Paper straw','Steel straw','Disposable food container','Takeaway box',
           'Cupcake liner','Doily','Table cover (disposable)','Banana leaf plate','Areca leaf plate'],
       ['pack of 10','pack of 25','pack of 50','pack of 100'], 'pack')

# ── Kitchen tools ───────────────────────────────────────────────────────
K = 'Kitchen tools'
spread(K, [
 'Chef knife','Paring knife','Bread knife','Utility knife','Santoku knife','Boning knife','Cleaver',
 'Knife sharpener','Honing steel','Knife block','Magnetic knife strip','Kitchen scissors','Poultry shears',
], ['-'], 'each')
spread(K, ['Cutting board (wood)','Cutting board (plastic)','Cutting board (bamboo)','Cutting board (glass)'],
       ['small','medium','large','set of 3'], 'each')
spread(K, [
 'Wooden spoon','Slotted spoon','Serving spoon','Ladle','Skimmer','Spatula (silicone)','Spatula (metal)',
 'Fish slice','Turner','Whisk','Balloon whisk','Tongs','Potato masher','Peeler','Julienne peeler',
 'Zester','Box grater','Flat grater','Coconut scraper','Garlic press','Ginger grater','Citrus juicer',
 'Can opener','Bottle opener','Jar opener','Corkscrew','Rolling pin','Chapati rolling board','Pastry brush',
 'Basting brush','Meat thermometer','Oven thermometer','Kitchen timer','Kitchen scale','Measuring jug',
 'Colander','Sieve','Fine mesh strainer','Tea strainer','Salad spinner','Mandoline slicer','Egg slicer',
 'Egg separator','Egg ring','Melon baller','Ice cream scoop','Pizza cutter','Cheese slicer','Mortar and pestle',
 'Masala dabba','Chakla belan','Puri press','Idli stand','Dosa tawa spreader','Chapati tongs','Sev press',
 'Murukku maker','Coconut grater (traditional)','Butter churner','Milk frother','Tea infuser',
], ['-'], 'each')
spread(K, ['Measuring cup set','Measuring spoon set','Mixing bowl set','Nesting bowl set','Prep bowl set'],
       ['3-piece','4-piece','5-piece','6-piece'], 'set')

# ── Cookware ────────────────────────────────────────────────────────────
CW = 'Cookware'
spread(CW, ['Frying pan (non-stick)','Frying pan (stainless steel)','Frying pan (cast iron)',
            'Saucepan','Stock pot','Sauté pan','Wok','Kadai (iron)','Kadai (non-stick)','Tawa (iron)',
            'Tawa (non-stick)','Dosa tawa','Appam pan','Paniyaram pan','Grill pan','Casserole dish',
            'Dutch oven','Milk pan','Steamer pot','Pasta pot','Roasting tin','Egg pan'],
       ['16 cm','18 cm','20 cm','22 cm','24 cm','26 cm','28 cm','30 cm'], 'each')
spread(CW, ['Pressure cooker','Stainless steel pressure cooker','Hard anodised pressure cooker'],
       ['2 L','3 L','5 L','7.5 L','10 L'], 'each')
spread(CW, ['Pot lid','Glass lid','Splatter guard','Trivet','Pan protector','Cookware set'],
       ['small','medium','large'], 'each')

# ── Bakeware ────────────────────────────────────────────────────────────
B = 'Bakeware'
spread(B, ['Cake tin (round)','Cake tin (square)','Springform tin','Loaf tin','Muffin tray','Cupcake tray',
           'Baking tray','Baking sheet','Cooling rack','Pie dish','Tart tin','Brownie tin','Bundt tin',
           'Swiss roll tin','Pizza tray','Bread tin','Ramekin','Silicone mould','Cookie cutter set'],
       ['small','medium','large'], 'each')
spread(B, ['Piping bag','Piping nozzle set','Cake turntable','Cake scraper','Palette knife','Dough scraper',
           'Sifter','Pastry mat','Silicone baking mat','Cake board','Cake tester','Oven mitt','Pot holder',
           'Apron','Chef hat'], ['-'], 'each')

# ── Tableware ───────────────────────────────────────────────────────────
T = 'Tableware'
spread(T, ['Dinner plate','Side plate','Quarter plate','Soup bowl','Cereal bowl','Katori','Thali',
           'Serving bowl','Serving platter','Mug','Tea cup','Saucer','Coffee cup','Glass tumbler',
           'Water glass','Wine glass','Champagne flute','Whisky glass','Beer glass','Juice glass',
           'Jug','Water pitcher','Tea pot','Coffee pot','Sugar bowl','Milk jug','Butter dish',
           'Salt and pepper set','Gravy boat','Chutney bowl'],
       ['each','set of 2','set of 4','set of 6','set of 12'], 'each')
spread(T, ['Dinner fork','Dinner knife','Tea spoon','Table spoon','Dessert spoon','Soup spoon',
           'Steak knife','Butter knife','Serving fork','Chopsticks'],
       ['set of 2','set of 4','set of 6','set of 12'], 'set')
spread(T, ['Table mat','Coaster','Table runner','Tablecloth','Napkin (cloth)','Napkin ring','Cutlery tray'],
       ['set of 2','set of 4','set of 6'], 'set')

# ── Food storage ────────────────────────────────────────────────────────
FS = 'Food storage'
spread(FS, ['Airtight container','Glass storage jar','Steel storage container','Plastic food container',
            'Spice jar','Masala container','Pickle jar','Cereal dispenser','Bread bin','Lunch box',
            'Steel tiffin carrier','Insulated tiffin','Bento box','Snack pot','Salad container',
            'Water bottle (steel)','Water bottle (plastic)','Water bottle (glass)','Flask','Thermos',
            'Insulated jug','Ice box','Cool bag','Freezer container','Ice cube tray','Ice pop mould'],
       ['250 ml','500 ml','750 ml','1 L','1.5 L','2 L','set of 3','set of 5'], 'each')
spread(FS, ['Vacuum sealer bag','Reusable silicone bag','Beeswax food wrap','Jar label','Chalk marker label',
            'Container clip','Bag clip','Bottle stopper','Jar seal ring'],
       ['pack of 6','pack of 12','pack of 24'], 'pack')

# ── Small appliances ────────────────────────────────────────────────────
SA = 'Small appliances'
for n in ['Electric kettle','Toaster','Sandwich maker','Waffle maker','Blender','Hand blender',
          'Mixer grinder','Wet grinder','Food processor','Stand mixer','Hand mixer','Juicer',
          'Cold press juicer','Coffee maker','Espresso machine','French press','Milk frother (electric)',
          'Air fryer','Microwave oven','OTG oven','Induction cooktop','Electric pressure cooker',
          'Slow cooker','Rice cooker','Egg boiler','Electric steamer','Roti maker','Idli maker (electric)',
          'Popcorn maker','Ice cream maker','Yoghurt maker','Electric griddle','Deep fryer','Food dehydrator',
          'Vacuum sealer','Electric chopper','Hand chopper','Atta kneader','Soda maker','Water purifier',
          'Water dispenser','Electric lunch box','Immersion rod','Electric tandoor','Sous vide stick']:
    add(n, SA, 'each')

# ── Bathroom ────────────────────────────────────────────────────────────
BA = 'Bathroom'
spread(BA, ['Bath towel','Hand towel','Face towel','Beach towel','Bath sheet','Bath mat','Toilet mat',
            'Shower curtain','Shower curtain ring','Bath robe','Loofah','Bath sponge','Back scrubber',
            'Pumice stone','Foot file','Soap dish','Soap dispenser','Toothbrush holder','Tumbler holder',
            'Toilet roll holder','Towel rail','Towel ring','Robe hook','Shower caddy','Shower shelf',
            'Bathroom mirror','Bathroom stool','Bath bucket','Bath mug','Water heater cover',
            'Shower head','Hand shower','Shower hose','Tap aerator','Toilet seat','Toilet seat cover',
            'Plunger','Bathroom bin','Laundry stool'],
       ['-'], 'each')

# ── Personal care ───────────────────────────────────────────────────────
PC = 'Personal care'
spread(PC, ['Bath soap','Herbal soap','Glycerine soap','Body wash','Shower gel','Body scrub','Body lotion',
            'Body butter','Body oil','Coconut hair oil','Almond oil','Deodorant','Antiperspirant',
            'Talcum powder','Prickly heat powder','Hand cream','Foot cream','Lip balm','Sunscreen',
            'Aftershave','Shaving cream','Shaving foam','Shaving gel','Face wash','Face scrub',
            'Face cream','Night cream','Moisturiser','Toner','Serum','Sheet mask','Face pack',
            'Micellar water','Makeup remover','Cotton pads','Cotton buds','Nail polish remover'],
       ['travel size','100 ml','200 ml','400 ml','500 ml','family pack'], 'each')
spread(PC, ['Razor','Disposable razor','Razor blade cartridge','Safety razor','Electric shaver',
            'Beard trimmer','Hair clipper','Nose trimmer','Epilator','Wax strips','Tweezers',
            'Nail clipper','Nail file','Nail scissors','Cuticle pusher','Manicure set','Pedicure set',
            'Hair brush','Comb','Wide-tooth comb','Detangling brush','Hair dryer','Hair straightener',
            'Curling iron','Hair rollers','Hair clip','Hair tie','Headband','Shower cap','Hair towel wrap'],
       ['-'], 'each')
spread(PC, ['Shampoo','Anti-dandruff shampoo','Conditioner','Hair mask','Hair serum','Hair gel',
            'Hair wax','Hair spray','Dry shampoo','Hair colour','Henna powder','Hair growth oil'],
       ['100 ml','200 ml','340 ml','650 ml','1 L'], 'bottle')
spread(PC, ['Toothpaste','Herbal toothpaste','Whitening toothpaste','Sensitive toothpaste','Mouthwash',
            'Toothbrush','Electric toothbrush','Toothbrush head','Dental floss','Floss picks',
            'Interdental brush','Tongue cleaner','Denture cleaner','Teeth whitening strips'],
       ['single','pack of 2','pack of 4','family pack'], 'pack')
spread(PC, ['Sanitary pad','Panty liner','Tampon','Menstrual cup','Period underwear','Intimate wash'],
       ['pack of 8','pack of 16','pack of 30','value pack'], 'pack')

# ── Health & first aid ──────────────────────────────────────────────────
H = 'Health & first aid'
spread(H, ['Adhesive bandage','Waterproof plaster','Fabric plaster','Gauze pad','Gauze roll',
           'Crepe bandage','Elastic bandage','Cotton wool','Cotton roll','Medical tape','Micropore tape',
           'Antiseptic liquid','Antiseptic cream','Burn gel','Pain relief spray','Pain relief gel',
           'Hot water bottle','Heat patch','Ice pack','Instant cold pack','Eye patch','Sling',
           'Finger splint','Knee support','Ankle support','Wrist support','Back support belt'],
       ['small','medium','large'], 'each')
for n in ['First aid kit','Digital thermometer','Infrared thermometer','Blood pressure monitor',
          'Pulse oximeter','Glucometer','Glucometer strips','Weighing scale','Body fat scale',
          'Nebuliser','Steam inhaler','Hot water bag','Pill organiser','Pill cutter','Medicine spoon',
          'Oral syringe','Face mask (surgical)','Face mask (N95)','Hand sanitiser','Disposable gloves',
          'Tweezers (medical)','Medical scissors','Eye wash cup','Ear syringe','Walking stick',
          'Crutches','Wheelchair cushion','Compression socks','Sleep mask','Ear plugs']:
    add(n, H, 'each')

# ── Baby & kids ─────────────────────────────────────────────────────────
BK = 'Baby & kids'
spread(BK, ['Nappy','Baby diaper','Swim nappy','Training pants','Nappy bin liner'],
       ['newborn','size 1','size 2','size 3','size 4','size 5','size 6'], 'pack')
for n in ['Baby wipes (fragrance-free)','Nappy rash cream','Baby lotion','Baby oil','Baby shampoo',
          'Baby soap','Baby powder','Baby bath tub','Baby bath seat','Changing mat','Nappy bag',
          'Feeding bottle','Bottle teat','Bottle brush (baby)','Bottle steriliser','Breast pump',
          'Nursing pads','Baby bib','Muslin cloth','Burp cloth','Pacifier','Pacifier clip','Teether',
          'Baby food maker','Baby bowl set','Baby spoon set','Sippy cup','High chair','Booster seat',
          'Baby monitor','Night light','Cot mattress','Cot sheet','Sleeping bag (baby)','Swaddle wrap',
          'Baby carrier','Baby sling','Pram','Stroller','Car seat','Play mat','Playpen','Stair gate',
          'Corner guard','Socket cover','Cabinet lock','Bath thermometer','Kids cutlery set',
          'Kids plate set','Kids water bottle','Kids lunch box','School bag','Kids umbrella']:
    add(n, BK, 'each')

# ── Pet supplies ────────────────────────────────────────────────────────
PS = 'Pet supplies'
spread(PS, ['Dog food','Puppy food','Cat food','Kitten food','Dog treats','Cat treats','Bird feed',
            'Fish food','Rabbit food','Hamster food'],
       ['500 g','1 kg','3 kg','7 kg','15 kg'], 'pack')
for n in ['Pet bowl','Slow feeder bowl','Water fountain (pet)','Pet bed','Pet blanket','Pet crate',
          'Pet carrier','Dog lead','Retractable lead','Dog collar','Cat collar','Harness','Name tag',
          'Litter tray','Cat litter','Litter scoop','Poop bags','Pet shampoo','Pet brush','Deshedding tool',
          'Nail clipper (pet)','Flea treatment','Tick collar','Chew toy','Squeaky toy','Catnip toy',
          'Scratching post','Cat tree','Pet gate','Pet stain remover','Aquarium filter','Aquarium heater',
          'Bird cage','Bird perch','Hamster wheel','Pet first aid kit']:
    add(n, PS, 'each')

# ── Hardware & maintenance ──────────────────────────────────────────────
HW = 'Hardware'
for size in ['3 mm','4 mm','5 mm','6 mm','8 mm','10 mm']:
    for L2 in ['16 mm','25 mm','40 mm','50 mm','75 mm','100 mm']:
        add(f'Wood screw {size} × {L2}', HW, 'box')
for size in ['M3','M4','M5','M6','M8','M10']:
    for L2 in ['16 mm','25 mm','40 mm','60 mm']:
        add(f'Machine screw {size} × {L2}', HW, 'box')
        add(f'Bolt {size} × {L2}', HW, 'box')
for size in ['M3','M4','M5','M6','M8','M10','M12']:
    add(f'Hex nut {size}', HW, 'box'); add(f'Washer {size}', HW, 'box')
    add(f'Spring washer {size}', HW, 'box'); add(f'Wall plug {size}', HW, 'box')
for L2 in ['20 mm','25 mm','40 mm','50 mm','65 mm','75 mm','100 mm']:
    add(f'Nail {L2}', HW, 'box'); add(f'Panel pin {L2}', HW, 'box')
spread(HW, ['Picture hook','Command hook','Cup hook','Screw eye','Bracket','L-bracket','Shelf bracket',
            'Hinge','Door latch','Padlock','Door chain','Door stopper','Door handle','Cabinet knob',
            'Drawer runner','Castor wheel','Curtain rod bracket','Chain link','Carabiner'],
       ['small','medium','large'], 'each')
spread(HW, ['Duct tape','Masking tape','Electrical tape','Double-sided tape','Packing tape','PTFE tape',
            'Anti-slip tape','Foam tape','Insulation tape'],
       ['25 mm × 10 m','48 mm × 25 m','48 mm × 50 m'], 'roll')
spread(HW, ['Super glue','Wood glue','PVA glue','Epoxy adhesive','Contact adhesive','Silicone sealant',
            'Acrylic sealant','Tile adhesive','Grout','Wall filler','Wood filler','Rust converter',
            'Machine oil','Penetrating oil','WD-40 spray','Grease'],
       ['small tube','standard tube','large tube','cartridge'], 'each')
spread(HW, ['Emulsion paint','Gloss paint','Primer','Undercoat','Wood stain','Varnish','Enamel paint',
            'Spray paint','Wall putty','Waterproof coating'],
       ['200 ml','1 L','2.5 L','5 L','10 L','20 L'], 'each')
spread(HW, ['Paint brush','Angled paint brush','Paint roller','Roller sleeve','Roller tray','Paint kettle',
            'Sanding block','Sandpaper sheet','Sanding sponge','Scraper','Filling knife','Caulking gun',
            'Dust sheet','Masking film'],
       ['25 mm','50 mm','75 mm','100 mm','150 mm'], 'each')
for g in ['40','60','80','120','180','240','320','400','600','800','1000','1500','2000']:
    add(f'Sandpaper, {g} grit', HW, 'sheet')

# ── Tools ───────────────────────────────────────────────────────────────
TL = 'Tools'
spread(TL, ['Claw hammer','Ball-peen hammer','Rubber mallet','Screwdriver (flat)','Screwdriver (Phillips)',
            'Precision screwdriver set','Ratchet screwdriver','Adjustable spanner','Combination spanner',
            'Socket set','Allen key set','Torx key set','Pliers','Long-nose pliers','Cutting pliers',
            'Locking pliers','Wire stripper','Crimping tool','Hacksaw','Handsaw','Tenon saw','Junior hacksaw',
            'Utility knife (tool)','Chisel','Wood plane','File set','Rasp','Clamp','G-clamp','Bench vice',
            'Spirit level','Tape measure','Folding ruler','Steel rule','Try square','Combination square',
            'Marking gauge','Carpenter pencil','Chalk line','Stud finder','Voltage tester','Multimeter',
            'Soldering iron','Solder wire','Desoldering pump','Heat gun','Glue gun','Glue stick',
            'Tool box','Tool bag','Tool belt','Step ladder','Extension ladder','Work bench','Work light',
            'Head torch','Torch','Knee pads','Safety goggles','Safety gloves','Dust mask','Ear defenders'],
       ['-'], 'each')
spread(TL, ['Cordless drill','Hammer drill','Impact driver','Angle grinder','Jigsaw','Circular saw',
            'Orbital sander','Belt sander','Router','Rotary tool','Nail gun','Air compressor',
            'Pressure washer','Wet and dry vacuum'],
       ['-'], 'each')
for d in ['1 mm','2 mm','3 mm','4 mm','5 mm','6 mm','8 mm','10 mm','12 mm']:
    add(f'HSS drill bit {d}', TL, 'each')
    add(f'Masonry drill bit {d}', TL, 'each')
    add(f'Wood drill bit {d}', TL, 'each')

# ── Electrical & lighting ───────────────────────────────────────────────
EL = 'Electrical & lighting'
for fit in ['B22 bayonet','E27 screw','E14 small screw','GU10 spot','G9 capsule','MR16 spot']:
    for w in ['3 W','5 W','7 W','9 W','12 W','15 W','18 W']:
        for k in ['warm white','cool white','daylight']:
            add(f'LED bulb {fit} {w} {k}', EL, 'each')
spread(EL, ['LED tube light','LED panel light','LED strip light','Batten light','Ceiling light','Pendant light',
            'Table lamp','Floor lamp','Desk lamp','Bedside lamp','Night light','Emergency light',
            'Rechargeable lantern','Solar garden light','Fairy lights','String lights','Motion sensor light',
            'Under-cabinet light','Mirror light','Picture light'],
       ['-'], 'each')
spread(EL, ['Extension lead','Surge protector','Multi-plug adaptor','Travel adaptor','USB wall charger',
            'USB-C cable','Micro-USB cable','Lightning cable','HDMI cable','Ethernet cable','Aux cable',
            'Speaker wire','Electrical wire','Junction box','Wall socket','Light switch','Dimmer switch',
            'Smart plug','Smart switch','Fuse','MCB','Doorbell','Ceiling fan','Table fan','Pedestal fan',
            'Exhaust fan','Wall fan','Voltage stabiliser','Inverter battery','UPS'],
       ['-'], 'each')

# ── Batteries & power ───────────────────────────────────────────────────
BT = 'Batteries & power'
for t in ['AA alkaline','AAA alkaline','AA rechargeable','AAA rechargeable','C cell','D cell',
          '9V block','AAAA','23A','A23','CR2032','CR2025','CR2016','CR1620','LR44','SR626',
          'CR123A','18650 li-ion','21700 li-ion','Button cell assorted']:
    for p in ['pack of 2','pack of 4','pack of 8','pack of 12','pack of 24']:
        add(f'{t} battery, {p}', BT, 'pack')
for n in ['Battery charger','Smart battery charger','Power bank (5,000 mAh)','Power bank (10,000 mAh)',
          'Power bank (20,000 mAh)','Solar power bank','Jump starter','Car charger','Wireless charging pad',
          'Battery tester','Coin cell holder']:
    add(n, BT, 'each')

# ── Office & stationery ─────────────────────────────────────────────────
OS = 'Office & stationery'
spread(OS, ['Ballpoint pen','Gel pen','Fountain pen','Rollerball pen','Marker pen','Permanent marker',
            'Whiteboard marker','Highlighter','Pencil','Mechanical pencil','Colour pencil','Crayon',
            'Sketch pen','Fineliner','Chalk','Eraser','Sharpener','Correction pen','Correction tape'],
       ['single','pack of 5','pack of 10','pack of 12','pack of 20','box of 50'], 'pack')
spread(OS, ['Notebook','Spiral notebook','Ruled notebook','Graph notebook','Plain notebook','Exercise book',
            'Journal','Diary','Planner','Sticky note pad','Index card','Legal pad','Memo pad'],
       ['A6','A5','A4','B5','pocket'], 'each')
spread(OS, ['Printer paper','Copy paper','Photo paper','Card stock','Coloured paper','Tracing paper',
            'Chart paper','Craft paper','Envelope','Window envelope','Padded envelope'],
       ['A4 (100)','A4 (500)','A3 (100)','pack of 25','pack of 50'], 'pack')
spread(OS, ['Stapler','Staple pin','Staple remover','Paper clip','Binder clip','Push pin','Drawing pin',
            'Rubber band','Bulldog clip','Hole punch','Ring binder','Lever arch file','Box file',
            'Document wallet','Plastic folder','Display book','Sheet protector','Index divider',
            'File label','Name badge','Lanyard','ID card holder','Clipboard','Desk organiser','Pen stand',
            'Paper tray','Book stand','Book end','Whiteboard','Cork board','Notice board','Magnet',
            'Scissors (office)','Paper trimmer','Guillotine','Laminator','Laminating pouch','Shredder',
            'Calculator','Scientific calculator','Label maker','Label tape','Stamp pad','Rubber stamp',
            'Glue stick (office)','Liquid glue','Ruler','Set square','Protractor','Compass set','Geometry box'],
       ['-'], 'each')

# ── School supplies ─────────────────────────────────────────────────────
SS = 'School supplies'
for n in ['Pencil case','Backpack','Lunch bag','Water bottle (school)','Homework folder','Textbook cover',
          'Book label','Name sticker','Art smock','Paint apron','Poster board','Science fair board',
          'Scientific set','Dissection kit','Graph book','Music manuscript book','Recorder (instrument)',
          'Gym bag','PE kit bag','School shoe polish','Uniform badge','School tie','Library bag',
          'Reading pointer','Flash cards','Alphabet chart','Number chart','World map poster','Globe',
          'Abacus','Counting blocks','Whiteboard (small)','Homework planner','Report folder']:
    add(n, SS, 'each')

# ── Party & celebration ─────────────────────────────────────────────────
PT = 'Party & celebration'
spread(PT, ['Balloon','Foil balloon','Number balloon','Latex balloon','Balloon pump','Balloon arch kit',
            'Party banner','Birthday banner','Bunting','Streamer','Confetti','Party popper','Sparkler',
            'Birthday candle','Number candle','Cake topper','Party hat','Party mask','Party blower',
            'Gift bag','Gift wrap','Gift ribbon','Gift bow','Gift tag','Greeting card','Thank you card',
            'Invitation card','Party bag','Piñata','Photo booth prop','Table confetti','Centrepiece'],
       ['pack of 6','pack of 12','pack of 24','pack of 50'], 'pack')

# ── Pooja & festival ────────────────────────────────────────────────────
PJ = 'Pooja & festival'
for n in ['Agarbatti (incense sticks)','Dhoop sticks','Dhoop cones','Camphor tablets','Cotton wicks',
          'Long wicks','Ghee diya','Oil lamp (diya)','Brass diya','Silver diya','Clay diya','Diya oil',
          'Kumkum','Haldi powder (pooja)','Chandan paste','Vibhuti','Rangoli powder','Rangoli stencil',
          'Pooja thali','Kalash','Bell (ghanti)','Conch shell','Aarti stand','Incense holder',
          'Agarbatti stand','Idol stand','Pooja mat','Asana mat','Toran (door hanging)','Marigold garland',
          'Mango leaf string','Coconut (pooja)','Betel leaves','Supari','Panchamrit set','Copper kalash',
          'Puja cloth','Deity dress','Mala (rudraksha)','Mala (tulsi)','Japa mala bag','Prasad box',
          'Modak mould','Festival lantern (kandil)','String of lights (diwali)','Rakhi','Rakhi thali',
          'Holi colours','Pichkari','Ganesh idol','Lakshmi idol','Nameplate (torana)']:
    add(n, PJ, 'each', 'in')

# ── Garden & outdoor ────────────────────────────────────────────────────
G = 'Garden & outdoor'
spread(G, ['Plant pot (terracotta)','Plant pot (plastic)','Plant pot (ceramic)','Hanging planter',
           'Window box','Grow bag','Seed tray','Propagator','Saucer tray','Self-watering pot'],
       ['10 cm','15 cm','20 cm','25 cm','30 cm','40 cm'], 'each')
spread(G, ['Potting compost','Garden soil','Cocopeat','Vermicompost','Perlite','Vermiculite','Bark mulch',
           'Gravel','Sand','Plant food','Liquid fertiliser','Bone meal','Neem cake','Epsom salt (garden)'],
       ['1 kg','5 kg','10 kg','25 kg','1 L','5 L'], 'bag')
for n in ['Trowel','Hand fork','Secateurs','Pruning saw','Loppers','Hedge shears','Garden spade','Garden fork',
          'Rake','Hoe','Garden knife','Watering can','Hose pipe','Hose reel','Hose nozzle','Sprinkler',
          'Drip irrigation kit','Spray bottle (garden)','Garden gloves','Kneeling pad','Wheelbarrow',
          'Garden trug','Plant support stake','Bamboo cane','Plant tie','Trellis','Plant label','Seed packet',
          'Bird feeder','Bird bath','Garden bench','Patio chair','Patio table','Parasol','Parasol base',
          'Outdoor cushion','Barbecue grill','Barbecue charcoal','Fire lighter','Grill brush','Outdoor mat',
          'Garden fence panel','Garden netting','Weed membrane','Compost bin','Leaf blower','Lawn mower',
          'Strimmer','Garden shredder','Garden shed lock','Solar lantern','Outdoor extension lead']:
    add(n, G, 'each')

# ── Car care ────────────────────────────────────────────────────────────
CR = 'Car care'
for n in ['Car shampoo','Car wax','Car polish','Tyre shine','Glass cleaner (car)','Dashboard polish',
          'Upholstery cleaner (car)','Engine degreaser','Screen wash','Antifreeze','Brake fluid',
          'Engine oil','Gear oil','Coolant','Power steering fluid','Chain lube','Microfibre car cloth',
          'Wash mitt','Wheel brush','Detailing brush','Drying towel','Bucket with grit guard','Sponge (car)',
          'Chamois leather','Car vacuum','Jump leads','Tyre inflator','Tyre pressure gauge','Puncture kit',
          'Car jack','Wheel wrench','Tow rope','Warning triangle','Hi-vis vest','Car first aid kit',
          'Fire extinguisher (car)','Ice scraper','Snow brush','Sun shade','Car cover','Seat cover',
          'Floor mat set','Boot liner','Steering wheel cover','Phone mount','Dash cam','Air freshener (car)',
          'Number plate screw','Wiper blade','Rear wiper blade','Headlight bulb','Fuse kit (car)']:
    add(n, CR, 'each')

# ── Pest control ────────────────────────────────────────────────────────
PE = 'Pest control'
spread(PE, ['Mosquito repellent spray','Mosquito coil','Mosquito vaporiser refill','Mosquito net',
            'Mosquito racket','Cockroach spray','Cockroach gel','Cockroach bait','Ant killer gel',
            'Ant powder','Fly spray','Fly paper','Fly swatter','Rat poison','Rat trap','Glue trap',
            'Mouse trap','Bed bug spray','Termite spray','Lizard repellent','Moth balls','Moth repellent sachet',
            'Silverfish trap','Wasp nest killer','Weed killer','Slug pellets','Ultrasonic pest repeller'],
       ['-'], 'each')

# ── Bedding & linens ────────────────────────────────────────────────────
BD = 'Bedding & linens'
spread(BD, ['Bed sheet','Fitted sheet','Flat sheet','Duvet cover','Duvet','Quilt','Comforter','Blanket',
            'Fleece blanket','Bedspread','Mattress protector','Mattress topper','Pillow','Memory foam pillow',
            'Bolster','Pillow cover','Cushion','Cushion cover','Throw','Electric blanket','Mosquito net (bed)'],
       ['single','double','queen','king','super king'], 'each')
spread(BD, ['Curtain','Blackout curtain','Sheer curtain','Curtain rod','Curtain ring','Curtain hook',
            'Roller blind','Venetian blind','Roman blind','Door curtain','Window film'],
       ['small','medium','large'], 'each')

# ── Storage & organisation ──────────────────────────────────────────────
SO = 'Storage & organisation'
spread(SO, ['Storage box','Clear storage box','Under-bed box','Fabric storage bin','Wicker basket',
            'Storage trunk','Vacuum storage bag','Wardrobe organiser','Shoe rack','Shoe box',
            'Drawer divider','Drawer organiser','Cutlery organiser','Spice rack','Kitchen shelf',
            'Corner shelf','Wall shelf','Floating shelf','Bookcase','Storage cube','Storage ottoman',
            'Hanging organiser','Over-door hook','Utility cart','Trolley','Stackable crate','Pegboard',
            'Cable organiser','Cable tie','Label sticker'],
       ['small','medium','large','set of 2','set of 3'], 'each')

# ── Safety & emergency ──────────────────────────────────────────────────
SF = 'Safety & emergency'
for n in ['Smoke alarm','Carbon monoxide alarm','Heat alarm','Fire extinguisher','Fire blanket','Fire escape ladder',
          'Emergency torch','Emergency radio','Whistle','Emergency blanket','Water purification tablets',
          'Emergency food ration','Power cut lamp','Candle (emergency)','Match box','Lighter','Gas leak detector',
          'Door alarm','Window lock','Safe box','Key safe','Security camera','Video doorbell','Motion sensor',
          'Anti-slip mat','Grab rail','Corner protector','Fire-resistant document bag','Emergency contact card']:
    add(n, SF, 'each')

# ── Sewing & mending ────────────────────────────────────────────────────
SW = 'Sewing & mending'
spread(SW, ['Sewing thread','Embroidery thread','Elastic band tape','Ribbon','Bias binding','Velcro tape',
            'Zip','Button','Snap fastener','Hook and eye','Safety pin','Sewing pin','Sewing needle',
            'Darning needle','Thimble','Seam ripper','Tailor chalk','Measuring tape (sewing)','Pin cushion',
            'Fabric scissors','Pinking shears','Iron-on patch','Knee patch','Fabric glue','Sewing machine oil',
            'Bobbin','Sewing machine needle','Knitting needle','Crochet hook','Wool yarn','Cotton yarn'],
       ['small','standard','assorted pack'], 'each')

# ── Craft & hobby ───────────────────────────────────────────────────────
CF = 'Craft & hobby'
spread(CF, ['Acrylic paint','Watercolour paint','Oil paint','Poster colour','Fabric paint','Glass paint',
            'Paint palette','Canvas board','Stretched canvas','Sketch pad','Watercolour pad','Charcoal stick',
            'Pastel set','Oil pastel','Marker set','Calligraphy pen','Ink bottle','Modelling clay','Air-dry clay',
            'Polymer clay','Play dough','Craft glue','Hot glue stick','Glitter','Sequins','Beads','Bead wire',
            'Pipe cleaner','Pom pom','Googly eyes','Craft foam sheet','Felt sheet','Craft stick','Origami paper',
            'Scrapbook','Washi tape','Stamp set','Stencil','Cutting mat','Craft knife','Punch tool'],
       ['small','medium','large','set'], 'each')

# ── Sports & fitness ────────────────────────────────────────────────────
SP = 'Sports & fitness'
for n in ['Yoga mat','Yoga block','Yoga strap','Exercise ball','Resistance band','Skipping rope',
          'Dumbbell set','Kettlebell','Barbell','Weight plate','Ankle weight','Push-up bar','Pull-up bar',
          'Ab roller','Foam roller','Massage gun','Massage ball','Gym gloves','Wrist wrap','Knee sleeve',
          'Water bottle (sports)','Shaker bottle','Gym towel','Gym bag (sports)','Fitness tracker',
          'Skipping mat','Treadmill mat','Badminton racket','Shuttlecock','Tennis ball','Cricket bat',
          'Cricket ball','Football','Basketball','Volleyball','Table tennis bat','Table tennis ball',
          'Swimming goggles','Swim cap','Swim float','Bicycle pump','Bicycle helmet','Bicycle lock',
          'Bicycle light','Skateboard','Roller skates','Camping mat','Sleeping bag','Tent','Camping stove',
          'Camping lantern','Cool box (camping)','Trekking pole','Rucksack']:
    add(n, SP, 'each')

# ── Travel ──────────────────────────────────────────────────────────────
TV = 'Travel'
spread(TV, ['Suitcase','Cabin bag','Duffel bag','Backpack (travel)','Travel organiser','Packing cube',
            'Toiletry bag','Travel bottle set','Luggage tag','Luggage strap','Luggage scale','Luggage lock',
            'Neck pillow','Eye mask (travel)','Travel blanket','Travel adaptor set','Passport holder',
            'Money belt','Document pouch','Shoe bag','Laundry bag (travel)','Umbrella','Folding umbrella',
            'Rain poncho','Travel mug','Travel kettle','Travel iron','Travel clothes line'],
       ['small','medium','large'], 'each')

# ── Shoe care ───────────────────────────────────────────────────────────
SH = 'Shoe care'
for n in ['Shoe polish (black)','Shoe polish (brown)','Shoe polish (neutral)','Liquid shoe polish',
          'Shoe cream','Suede cleaner','Suede brush','Shoe brush','Polishing cloth','Shoe horn','Shoe tree',
          'Insole','Gel insole','Arch support insole','Heel grip','Shoe deodoriser','Waterproofing spray',
          'Shoe laces (flat)','Shoe laces (round)','Boot laces','Shoe glue','Heel tip','Shoe rack (small)',
          'Shoe storage box','Sneaker cleaner kit','Anti-slip sole pad']:
    add(n, SH, 'each')

# ── Electronics accessories ─────────────────────────────────────────────
EA = 'Electronics accessories'
for n in ['Phone case','Screen protector','Tempered glass','Phone stand','Pop socket','Selfie stick',
          'Tripod','Ring light','Webcam','Headphones','Earphones','Wireless earbuds','Bluetooth speaker',
          'Sound bar','Keyboard','Mouse','Mouse pad','Wrist rest','Laptop stand','Laptop sleeve','Laptop bag',
          'Cooling pad','USB hub','Card reader','Memory card','USB flash drive','External hard drive',
          'SSD enclosure','Monitor','Monitor arm','HDMI switch','TV remote','Universal remote',
          'Cable clips','Cable sleeve','Cleaning kit (electronics)','Compressed air duster','Anti-static wipes',
          'Router','Wi-Fi extender','Powerline adaptor','Network switch','Printer ink cartridge',
          'Printer toner','Printer paper tray','Label printer roll']:
    add(n, EA, 'each')


# ── Plumbing ────────────────────────────────────────────────────────────
PL = 'Plumbing'
for d in ['15 mm','20 mm','25 mm','32 mm','40 mm','50 mm']:
    for k in ['PVC pipe','CPVC pipe','PPR pipe','Copper pipe','Elbow joint','Tee joint','Coupler',
              'Reducer','End cap','Ball valve','Gate valve','Pipe clamp','Union joint']:
        add(f'{k} {d}', PL, 'each')
spread(PL, ['Kitchen tap','Basin tap','Bib tap','Angle valve','Pillar cock','Shower mixer','Bath mixer',
            'Sink waste','Bottle trap','P-trap','Waste pipe','Flexible hose','Inlet hose','Drain cover',
            'Sink strainer','Tap washer','Rubber gasket','O-ring set','Cistern fitting','Float valve',
            'Toilet flush valve','Water tank fitting','Pipe insulation','Tank connector'],
       ['-'], 'each')
for n in ['Plumber tape','Pipe wrench','Basin wrench','Plunger (sink)','Drain snake','Pipe cutter',
          'Blow torch','Solder ring fitting','Leak sealing tape','Waterproof putty','Silicone gun',
          'Water pump','Booster pump','Water tank','Water filter cartridge','Tap filter','Shower filter']:
    add(n, PL, 'each')

# ── Home decor ──────────────────────────────────────────────────────────
HD = 'Home decor'
spread(HD, ['Photo frame','Collage frame','Wall art print','Canvas print','Wall clock','Table clock',
            'Alarm clock','Mirror (decor)','Vase','Flower vase','Artificial plant','Artificial flowers',
            'Candle holder','Scented candle','Tea light','Tea light holder','Diffuser','Reed diffuser',
            'Essential oil','Wind chime','Wall hanging','Tapestry','Dream catcher','Figurine','Showpiece',
            'Bookend (decor)','Tray (decorative)','Fruit bowl (decor)','Doormat','Area rug','Runner rug',
            'Floor cushion','Bean bag','Pouffe','Room divider','Wallpaper roll','Wall decal','Wall hook (decor)',
            'Fairy light curtain','Lampshade'],
       ['small','medium','large'], 'each')

# ── Seasonal ────────────────────────────────────────────────────────────
SN = 'Seasonal'
for n in ['Christmas tree','Tree stand','Tree skirt','Christmas lights','Baubles','Tinsel','Tree topper',
          'Advent calendar','Stocking','Wreath','Santa hat','Gift sack','Snow spray','Nativity set',
          'Halloween pumpkin','Halloween costume','Halloween mask','Cobweb decoration','Trick-or-treat bucket',
          'Easter egg basket','Egg decorating kit','New Year party kit','Sparkler (festival)','Sky lantern',
          'Beach umbrella','Beach mat','Inflatable pool','Pool float','Sun lounger','Hot water bottle cover',
          'Thermal blanket','Draught excluder','Window insulation film','Snow shovel','De-icer spray',
          'Grit salt','Winter door mat','Fan cover','Air cooler','Room heater','Oil heater','Humidifier',
          'Dehumidifier','Air purifier','Air purifier filter']:
    add(n, SN, 'each')

# ── Bathroom, sized ─────────────────────────────────────────────────────
spread('Bathroom', ['Bath towel set','Towel set','Bath rug','Anti-slip bath mat','Shower squeegee',
                    'Bathroom organiser','Shower basket','Corner shelf (bath)','Vanity tray',
                    'Toothpaste squeezer','Bathroom scale','Shower speaker','Shower timer','Bath pillow',
                    'Bath tray','Bath bomb','Bath salts','Bubble bath','Foot soak'],
       ['small','medium','large'], 'each')

# ── write out ───────────────────────────────────────────────────────────
seen, out = set(), []
for name, cat, unit, tags in rows:
    name = re.sub(r'\s+', ' ', name).strip()
    key = name.lower()
    if key in seen: continue
    seen.add(key)
    assert '|' not in name and '`' not in name and '${' not in name, name
    out.append(f'{name}|{cat}|{unit}|{tags}')

p = pathlib.Path('/root/artifact/data/supplies.txt')
p.write_text('\n'.join(out) + '\n')
cats = {}
for line in out:
    cats[line.split('|')[1]] = cats.get(line.split('|')[1], 0) + 1
print(f'{len(out)} supplies across {len(cats)} categories')
for k, v in sorted(cats.items(), key=lambda x: -x[1]):
    print(f'  {v:5d}  {k}')
