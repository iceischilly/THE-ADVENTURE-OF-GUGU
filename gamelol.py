#important stuff
import json
import time
trise=0
sleep=0
loop=True
gamesaveloll=0
filenamee="coledumlol"
inv=["default csgo knife","dragon lore awp"]
spellbook=["BIG ROCK"]
armor=1
loadingggg=None
loadingggg=False
stuff=[]
hp=100
maxhp=100
effects=None
import random
moneffects=None
roknum=1 #:(
mp=100
rokstun=-1
gp=10
checkpoint=1
hfbomb=0
shpp=0
mhpp=0
lhpp=0
mpp=0
mcslvl=200
magicrobe=1
atkefx=None
mondefch=10
awpammo=3
pammo=3
monsdef=False
tempinv=[]
tempstuff=[]
tempspellbook=[]
temparmor=None
tempmaxhp=100
tempmagicrobe=None
tempmp=100
temphp=100
tempgp=10
temproknum=1
tempshpp=0
tempmhpp=0
templhpp=0
tempmpp=0
gend=0
savepoint=None
mcsnum=0
mcslvl=0
savepointt=None
lvl=None

def saving(filenameee):
    

    f=open(filenameee,"w")
    
    values = {
                "hp" : hp,
                "inv" : inv,
                "mp" : mp,
                "spellbook" : spellbook,
                "gend" : gend,
                "roknum" : roknum,
                "maxhp" : maxhp,
                "shpp" : shpp,
                "mhpp" : mhpp,
                "lhpp" : lhpp,
                "mpp" : mpp,
                "gp" : gp,
                "stuff" : stuff,
                "armor" : armor,
                "magicrobe" : magicrobe,
                "savepoint" : savepoint,
                "mcsnum" : mcsnum,
                "mcslvl" : mcslvl,
                "mcslvl" : mcslvl,
                "savepointt" : savepointt,
                "checkpoint" : checkpoint
                
            }
    json.dump(values,f,indent=4)



#MAKE LOADING 
def loading(filenameee):
    filename=open(filenameee,"r")
    load=json.load(filename)
    hp=load["hp"]
    mp=load["mp"]
    gp=load["gp"]
    gend=load["gend"]
    roknum=load["roknum"]
    maxhp=load["maxhp"]
    mpp=load["mpp"]
    stuff=load["stuff"]
    armor=load["armor"]
    magicrobe=load["magicrobe"]
    mcsnum=load["mcsnum"]
    mcslvl=load["mcslvl"]
    savepointt=load["savepointt"]
    savepoint=load["savepoint"]
    lhpp=load["lhpp"]
    mhpp=load["mhpp"]
    shpp=load["shpp"]
    spellbook=load["spellbook"]
    inv=load["inv"]
    checkpoint=load["checkpoint"]
    








def fight():
    global effects
    global hp
    global moneffects
    global roknum #:(
    global mp
    global rokstun
    global gp
    global checkpoint
    global hfbomb
    global shpp
    global mhpp
    global lhpp
    global mpp
    global magicrobe
    global bhop
    global pammo
    global hp
    global inv
    global spellbook
    global atkefx
    global mondefch
    global awpammo
    global stuff
    global monsdefch
    global monsdef
    bhop=0
    f1A=None
    spell=None
    monshp=maxmonshp
    while monshp>0 and hp>0:
        stun=False
        monsdmg=tempmonsdmg
        if effects!=None:
            if effects=="fire":
                hp-=10
                print("you are burning hp-10")
            elif effects=="poison":
                hp-=20
                print("you are poisoned hp-20")
            elif effects=="hellfire":
                hp-40
                print("you are buring in hellfire hp-40")
            elif effects=="godfire":
                hp-100
                print("you are bruning in god fire")
        time.sleep(2)
        print("your hp is",hp)
        print("enemy hp is",monshp)
        print("your mp is",mp)
        print("your turn")
        hpp=str(input("do you want to use a health potion? (yes or no)"))
        if hpp=="yes":
            print("small hp potion(+50hp) you have",shpp,"small hp potions left")
            print()
            print("medium hp potion (+200hp) you have",mhpp,"medium hp potions left")
            print()
            print("large hp potions (+800hp) you have",lhpp,"large hp potions left")
            hpptype=str(input("pick what one you want to use(1=small 2=medium 3=large)"))
            if hpptype=="1":
                print("you used a small hp potion +50hp")
                hp+=50
                if hp>maxhp:
                    hp=maxhp
                print("your hp is now",hp)
            elif hpptype=="2":
                print("you used a medium hp potion +200hp")
                hp+=200
                if hp>maxhp:
                    hp=maxhp
                print("your hp is now",hp)
            elif hpptype=="3":
                print("you used a large hp potion +400hp")
                hp+=400
                if hp>maxhp:
                    hp=maxhp
                print("your hp is now",hp)
            else:
                print("invaild")
        elif hpp=="no":
            print("skipping hp potions")

        
        Lmpp=str(input("do you want to use a mp potion?(yes or no) you have " +str(mpp)+ " magic power potions left"))
        if Lmpp=="yes":
            mp+=25
            print("you used a magic power potion your mp is now:",mp)

        if magicrobe!=None:
            if magicrobe=="t1":
                print("mp+15 (magic robe t1)")
                mp+=15
            elif magicrobe=="t2":
                print("mp+25 (magic robe t2)")
                mp+=25
            elif magicrobe=="t3":
                print("mp+50 (magic robe t3)")
                mp+=50
            
        time.sleep(1)
        print("+5mp")
        mp+=5
        print("what do you want to use")
        print()
        print(inv)
        print("(type spellbook for spells)")
        f1=str(input("what would you like to use(type the name of the item or type 'defend' to take half dmg and heal some hp)"))
        print()

        #spell book-------------------------------------------------
        if f1=="spellbook":
            if "spellbook" in inv:
                print(spellbook)
                spell=str(input("what spell would you like to use"))
    
    #   csgo knife----------------------
        if f1=="default csgo knife":
                      
            f1A=str(input("do you want to start bhop (type 'bhop') or do you want to stab"))
            print()
        
         
            if f1A=="bhop":
                if bhop==0:
                    bhop+=50
                    print("bhop=50%")
                else:
                    if monsdef==True:
                        print("you have started going super fast and you strike the defending enemy in the back")
                        bhop=0
                        monshp=monshp-35
                        print()
                    else:
                        print("you have started going super fast and you strike the enemy in the back")
                        bhop=0
                        monshp=monshp-75
                        print()

        #stab --------------------       
        elif f1A=="stab":
            stab=random.randint(0, 11)
            if stab>=8:
                print("you jumped over the enemy and stabbed it in the back(critical hit 40dmg)")
                monshp-=40
                print()
                
            elif stab<8 and stab>2:
                if monsdef==True:
                    monshp-=10
                    print("you stab the defending enemy in the chest (10 dmg)")
                    print()
                else:
                    monshp-=20
                    print("you stab the enemy in the chest (20 dmg)")
                    print()
                
            else:
                print("you missed")
        
    #defend--------------------
        elif f1=="defend":
            print("you prepare for impact(dmg taken this round lowered hp +20%")
            if hp>maxhp*0.8:
                hp=maxhp
                print("fully healed")
            
            else:
                print("healed")
                hp+=hp*0.2
            monsdmg=monsdmg/2
        
        #hammer------------------------
        elif f1=="hammer":
            if "hammer" in inv:
                if monsdef==True:
                    print("enemy defending 15 dmg")
                    monshp-=15
                    hstun=random.randint(0, 11)
                    if hstun<5: 
                        stun=True
                else:
                    monshp-=30
                    hstun=random.randint(0, 11)
                    if hstun<5: 
                        stun=True
        #pistol--------------------------
        elif f1=="pistol":
            if "pistol" in inv:
                if pammo>0:
                    if monsdef==True:
                        print("you shot the defending enemy in the dome!!")
                        monshp-=45
                        pammo-=1
                        print(pammo,"shots left")
                    else:
                        print("you shot the enemy in the dome!!")
                        monshp-=90
                        pammo-=1
                        print(pammo,"shots left")
                else:
                    print("you have NO ammo")
                    print("reloading")
                    pammo=3
                    print(pammo,"shots left")
        #torch-------------------------------
        elif f1=="torch":
            if "torch" in inv:
                print("you made the enemy a lil crispy")
                monshp-=20
                moneffects=fire
        #baseball bat------------------------
        elif f1=="bat":
            if "bat" in inv:
                print("you hit a home run")
                bstun=random.randint(0, 11)
                if bstun<3: 
                    stun=True
                    monshp-=20
                    print("enemy is stunned")
                elif bstun>3 and bstun<7:
                    monsdmg=monsdmg/2
                    monshp-=20
                    print("enemy is weaker for this turn")

        #BIG sword------------------------
        elif f1=="big sword":
            if "big sword" in inv:
                print("you pull out a big sword out of your back pocket")
                bsstun=random.randint(0, 11)
                if bsstun<3:
                    print("you hit the enemy in the middle of its chest")
                    print("massive dmg")
                    if monsdef==True:
                        print("150dmg enemy defending")
                        monshp-=150
                    else:
                        print("300dmg")
                        monshp-=300
                else:
                    print("you missed")

        #rok--------------------------------
        elif f1=="rok":
            if "rok" in inv:
                if roknum>0:
                    print("you use rok")
                    print("you throw rok")
                    print("-1 rok")
                    roknum-=1
                    print(roknum,"roks left")
                    print("stunned enemy alot")
                    rokstun=3

                else:
                    print("no roks :(")
        #zuzu sword-----------------------------------------------
        elif f1=="zuzu sword":
            if "zuzu sword" in inv:
                print("you pull out the fallen sword of zuzu the world zucker")
                time.sleep(1)
                print("the sword burns up in a purple flame")
                time.sleep(1)
                print("it is radiating in a blinding purple light")
                time.sleep(1)
                print("you swing the sword at the enemy")
                print("setting it on god fire and slashing it with the blinding sword")
                zucrit=random.randint(0, 11)
                if zucrit<=3:
                    if monsdef==True:
                        print("CRITICAL")
                        
                        print("1000 dmg enemy defending")
                        monshp-=1000
                        moneffects="godfire"
                    else:
                        print("CRITICAL")
                        print("2000dmg")
                        monshp=monshp-2000
                        moneffects="godfire"
                else:
                    if monsdef==True:
                        print("500 dmg enemy defending")
                        monshp-=500
                        moneffects="godfire"
                    else:   
                        print("1000dmg")
                        monshp=monshp-1000
                        moneffects="godfire"
        #stinky dagger--------------------------------------------------------
        elif f1=="stinky dagger":
            if "stinky dagger"in inv:
                print("you pull out a dagger that smells very very bad")
                print("you stab the enemy with the very stink dagger")
                print("oof")
                sdag=random.randint(0, 11)
                if sdag>=6:
                    stun=True
                    print("this smell from the dagger is so bad that it stuns the enemy")
                if monsdef==True:
                    print("30 dmg enemy defending")
                    monshp-=30
                    moneffects="poison"
                else:   
                    print("60 dmg")
                    monshp-=60
                    moneffects="poison"
        #hellfire bomb---------------------------------------------------------
        elif f1=="hellfire bomb":
            if "hellfire bomb" in inv:
                if hfbomb>0:
                    hfbomb-=1
                    print("you threw the hellfire bomb at the enemy")
                    print(hfbombk,"hell fire bombs left")
                    hfb=random.randint(0, 11)
                    if hfb<=1:
                        print("the explosion from the hellfire bomb lit you of hellfire L bozo")
                    print("enemy on hellfire -40 hp every turn")
        #frying pan------------------------------------------------------------
        elif f1=="frying pan":
            if "frying pan" in inv:
                print("you pull out the best weapon in the whole game......")
                time.sleep(2)
                print("a frying pan")
                print("you swing the pan at the enemy bashing it in the middle of the head")
                fpan=random.randint(0, 11)
                time.sleep(1)
                if fpan<=2:
                    stun=True
                    print("you got a critical hit")
                    print("enemy stunned and 1250dmg")
                    monshp-=1250
                else:
                    monshp-=750
                    print("750dmg")
                monsdmg=monsdmg/1.5
                if hp>maxhp*0.9:
                    print("hp fully healed")
                    hp=maxhp
                else:
                    hp+=hp*0.1
        #ICE---------------------------------------------------------------
        elif f1=="I.C.E":
            if "I.C.E" in inv:
                if mp>=200:
                    mp-=200
                    print("you pull out the interdimensional creature ender (or ice)")
                    time.sleep(2)
                    print("The sword shines in the air as you hold it up")
                    print("A beam of light shoots from the top of the sword into the sky")
                    time.sleep(2)
                    print("The sky turns dark and a beam of pure light crashes into the ground")
                    print("on top of the enemy covering it")
                    print("the beam and sky clears showing the enemy bruning in the fire from the gods")
                    time.sleep(2)
                    print("enemy on god fire")
                    if monsdef==True:
                        print("2500dmg enemy defending")
                        monshp-=2500
                        moneffects="godfire"
                    else:
                        print("5000 dmg")
                        monshp-=5000
                        moneffects="godfire"
                else:
                    print("you are out of mp")
        #Big rock--------------------------------------------------------------------
        elif spell=="BIG ROCK":
            if "BIG ROCK" in spellbook:
                print("you say the magic words")
                print("ooga booga rok ooga booga rok")
                time.sleep(2)
                print("a big rock rockets down from the sky crushing the enemy")
                print("-50mp")
                mp-=50
                print("you have",mp,"mp left")
                if monsdef==True:
                    print("75dmg enemy defending")
                    monshp-=75
                else:
                    print("you did 150 dmg")
                    monshp-=150
                brstun=random.randint(0, 11)
                if brstun<3:
                      stun=True


        #blade of the gods-----------------------------------------------
        elif spell=="botg":
            if "botg" in inv:
                if mp>=400:
                    mp-=400
                    print("you have",mp,"mp left")
                    print("mp-400")
                    print("you use the botg or blade of the gods")
                    print("you chant the words: gugu,mumu,hima,gifon,dudu,ramram")
                    print("the sky turns dark and swords of pure light float down to your side")
                    time.sleep(1)
                    print("the swords fly at the enemy pircing them")
                    print("10000 dmg")
                    print("emeny burns the flames of the gods")
                    if monsdef==True:
                        print("5000dmg enemy defending")
                        monshp-=5000
                        moneffects="godfire"
                    else:
                        print("10000 dmg")
                        monshp-=10000
                        moneffects="godfire"
                else:
                    print("you are out of mp")

        #diamond sword----------------------------------------
        elif f1=="diamond sword":
            if "diamond sword" in inv:
                print("you pull out a sword made of diamonds")
                print("(fake diamonds)")
                diamondsw=random.randint(0, 11)
                if diamondsw<=1:
                    print("you swing at the enemy but")
                    print("the sword becomes real diamonds!")
                    print("you swing at the enemy again -400hp")
                    monshp-=400
                else:
                    if monsdef==True:
                        print("35dmg enemy defending")
                        monshp-=35
                    else:
                        print("you swing at the enemy -70hp")
                        monshp-=70
        #iron sword
        elif f1=="iron sword":
            if "iron sword" in inv:
                print("you pull out a iron sword")
                print("(not fake iron)")
                if monsdef==True:
                    print("100dmg enemy defending")
                    monshp-=100
                else:
                    print("you swing at the enemy -200hp")
                    monshp-=200

        #stone sword-------------------------------------
        elif f1=="stone sword":
            if "stone sword" in inv:
                print("you pull out a stone sword")
                print("made from the stone of gods")
                print("you swing at the enemy")
                if monsdef==True:
                    print("450dmg enemy defending")
                    monshp-=450
                else:
                    print("-700hp")
                    monshp-=700
        
                    

        #wood sword------------------------------------------
        elif f1=="wood sword":
            if "wood sword" in inv:
                print("you pull out a basic wood sword")
                print("you swing at the enemy")
                if monsdef==True:
                    print("900dmg mon defending")
                    monshp-=900
                else:
                    print("1800dmg")
                    monshp-=1800
        #shiny wood sword-----------------------------------------------------------
        elif f1=="shiny wood sword":
            if "shiny wood sword":
                print("you pull out the final form of the swords the shiny wood sword")
                print("you swing it at the enemy")
                time.sleep(2)
                print("100dmg")
                time.sleep(2)
                print("a massive shiny wooden sword falls from the sky crashing into the enemy")
                if monsdef==True:
                    print("2000dmg enemy defending")
                    monshp-=2000
                else:
                    print("4000dmg")
                    monshp-=4000
        #awp-----------------------------------------------------------------
        elif f1=="dragon lore awp":
            if "dragon lore awp"in inv:
                if awpammo>0:
                    print("you pull out the dragon lore awp")
                    print("it shines with a golden light")
                    time.sleep(1)
                    print("you load a bullet and ready the gun")
                    print("you scope in at the enemy")
                    time.sleep(1)
                    print("your finger presses down on the golden trigger firing")
                    awpammo-=1
                    print("you have", awpammo ,"ammo left")
                    if monsdef==True:
                        print("4500dmg enemy defending")
                        monshp-=4500
                    else:
                        print("7000dmg")
                        monshp-=7000
                else:
                    print("out of ammo reloading")
                    awpammo=3
                    print("you have", awpammo ,"ammo left")


        #effect healing-------------------------------------------
        elif spell=="effect heal":
            if "effect heal" in spellbook:
                if mp>50:
                    print("you say the magic words AAAAAAAAAAAAAAAAAAAAA")
                    print("you heal all effects")
                    effects=None
                    mp-=50
                else:
                    print("no mp")
        #light beam---------------------------------------------
        elif spell=="light beam":
            if "light beam" in spellbook:
                if mp>50:
                    print("you say the magic words MY EYES")
                    print("you shoot a beam of light")
                    print("enemy in god fire")
                    moneffects="godfire"
                    mp-=75
                else:
                    print("no mp")
        #blue gem  --------------------------------------------------         
        elif spell=="blue gem":
            if "blue gem" in spellbook:
                if "case hardened karambit" in stuff:
                    if mp>=800:
                        mp-=1000
                        print("you pull out the old case hardened karambit")
                        print("you say the magic words blue gem blue gem")
                        time.sleep(1)
                        print("the old yellow brown and kinda blue karambit turns a bright blue")
                        print("you hold it and you feel a pulse of energy go through your body")
                        time.sleep(1)
                        print("blue lighting bursts out of your body powering you")
                        print("you jump at the enemy and stab it")
                        time.sleep(1)
                        print("the enemy gets stunned")
                        print("150000dmg")
                        monshp-=150000
                        stun=True
                    else:
                        print("no mp")
                else:
                    print("you try and use the spell but you dont have the case hardened karambit")


        #flashbang-----------------------------------------------------------------
        elif spell=="flash bang":
            if "flash bang" in spellbook:
                if mp>=50:
                    print("mp-50")
                    print("FLASH BANG OUT!!!!!!!!!!")
                    print("a blinding light comes from your book")
                    print("enemy stunned for 2 turns")
                    rokstun=1
                else:
                    print("no mp")


        #magic sword-------------------------------------------
        elif spell=="magic sword":
            if "magic sword"in spellbook:
                if mp>=75:
                    print("a magical sword comes out of your book")
                    print("you stab the enemy with it")
                    if monsdef==True:
                        print("400dmg enemy defending")
                        monshp-=400
                    else:
                        print("800 dmg")
                        monshp-=800
                else:
                    print("no mp")
        #MONEY RAIN!!!!---------------------------------------------------
        elif spell=="money rain":
            if "money rain" in spellbook:
                if mp>=75:
                    print("you say the magic words MR CRABS")
                    print("money rains from they sky")
                    print("dmg = to your gp")
                    if monsdef==True:
                        print(gp/2,"dmg enemy defending")
                        monshp-=gp/2
                    else:
                        print(gp,"dmg")
                        monshp-=gp
                else:
                    print("no mp")
        



        #scouts bat
        elif f1=="scouts bat":
            if "scouts bat" in inv:
                print("BONK")
                if monsdef==True:
                    print("300dmg enemy defending")
                    monshp-=300
                    scoutstun=random.randint(0, 11)
                    if scoutstun<4:
                          stun=True
                else:
                    print("600dmg enemy defending")
                    monshp-=600
                    scoutstun=random.randint(0, 11)
                    if scoutstun<4:
                          stun=True


        #SUS knife
        elif f1=="sus knife":
            if "sus knife" in inv:
                print("you pull out a very sus knife")
                if monsdef==True:
                    print("200dmg enemy defending")
                    monshp-=200
                    susknife=random.randint(0, 20)
                    if susknife<1:
                          print("you pull out the knife and feel a very sus energy pulse from the knife")
                          print("2000 dmg enemy defending")
                          monshp-=2000
                    else:
                        print("400dmg")
                        monshp-=400
                        susknife=random.randint(0, 20)
                        if susknife<1:
                            print("you pull out the knife and feel a very sus energy pulse from the knife")
                            print("4000dmg")
                            monshp-=4000
        #lazer--------------------------------------------------
        elif spell=="BIG lazer":
            if "BIG lazer" in spellbook:
                if mp>=50:
                    mp-=50
                    print("you say the words BEEEEEEEEEEEEEEEEEEEEMMMMMMM")
                    print("a lazer beam shoots from the book")
                    if monsdef==True:
                          print("400 dmg enemy defending")
                          monshp-=400
                          moneffects="hellfire"
                    else:
                        print("800dmg")
                        monshp-=800
                        moneffects="hellfire"

                        #blood knife (get from bad route)
        elif f1=="bloody knife":
            if "bloody knife" in inv:
                if hp<hp*0.4:
                    print("you pull out a knife soaked in the blood of your enemys")
                    time.sleep(1)
                    print("you can hear the screams of the traped souls of everything you killed")
                    time.sleep(1)
                    print("the sky goes a dark red")
                    print("your vision goes dark")
                    time.sleep(2)
                    print("you wakeup with blood covered hands and the knife in you hands")
                    print("you feel a sharp pain in your heart (hp-40%)")
                    if monsdef==True:
                        print("50000 dmg menemy defending")
                        monshp-=50000
                    else:
                        print("100000 dmg")
                        monshp-=100000
                        #skele sword
        elif f1=="skeleton sword":
            if "skeleton sword" in inv:
                print("you pull out a sword made of bones and rags")
                time.sleep(1)
                if monsdef==True:
                    print("50 dmg enemy defending")
                    monshp-=50
                else:
                    print("100 dmg")
                    monshp-=100
                    
                    
                


        else:
            print("not valid item")


        
        time.sleep(2)
        print()
        print()
        if rokstun>0 and rokstun!=0 and rokstun!=-1 :
            stun=True
            rokstun-=1
            print("stun -1")
            if rokstun==0:
                print("one more turn for stun")
            else:
                print(rokstun,"turns left when enemy is stunned")
        print()
        print()
        print()
        if moneffects!=None:
            if moneffects=="fire":
                monshp-=10
                print("the enemy is burning hp-10")
            elif moneffects=="poison":
                monshp-=20
                print("the enemy is poisoned hp-20")
            elif moneffects=="hellfire":
                monshp-=40
                print("the enemy is buring in hellfire hp-40")
            elif moneffects=="godfire":
                monshp-=100
                print("they enemy is burning in the eternal flame of the gods hp-100")
        if monshp>0:
            if stun==True:
                print("enemy stuned")
            else:
            #enemy turn
                print("enemy turn")
                mondef=random.randint(1, mondefch)
                if mondef<=2:
                    print("monster is defending")
                    if monshp<=maxmonshp-maxmonshp*0.2:
                        monshp+=maxmonshp*0.2
                    else:
                        monshp=maxmonshp
                    monsdef=True
                else:
                    monatk=random.randint(0, 11)
                    if monatk>=8:
                        monsdmg+=monsdmg
                        print("the monster got a crtical hit")
                        hp=hp-monsdmg
                        if atkefx=="fire":
                           effects="fire"
                        elif atkefx=="poison":
                            effects="poison"
                        elif atkefx=="hellfire":
                            effects="hellfire"
                        elif atkefx=="godfire":
                            effects="godfire"
                            
                    if monatk<=1:
                        print("the enemy missed")
                
                    else:
                        print("the enemy hit you")
                        hp-=monsdmg
                        if atkefx=="fire":
                           effects="fire"
                        elif atkefx=="poison":
                            effects="poison"
                        elif atkefx=="hellfire":
                            effects="hellfire"
                        elif atkefx=="godfire":
                            effects="godfire"
        
        
            
    print("fight over")
    if hp<0:
        print("you died")
        if checkpoint=="c1":
            print("going to checkpoint 1")
            lvl=c1()
            
        elif checkpoint=="c2":
            print("going to checkpoint 2")
            lvl=c2()
            
        elif checkpoint=="c3":
            print("going to checkpoint 3")
            lvl=c3()
        elif savepointt==True:
            print("going to save point")
            lvl=savepoint
    elif monshp<0:
        print("you win! You will be now told you rewards!!!")






































#wall
def w1l4():
    print("not made yet")






#door
def w1l4a():
    global hp
    global inv
    global stuff
    global spellbook
    global gend
    global gp
    global maxmonshp
    global tempmonsdmg
    global atkefx
    global hfbomb
    global mp
    global trise
    print("you climb the wall into the stands")
    print("voice- 'i take it you dont want to come'")
    time.sleep(1)
    print("voice-'that is fine, but if your running you better run fast'")
    time.sleep(3)
    print("the next inputs are timed if you dont do it fast enough you will die")
    time.sleep(2)
    print("good luck")
    time.sleep(2)
    print("you keep running then wall close around you and he floor opens")
    time.sleep(2)
    print("the walls open and you are now in a hallway")
    time.sleep(1)
    print("you walk forwards then a saw flies down from the wall")
    time.sleep(1)
    print("to dodge right hit 'd' to jump hit 'w' to dodge left hit 'a' to slide hit 's'")
    time.sleep(3)
    trise==0
    enddd=False
    #run time----------------------
    while enddd==False:
        while trise<=3 and enddd==False:
            start=time.time()
            qtime=input("dodge right! ")
            time.sleep(2)
            if qtime=="d":
                end=time.time()
            else:
                print("you missed")
                trise+=1
                break
            if end-start>3:
                print("the saw hits you")
                trise+=1
                break
            print("you keep running but them spikes come up from the floor")
            time.sleep(1)
            start=time.time()
            qtime=input("JUMP!")
            time.sleep(2)
            
            #jump-------------------------------------------
            if qtime=="w":
                end=time.time()
            else:
                trise+=1
                break
            if end-start>3:
                print("the spikes hit you")
                trise+=1
                break
            print("voice-'impressive'")
            time.sleep(1)
            print("you keep running")
            time.sleep(1)
            print("some holes open in the wall ")
            time.sleep(1)
            print("but arrows get shot out!!!")
            
            start=time.time()
            #slide------------------------------------------
            qtime=input("SLIDE!")
            if qtime=="s":
                end=time.time()
            else:
                trise+=1
                break
            if end-start>3:
                print("the arrows hit you")
                trise+=1
                break
            print("you keep running")
            
            time.sleep(2)
            #go left---------------------
            print("a saw comes from the right wall")
            start=time.time(1)
            qtime=input("GO LEFT!")
            if qtime=="a":
                end=time.time()
            else:
                trise+=1
                break
            if end-start>3:
                print("the saw hit you")
                trise+=1
                break
            time.sleep(2)
            #jump + wall hole
            print("a massive hole opens in the right wall")
            print("but lava flows onto the floor")
            time.sleep(2)
            start=time.time()
            qtime=input("JUMP")
            end=time.time
            if qtime=="w"or qtime=="d":
                end=time.time()
            else:
                trise+=1
                break
            if end-start>3:
                print("the saw hit you")
                trise+=1
                break
            if qtime=="d":
                #skip----
                time.sleep(1)
                print("you jump into the hole and hide")
                print("voice-'HEY WHERE DID YOU GO!'")
                time.sleep(1)
                print("you walk through the hole and find yourself at the exit door of the hall")
                time.sleep(1)
                print("looks like you skipped some of the traps")
                enddd=True
                break
            
            time.sleep(1) 
            print("you keep running")
            print("spikes come down from the roof")
            #slide
            time.sleep(2)
            start=time.time()
            qtime=input("SLIDE!")
            if qtime=="s":
                end=time.time()
            else:
                trise+=1
                break
            if end-start>3:
                print("the spikes hit you")
                trise+=1
                break
            print("you keep running and a skeleton jumps at you")
            #small fight
            maxmonshp=100
            tempmonsdmg=20
            fight()
            if hp==0:
                lvl=c1()
                return
            print("you finaly make it out of the hallway")
            enddd=True
            break
    if trise>3:
        print("you died")
        lvl=c1()
        return
    else:
        print("you make it out of the hall")
        lvl=w1l5
            
            
        






#skeledongeon mid------------------------------------------------
def w1l3():
    global hp
    global inv
    global stuff
    global spellbook
    global gend
    global gp
    global maxmonshp
    global tempmonsdmg
    global atkefx
    global hfbomb
    global mp
    print("the door opens as soon as you unlock it")
    print("you see a green needle and use it")
    time.sleep(1)
    print("healed")
    hp=maxhp
    print("you also see a blue needle and use it")
    print("mp+100")
    mp+=100
    time.sleep(2)
    print("you see another door and walk towards it")
    print("you get closer and hear load yelling")
    time.sleep(1)
    print("you see light coming from under the door")
    print("you get close to it and it slams open")
    time.sleep(3)
    print("you see a masive arena")
    print("you look up and see stands full of skeletons cheering")
    print("on the other side of the arena you see a massive skeleton")
    time.sleep(4)
    print("you lock eyes with the masive skeleton")
    maxmonshp=500
    tempmonsdmg=40
    print("THE FIGHT BEGINS")
    fight()
    if hp==0:
        return
    print("you deal the final blow knocking the mess of bones to the ground")
    time.sleep(1)
    print("you take its sword and stab it in the head")
    time.sleep(1)
    print("the skeletons in the stands start cheering for you")
    print("+50gp +skeleton sword")
    gp+=50
    inv.append("skeleton sword")
    time.sleep(2)
    print("new item:**skeleton sword**")
    time.sleep(2)
    print("you look at the dead skeleton on the ground then look up and all the skeletons in the stands are gone")
    time.sleep(2)
    print("you look around everywhere but cant see anything")
    time.sleep(1)
    print("bricky come out from you pocket to help you")
    time.sleep(1)
    print("brikcy- huh looks like your stuck")
    time.sleep(1)
    print("bricky-try climbing up one of the walls maybe")
    time.sleep(1)
    print("you walk towards the wall but a door opens at the end of the arena")
    print("you hear a voice over a speaker")
    time.sleep(2)
    print("voice-'i see, you have killed the first gladiator'")
    time.sleep(1)
    print("voice-'impresive'")
    time.sleep(2)
    print("voice-'how about you come to just i already opened the door for you'")
    time.sleep(2)
    w1l3q=input("do you want to climb the wall(1) or go to the door(2)")
    if w1l3q=="1":
        lvl=w1l4a
    else:
        lvl=w1l4
        #work here
    
    
    
    







#skeledongeon start----------------------------------
def w1l2():
    global hp
    global inv
    global stuff
    global spellbook
    global gend
    global gp
    global maxmonshp
    global tempmonsdmg
    global atkefx
    global hfbomb
    global shpp
    global mp
    print("you walk down the stairs")
    print("you get to the bottom and you see prison cells lining the walls.")
    time.sleep(2)
    print("you look around the hallway")
    findranw1l2=random.randint(1,6)
    if findranw1l2>=4:
        print("you see a hellfire bomb in the corner of the room")
        time.sleep(1)
        hfbomb+=1
        if "hellfire bomb"not in inv:
            inv.append("hellfire bomb")
    time.sleep(2)
    print("you walk down the hall")
    print("you get to a part where the prison cells end and it is almost pitch black")
    time.sleep(2)
    print("you keep walking and you start to see skeletons on the ground")
    time.sleep(2)
    print("you see a locked door and a key in a skeletons hand")
    time.sleep(3)
    print("you go to pick it up but the skeletons start to stand up")
    #skeleskip
    if hfbomb>=1:
        print("you pull out a hellfire bomb and throw it at all of the skeletons")
        print("they all burn and run away")
    else:
        #fight
        print("fight time")
        maxmonshp=50
        tempmonsdmg=30
        fight()
        if hp==0:
            lvl=c1()
            return
        print("another skeleton comes up to you")
        time.sleep(2)
        maxmonshp=50
        tempmonsdmg=30
        fight()
        if hp==0:
            lvl=c1()
            return
        print("one more come at you but this one as a torch")
        time.sleep(1)
        maxmonshp=200
        tempmonsdmg=30
        atkefx="fire"
        fight()
        if hp==0:
            lvl=c1()
            return
        time.sleep(2)
        print("after you kill the 3 all of the others run")
        print("+100gp +torch")
        time.sleep(2)
        inv.append("torch")
        print("you also find 2 small hp potions")
        shpp+=2
    print("you take the key and unlock the door.....")
    time.sleep(2)
    lvl=w1l3





#world1 lvl1------------------------------------------------
def w1l1():
    global hp
    global inv
    global stuff
    global spellbook
    global gend
    global gp
    global maxmonshp
    global tempmonsdmg
    print("you walk out of the diner into a forest of massive redwood trees")
    print("you look aroud and see some sort of ruins in the distance")
    print("you walk towards it")
    time.sleep(1)
    print("you see two small hodded figures searching the ruins")
    print("it does not see you")
    w1l1q=input("do you want to fight it(1) or hide(2)(if invaild it will do 1)")


    if w1l1q=="1":
        #kill
        print("you charge the hodded figures knife in hand")
        print("they see you and prepare for battle")
        print("*epic battle music*")
        maxmonshp=100
        tempmonsdmg=10
        fight()
        if hp==0:

            lvl=c1()
            return
        print("you kill one")
        print("the other one attacks you but this one looks stonger")
        maxmonshp=150
        tempmonsdmg=30
        fight()
        if hp==0:
            lvl=c1()
            return
        print("you kill both")
        print("you see they have a lot of gold +60 gp")
        gp+=60
        print("you search their body and find a pulsating blue stone")
        stuff.append("bluestone")
        time.sleep(3)



        
    elif w1l1q=="2":
        #hide
        gend+=1
        print("you hide from them but they see you")
        print("they walk up to you and greet you")
        time.sleep(1)
        print("you ask them what they are doing and they")
        print("hodded figure-'hi my name is alexia and this is my friend nicole")
        #credits to ramiro for the names
        time.sleep(2)
        print("alexia-'we are looking for some of these stones'")
        print("*they show you a blue stone*")
        time.sleep(1)
        print("nicole- 'its very nice to find some that does not try and fight us every time they see us'")
        print("alexia-'yes its very rare in these lands'")
        time.sleep(1)
        print("alexia-'here take this as a gift of your appreciation'")
        print("*blue stone* addded to stuff inv")
        time.sleep(1)
        stuff.append("bluestone")
        time.sleep(3)
        
    else:
        #kill
        print("you charge the hodded figures knife in hand")
        print("they see you and prepare for battle")
        print("*epic battle music*")
        maxmonshp=100
        tempmonsdmg=10
        fight()
        if hp==0:
            return
        print("you kill one")
        print("the other one attacks you but this one looks stonger")
        maxmonshp=150
        tempmonsdmg=30
        fight()
        if hp==0:
            lvl=c1()
            return
        time.sleep(1)
        print("you kill both")
        print("you see they have a lot of gold +60 gp")
        gp+=60
        print("you search their body and find a pulsating blue stone")
        time.sleep(1)
        stuff.append("bluestone")
        time.sleep(3)
        #transfer to next lvl
    print("you look at the ruins and find a small hole covered in rocks.")
    time.sleep(1)
    print("you move the rocks to uncover the hole.")
    time.sleep(1)
    print("once you finish moving the rocks you find the hole is actualy")
    time.sleep(2)
    print("a broken trap leading to a staircase")
    print("you go down")
    
    time.sleep(2)
    lvl=w1l2
        
              

        
#CHECKPOINT 1------------------------------------------------
def c1():
    global hp
    global inv
    global stuff
    global spellbook
    global armor
    global maxhp
    global magicrobe
    global mp   
    global gp
    global roknum
    global shpp
    global mhpp
    global lhpp
    global mpp
    global mcslvl
    global mcsnum
    global savepoint
    global w1l1
    global gend
    global hfbomb
    global lvl
    global checkpoint
    #saving start
    checkpoint=c1
    if hp<=0:
        print("items set back to what you had when you saved")
        inv=tempinv
        stuff=tempstuff
        spellbook=tempspellbook
        armor=temparmor
        maxhp=tempmaxhp
        magicrobe=tempmagicrobe
        mp=tempmp
        hp=temphp
        gp=tempgp
        roknum=temproknum
        shpp=tempshpp
        mhpp=tempmhpp
        lhpp=templhpp
        mpp=tempmpp
        hfbomb=temphfbomb
        mcsnum=tempmcsnum
        mcslvl=tempmcslvl
        gend=tempgend
       
    print("checkpoint 1")
    print("game saved")
    tempmcslvl=mcslvl
    tempmcsnum=mcsnum
    temphfbomb=hfbomb
    tempinv=inv
    tempstuff=stuff
    tempspellbook=spellbook
    temparmor=armor
    tempmaxhp=maxhp
    tempmagicrobe=magicrobe
    tempmp=mp
    temphp=hp
    tempgp=gp
    temproknum=roknum
    tempshpp=shpp
    tempmhpp=mhpp
    templhpp=lhpp
    tempmpp=mpp
    tempgend=gend

    #do the json stuff here------------------------------------------
    effects=None
    print("c1")
    time.sleep(1)
    saving(filenameee)
    json.dump(saving(filenameee))
    
    if savepointt==True:
        print("savepoint",savepoint)
    else:
        print("checkpoint=c1")
    #saving end
    print()
    print()
    print()
    print("hp healed")
    hp=maxhp
    print("you look around and see a shop, a doorway out, and a old lady")
    question=input("what would you like to do(1=oldlady,2=shop,3=leave")
    while question!="3":

        if question=="1":
            print("you walk up to the old lady")
            print("-'hello sir'")
            print("-'thank you for saving us and the diner'")
            print("-'take this old book as a gift'")
            print("**spell book unlocked**")
            print("**big rock spell unlocked**")
            if spellbook not in inv:
                print(inv.append("spellbook"))
            else:
                print("items got already")


                
            question=input("what would you like to do(1=oldlady,2=shop,3=leave")
        elif question=="2":
            #shop
            print("you go to the shop")
            time.sleep(2)
            shopc1=None
            while shopc1!="leave":
                print()
                print("you have",gp,"gp")
                print("---------------------------------")
                print("rok-300gp for 1")
                
                print("diamond sword-100gp")
                if "diamond sword" in inv:
                    print("upgrade sword-",mcslvl,"gp")
                print("hellfire bomb-50gp for 1")
                
                print("bat-60gp")
                
                print("pistol-100gp")
                
                print("small hp potion(type shpp)-30gp")
                
                print("magic power potion (type mpp)-20gp")
                
                print("zuzus mask(maxhp=200)-100gp")
                #input
                shopc1=input("what would you like to buy(type leave if you want to leave the store)")
                if shopc1=="rok":
                    if gp>=300:
                        roknum+=1
                        gp-=300
                        print("+1 roks u have",roknum,"roks")
                    else:
                        print("too broke L")
                elif shopc1=="diamond sword":
                    if "diamond sword" not in inv:
                        if gp>=100:
                            print("you bought a diamond sword")
                            gp-=100
                            inv.append("diamond sowrd")
                            mcslvl=150
                            mcsnum=2
                        else:
                            print("to broke")
                            #sword upgrade
                elif shopc1=="upgrade sowrd":
                    if gp>=mcslvl:
                        if mcsnum==2:
                            print("iron sword bought")
                            gp-=mcslvl
                            inv.append("iron sword")
                            mcslvl=600
                            mcsnum=3
                            
                        elif mcsnum==3:
                            print("stone sword bought")
                            gp-=mcslvl
                            inv.append("stone sword")
                            mcslvl=1600
                            mcsnum=4
                            
                        elif mcsnum==4:
                            print("wood sword bought")
                            gp-=mcslvl
                            inv.append("wood sword")
                            mcslvl=3500
                            mcsnum=5
                            
                        elif mcsnum==5:
                            print("you pay for a upgrade but your sword does not change")
                            gp-=mcslvl
                            time.sleep(2)
                            print("you start to walk away but then a blinding light comes from the sword")
                            print("the sword shines with a pulsating purple light")
                            inv.append("shiny wood sword")
                            print("sword maxxed")
                            mcslvl="max"
                            mcsnum="max"
                            
                        else:
                            print("invalid (or max)")
                    else:
                        print("toooooo broke l")
                        #hellfire bomb
                elif shopc1=="hellfire bomb":
                    if gp>=50:
                        print("hellfire bomb bought")
                        gp-=50
                        hfbomb+=1
                        print("you have",hfbomb,"hellfire bombs")
                        if "hellfire bomb"not in inv:
                            inv.append("hellfire bomb")
                        
                    else:
                        print("you too broke L")
                        #bat
                        
                elif shopc1=="bat":
                    if gp>=60:
                        print("you bought a bat BONK")
                        gp-=60
                        inv.append("bat")

                    else:
                        print("toooo broke L")
                    #pistol
                elif shopc1=="pistol":
                    if gp>=100:
                        print("you got a gun")
                        print("uh oh")
                        gp-=100
                        inv.append("pistol")
                    else:
                        print("tooo broke")
                        #shpp
                elif shopc1=="shpp":
                    if gp>=30:
                        print("small hp potion bought")
                        gp-=30
                        shpp+=1

                    else:
                        print("too broke L")
                        #mpp
                elif shopc1=="mpp":
                    if gp>=20:
                        print("magic power potion bought")
                        gp-=20
                        mpp+=1
                    else:
                        print("tooooooo broke")
                        #zuzus mask
                elif shopc1=="zuzus mask":
                    if gp>=100:
                        print("you bought zuzus mask max hp=200:")
                        armor="zuzus mask"
                        maxhp=200
                    else:
                        print("tooooo broke")
            question=input("what would you like to do(1=oldlady,2=shop,3=leave")
        else:
            print("invaild num")
            question=input("what would you like to do(1=oldlady,2=shop,3=leave")
                        
    if question=="3":
        print("you walk out of the dinner")
        if savepointt==True:
            lvl=savepoint
            saving(filenamee)
        else:
            lvl=w1l1
            saving(filenamee)
        
                
                        






    
    

    

#start--------------------------------------------------------------------------------------------------------------
print("=====================================================================")
print("                  =======   ||  ||   ||=====")
print("                    ||      ||  ||   ||")
print("                    ||      ||==||   ||===")
print("                    ||      ||  ||   ||")
print("                    ||      ||  ||   ||=====")
print("                        ADVENTURES OF")
print("/==========\\       ||        ||     /==========\\      ||        ||")
print("|                  ||        ||     |                 ||        ||")
print("|                  ||        ||     |                 ||        ||")
print("|    ======\\       ||        ||     |   ======\\       ||        ||")
print("|           \\      ||        ||     |          \\      ||        ||")
print("\\==========//      \\========//     \\==========//      \\========//")



#dialogue1------------------------------------------------------------------------------------------------------------
gamesavelol=input("do you have a save file(yes or no)")
if gamesavelol=="yes":
    gamesaveloll=input("what save file(1,2,3)")
    loadingggg=True
    if gamesaveloll=="1":
        filenameee="hehehehaw.json"
    elif gamesaveloll=="2":
        filenameee="hawhawhawhe.json"
    elif gamesaveloll=="3":
        filenameee="ehehehwah.json"
    loading(filenameee)
    
        
        
savefile=input("what file do you want to save to(1,2,or 3)")
if savefile=="1":
    filenameee="hehehehaw.json"
elif savefile=="2":
    filenameee="hawhawhawhe.json"
elif savefile=="3":
    filenameee="ehehehwah.json"
        
saving(filenameee)




#FIX AND CHECK RETRUN!!!!________________________________
if loadingggg==False:
    print("you wake up in a diner with a bunch of food that has been eaten on your plate.")
    print()
    print("you see the waiter coming towards you for the bill, but when you go to grab some money you relize you are broke :(")
    print()
    print("(any question anwser in yes or no, unless asked to awnser a diffrent way)")
    print()
    time.sleep(1)
    print("your inv will show during fights it will also show you mp(magic power) healing potions and mp potions")
    print()
    print("how to play (fights): in a fight you will shown actions that you can do pick one by typing it EXACTLY how it is in your inv.")
    print("SHOPS: at a shop you will be told what you can buy and how much it costs")
    print()
    time.sleep(1)
    print("at checkpoints or savepoints you can teleport to checkpoints ( you can also do this in a checkpoint)")
    print("you can type leave while at a checkpoint you teleported too if you want to go back")
    print()
    start=None
    while start!="start":
        start=str(input("enter 'start' when ready"))
    print()
    print("continuing")
    time.sleep(1)
    print("the waiter comes up to you and asks you to pay but you tell him you are broke")
    print("he looks away from you and looks back now holding a massive hammer!!!!")
    print("The fight begins")
    print()
    print()
    print()
    #first fight-----------------------------------------------------------------------------------------------------------
    maxmonshp=300
    tempmonsdmg=30
    fight()
    if hp==0:
        exit
        

    #end of fight-----------------

    time.sleep(1)
    print("another waiter comes up to you.")
    print("thank you for killing that waiter he was very mean")
    print()
    time.sleep(1)
    print("your rewards-50 gold")
    gp+=50
    print("you look at the body you see 2 items a hammer and a white shirt")
    opt1=str(input("what do you take: hammer or white shirt"))
    print()
    if opt1=="hammer":
        inv.append("hammer")
    elif opt1=="white shirt":
        armor="white shirt"
        maxhp=150
        print("hp = 150 armor(white shirt)")
    else:
        print("invaild item stupid")
        print()
    print()
    print("you take your rewards and when u stand up a brick hit you on the head")
    time.sleep(2)
    print()
    print("you pick up the brick and when you are about to throw it, it starts to talk")
    print()
    time.sleep(1)
    print("bricky-'hi my name is bricky, bricky the brick i saw you fight the enemy and now im here to help'")
    time.sleep(2)
    print()
    print("bricky- 'i will help you out in hard places or tell you what to do at some points'")
    time.sleep(1)
    print()
    print("bricky- 'but now let me fix up this place'")
    time.sleep(4)
    print()
    print("bricky jumps out of your hands and runs around fixing the old diner")
    print("the diner is fully fixed with a store and everything")
    time.sleep(2)
    print()
    print("------------------------------------------------------------")
    print("------------------checkpoint 1 reached---------------------")
    print("------------------------------------------------------------")
    checkpoint=c1
    lvl=c1
else:
    print("loading")
if savepointt==True:
    lvl=savepoint
else:
    lvl=checkpoint
while loop==True:
    lvl()


    
    
    
        
          

 










#mr.snake
#   V
#  /^\
# /o o\
#  (})
#  (})
#  (})
#  (})
#  (})
#  (})
#  (})
#  (})
#  (})
#  (})
#  \}/
#   V
#   V
#   Y
