import random

name=input('What is your name? ')
print()

print('Hello', name,'!')
print('''Welcome to ANAGRAM!

How to play:
You can pick the topic.
You will be given jumbled words from the topic and you will have to figure out what the word is.
You will be given five words and you have three chances to get each of them right.
If you want to skip to the next word, enter the character \'s\' or \'S\'.
ALL THE BEST!''')

print()

x='yes'

while x=='Yes' or x=='yes' or x=='YES' or x=='y' or x=='Y':
    print()
    topic=int(input('''These are your topics:
1. Countries
2. Animals
3. Famous personalities
4. Cars
5. Celestial Bodies
6. Business Companies
7. Electronic Gadgets/Applianaces
8. Books (Classics)
9. Flowers
10. Elements from the Periodic Table

Enter the number corresponding to the topic you want to choose: '''))

    print()

    lod=input('''Choose level of difficulty:
a)Easy
b)Hard

Enter (a) or (b):''')

    if topic==1:
        wordsdict1={1:['INDIA', 'The most populous democracy in the world.'],2:['SPAIN', 'Famous for \'La Siesta\'.'],3:['IRELAND', 'Best known for the fabled tiny Leprechauns.'],4:['AUSTRALIA', 'Best known for its beaches, reefs and outback.'],5:['SOUTH AFRICA', 'Well known for ridding itself of the apartheid regime.'],6:['CANADA', 'Widely known for its hockey, maple syrup and brutally cold winters.'],7:['UNITED KINGDOM', 'Famous for its long history and its Royal Family.'],8:['RUSSIA','First to send a man into the outer space.'],9:['IRAN','Poetry holds a special place in this culture.'],10:['CHINA', 'Known as the \'Factory of the World\'.']}
        wordsdict2={1:['BULGARIA'],2:['BOLIVIA'],3:['LITHUANIA'],4:['LUXEMBURG'],5:['CAMBODIA'],6:['TURKMENISTAN'],7:['SOMALIA'],8:['SLOVENIA'],9:['KYRGYSTAN'],10:['CROATIA']}
    elif topic==2:
        wordsdict1={1:['TIGER', 'Striped animal.'],2:['ELEPHANT','Heaviest terrestrial animal.'],3:['MONKEY','Fabled to imitate anything you do.'],4:['CHIMPANZEE','Share about 95-98 % of DNA with humans.'],5:['GORILLA','One of the biggest, most powerful living primates.'],6:['ZEBRA','A group is called a Dazzle.'],7:['LEOPARD','Fast felines that can run upto 58 km/h!'],8:['KANGAROO', 'Carries their kids in a pouch.'],9:['JELLYFISH', 'No brain, heart, bones or eyes!'],10:['WALRUS', 'Both the male and female of the species have large tusks.']}
        wordsdict2={1:['IGUANA','Large, tree-climbing lizards.'],2:['COYOTE','Wild dog that resembles a wolf.'],3:['ARMADILLO', 'Rolls itself into a ball to protect itself.'],4:['BANDICOOT','Known to dig small, conical holes in lawns or gardens.'],5:['BADGER', 'Their home is called a sett.'],6:['ANTELOPE', 'Have extremely developed senses to detect predators and are quick runners.'],7:['MACAQUE', 'Primates that possess large cheek pouches to carry extra food.'],8:['BOA CONSTRICTOR', 'Large, non-venomous, heavy-bodied snake often kept and bred in captivity.'],9:['PORCUPINE', 'Huge quills all over its body for protection.'],10:['VIPER', 'Venomous snakes that have long, hinged fangs that permit deep penetration and injection of venom.']}
    elif topic==3:
        wordsdict1={1:['ALBERT EINSTEIN'],2:['MARTIN LUTHER KING'],3:['J K ROWLING'],4:['ABRAHAM LINCOLN'],5:['NEIL ARMSTRONG'],6:['FRANKLIN D ROOSEVELT'],7:['NELSON MANDELA'],8:['JANE AUSTEN'],9:['ADOLF HITLER'],10:['JOHN F KENNEDY']}
        wordsdict2={1:['VLADIMIR PUTIN'],2:['CHRISTOPHER COLUMBUS'],3:['GEORGE WASHINGTON'],4:['MARYLIN MONROE'],5:['WINSTON CHURCHILL'],6:['MARGARET THATCHER'],7:['LUDWIG BEETHOVEN'],8:['PABLO PICASSO'],9:['AMELIA EARHART'],10:['GRETA THUNBERG']}
    elif topic==4:
        wordsdict1={1:['MARUTI SUZUKI'],2:['TOYOTA'],3:['HONDA'],4:['BENTLEY'],5:['NISSAN'],6:['CHRYSLER'],7:['SKODA'],8:['CHEVROLET'],9:['DODGE'],10:['MERCEDES']}
        wordsdict2={1:['BUICK'],2:['MITSUBISHI'],3:['ALFA-ROMEO'],4:['CADILLAC'],5:['LAMBORGHINI'],6:['CITROEN'],7:['PONTIAC'],8:['SUBARU'],9:['VOLKSWAGEN'],10:['BUGATTI']}
    elif topic==5:
        wordsdict1={1:['JUPITER'],2:['GANYMEDE'],3:['EARTH'],4:['VENUS'],5:['MERCURY'],6:['CERES'],7:['ERIS'],8:['ANDROMEDA GALAXY'],9:['HALEY\'S COMET'],10:['SIRIUS']}
        wordsdict2={1:['ENCELADUS'],2:['MIMAS'],3:['DIONE'],4:['IAPETUS'],5:['HYPERION'],6:['CALYPSO'],7:['TRITON'],8:['NEREID'],9:['PROTEUS'],10:['GALATEA']}
    elif topic==6:
        wordsdict1={1:['COCA COLA'],2:['PEPSI'],3:['APPLE'],4:['AMAZON'],5:['MICROSOFT'],6:['WALMART'],7:['BIG BAZAR'],8:['GOOGLE'],9:['FACEBOOK'],10:['JOHNSON & JOHNSON']}
        wordsdict2={1:['HILTON'],2:['SAMSUNG ELECTRONICS'],3:['VERIZON COMMUNICATIONS'],4:['SIEMENS'],5:['UNILEVER'],6:['HITACHI'],7:['PHILIPS'],8:['TARGET'],9:['MCDONALD\'S'],10:['PANASONIC']}
    elif topic==7:
        wordsdict1={1:['FAX'],2:['COMPUTER'],3:['CAMERA'],4:['TELEVISION'],5:['LAPTOP'],6:['TABLET'],7:['PRINTER'],8:['RADIO'],9:['DVD PLAYER'],10:['REMOTE CONTROL']}
        wordsdict2={1:['DRONE'],2:['PAGER'],3:['EARPHONES'],4:['HEADPHONES'],5:['CHARGER'],6:['KEYBOARD'],7:['MOBILE PHONE'],8:['SPEAKER'],9:['PLAYSTATION'],10:['AIR CONDITIONER']}
    elif topic==8:
        wordsdict1={1:['PRIDE AND PREJUDICE'],2:['ANNE OF GREEN GABLES'],3:['GREAT EXPECTATIONS'],4:['A TALE OF TWO CITIES'],5:['TO KILL A MOCKINGBIRD'],6:['RAILWAY CHILDREN'],7:['LITTLE WOMEN'],8:['JANE EYRE'],9:['THE GREAT GATSBY'],10:['WUTHERING HEIGHTS']}
        wordsdict2={1:['ANNA KARENINA'],2:['THE WIND IN THE WILLOWS'],3:['DORIAN GRAY'],4:['THE MAYOR OF CASTERBRIDGE'],5:['THE CALL OF THE WILD'],6:['LORD OF THE FLIES'],7:['CHARLOTTE\'S WEB'],8:['JAMAICA INN'],9:['LORNA DOONE'],10:['ONE HUNDRED YEARS OF SOLITUDE']}
    elif topic==9:
        wordsdict1={1:['HIBISCUS'],2:['CHRYSANTHAMUM'],3:['LILY'],4:['PETUNIA'],5:['BLUEBELL'],6:['DAFFODIL'],7:['TULIP'],8:['ROSE'],9:['SUNFLOWER'],10:['JASMINE']}
        wordsdict2={1:['CORPSE FLOWER'],2:['LADY\'S SLIPPER ORCHID'],3:['CHOCOLATE COSMOS'],4:['MIDDLEMIST\'S RED'],5:['FRANKLIN TREE FLOWER'],6:['KADUPUL FLOWER'],7:['COOKE\'S KOKIO'],8:['PARROT\'S BEAK'],9:['ROTHSCHILD\'S SLIPPER ORCHID'],10:['JULIET ROSE']}
    elif topic==10:
        wordsdict1={1:['SILICON'],2:['GERMANIUM'],3:['ARSENIC'],4:['LEAD'],5:['BORON'],6:['BERYLLIUM'],7:['LITHIUM'],8:['CADMIUM'],9:['NEON'],10:['CHLORINE']}
        wordsdict2={1:['MOSCOVIUM'],2:['HAFNIUM'],3:['ASTATINE'],4:['RHODIUM'],5:['POLONIUM'],6:['ACTINIUM'],7:['RUTHERFORDIUM'],8:['TANTALUM'],9:['EUROPIUM'],10:['NIOBIUM']}

    print()

    Lkeys=[]

    i=0
    score=0
    while i<5:
        if lod=='a' or lod=='A':
            wordsdict=wordsdict1
        elif lod=='b' or lod=='B':
            wordsdict=wordsdict2
        key=random.randint(1,10)
        if key not in Lkeys:
            word=wordsdict[key][0]
            Lkeys+=[key]
            wordshuff=word
            while wordshuff==word:
                splitwrd=word.split()
                L=[]
                for k in splitwrd:
                    x=k
                    if len(k)!=1:
                        while x==k:
                            l=list(k)
                            random.shuffle(l)
                            x=''.join(l)
                    L+=[x]
                wordshuff=' '.join(L)
            print(wordshuff)
            ctr=0
            while ctr<3:
                ans=input('Enter your answer: ')
                if ans==word.upper() or ans==word.lower():
                    if (lod=='a' or lod=='A') and ctr==0:
                        score+=30
                    elif (lod=='b' or lod=='B')and ctr==0:
                        score+=60
                    elif (lod=='a' or lod=='A') and ctr==1:
                        score+=20
                    elif (lod=='b' or lod=='B') and ctr==1:
                        score+=40
                    elif (lod=='a' or lod=='A') and ctr==2:
                        score+=10
                    elif (lod=='b' or lod=='B') and ctr==2:
                        score+=20
                    elif (lod=='a' or lod=='A') and ctr==2 and h in ('Yes','yes','YES','y','Y'):
                        score+=5
                    elif (lod=='b' or lod=='B') and ctr==2 and h in ('Yes','yes','YES','y','Y'):
                        score+=10

                    break
                elif ans=='s' or ans=='S':
                    ctr=3
                    print('The answer is', word)
                else:
                    if ctr<2:
                        print('Oops! Your answer is wrong. Try again!')
                        ctr+=1
                        if ctr==2:
                            h=input('Would you like a hint? (y/n)')
                            if h in ('Yes','yes','YES','y','Y'):
                                hint=wordsdict[key][1]
                                print(hint)
                    else:
                        print('Sorry! You got it wrong! The correct word is', word)
                        print('Let\'s move on to the next word')
                        break
        else:
            i-=1
        i+=1
    else:
        if lod in 'aA':
            print('Game over! Your score is', score,'/150')
        elif lod in 'bB':
            print('Game over! Your score is', score,'/300')



    print()
    x=input('Would you like to play again? (Yes/No) ')
