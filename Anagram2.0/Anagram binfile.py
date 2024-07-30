import pickle

with open(r'WordsCountries.dat','wb') as f:
    easywords={1:['INDIA', 'The most populous democracy in the world.'],2:['SPAIN', 'Famous for \'La Siesta\'.'],3:['IRELAND', 'Best known for the fabled tiny Leprechauns.'],4:['AUSTRALIA', 'Best known for its beaches, reefs and outback.'],5:['SOUTH AFRICA', 'Well known for ridding itself of the apartheid regime.'],6:['CANADA', 'Widely known for its hockey, maple syrup and brutally cold winters.'],7:['UNITED KINGDOM', 'Famous for its long history and its Royal Family.'],8:['RUSSIA','First to send a man into the outer space.'],9:['IRAN','Poetry holds a special place in this culture.'],10:['CHINA', 'Known as the \'Factory of the World\'.']}
    diffwords={1:['BULGARIA', 'The only European country that hasn\'t changed its name since being established'],2:['BOLIVIA', 'Home to two of the highest cities in the world!'],3:['LITHUANIA', 'The people here celebrate two independence days!'],4:['LUXEMBOURG','The second richest country in the world!'],5:['CAMBODIA', 'The flag of this country is the only one in the world to feature a building.'],6:['TURKMENISTAN', 'One of the least visited countries of the world that is 70% desert!'],7:['SOMALIA', 'The people here are divided into numerous clans that trace their common ancestry back to a single father.'],8:['SLOVENIA', 'A country where 1 in 20 people keep bees!'],9:['KYRGYZSTAN', 'Its name is thought to be derived from the Turkic word for \'forty\''],10:['CROATIA', 'This country invented the necktie.']}

    pickle.dump(easywords, f)
    pickle.dump(diffwords, f)

with open(r'WordsAnimals.dat','wb') as f:
    easywords={1:['TIGER', 'Striped animal.'],2:['ELEPHANT','Heaviest terrestrial animal.'],3:['MONKEY','Fabled to imitate anything you do.'],4:['CHIMPANZEE','Share about 95-98 % of DNA with humans.'],5:['GORILLA','One of the biggest, most powerful living primates.'],6:['ZEBRA','A group is called a Dazzle.'],7:['LEOPARD','Fast felines that can run upto 58 km/h!'],8:['KANGAROO', 'Carries their kids in a pouch.'],9:['JELLYFISH', 'No brain, heart, bones or eyes!'],10:['WALRUS', 'Both the male and female of the species have large tusks.']}
    diffwords={1:['IGUANA','Large, tree-climbing lizard.'],2:['COYOTE','Wild dog that resembles a wolf.'],3:['ARMADILLO', 'Rolls itself into a ball to protect itself.'],4:['BANDICOOT','Known to dig small, conical holes in lawns or gardens.'],5:['BADGER', 'Their home is called a sett.'],6:['ANTELOPE', 'Have extremely developed senses to detect predators and are quick runners.'],7:['MACAQUE', 'Primates that possess large cheek pouches to carry extra food.'],8:['BOA CONSTRICTOR', 'Large, non-venomous, heavy-bodied snake often kept and bred in captivity.'],9:['PORCUPINE', 'Huge quills all over its body for protection.'],10:['VIPER', 'Venomous snakes that have long, hinged fangs that permit deep penetration and injection of venom.']}

    pickle.dump(easywords, f)
    pickle.dump(diffwords, f)

with open(r'WordsFamousPersonalities.dat','wb') as f:
    easywords={1:['ALBERT EINSTEIN', 'Scientist known for the Theory of Relativity.'],2:['MARTIN LUTHER KING JR.', 'Famous for his speech, \'I Have a Dream\'.'],3:['J K ROWLING', 'British author famous for her 7 book children\'s fantasy series.'],4:['ABRAHAM LINCOLN', 'American statesman and lawyer that served as the 16th U.S. President.'],5:['NEIL ARMSTRONG', 'The firt person to walk on the moon.'],6:['ELEANOR ROOSEVELT', 'Human rights activist that was the longest-serving First Lady of the United States.'],7:['NELSON MANDELA', 'South Africa\'s first black President.'],8:['JANE AUSTEN', 'British novelist known for her works that explore the dependence of women on marriage.'],9:['ADOLF HITLER', 'German politician and leader of the Nazi party.'],10:['JOHN F KENNEDY', 'Served as U.S. President until his assassination November 1963.']}
    diffwords={1:['VLADIMIR LENIN', 'Leader of Russian Revolution 1917.'],2:['CHRISTOPHER COLUMBUS', 'Italian explorer and navigator who completed four voyages across the Atlantic Ocean.'],3:['GEORGE WASHINGTON', 'The 1st U.S. President.'],4:['CHARLES DARWIN', 'English Natural Scientist that laid down a framework for the \'Theory of Evolution\'.'],5:['WINSTON CHURCHILL', 'Former Prime Minister of the U.K. that successfully lead Britain through WWII.'],6:['MARGARET THATCHER', 'Longest-serving British Prime Minister of the 20th century and the first woman to hold that office, dubbed the \'Iron Lady\'.'],7:['LUDWIG BEETHOVEN', 'German composer and pianist, remains one of the most admired composers in the history of Western music.'],8:['PABLO PICASSO', 'Spanish painter, sculptor, printmaker, ceramicist and thetre designer whose most famous piece is the \'Guernica\'.'],9:['AMELIA EARHART', 'First female aviator to fly solo across the Atlantic Ocean.'],10:['GRETA THUNBERG', 'Swedish environmental activist who is internationally known for challenging world leaders to take immediate action against climate change.']}

    pickle.dump(easywords, f)
    pickle.dump(diffwords, f)

with open(r'WordsCars.dat','wb') as f:
    easywords={1:['MARUTI SUZUKI', 'Tagline: Way of Life!'],2:['TOYOTA', 'Tagline: Let\'s Go Places'],3:['HONDA', 'Tagline: The Power of Dreams'],4:['BENTLEY', 'Tagline: There\'s no replacement for displacement.'],5:['NISSAN', 'Tagline: Innovation that Excites.'],6:['CHRYSLER', 'Tagline: Inspiration comes Standard.'],7:['SKODA', 'Tagline: Simply Clever.'],8:['CHEVROLET', 'Tagline: Find New Roads.'],9:['DODGE', 'Tagline: Domestic. Not Domesticated.'],10:['MERCEDES', 'Tagline: The Best or Nothing.']}
    diffwords={1:['BUICK', 'Tagline: The New Symbol for Quality in America.'],2:['MITSUBISHI', 'Tagline: Drive your Ambition.'],3:['ALFA-ROMEO', 'Tagline: Beauty is not enough. Power for your control.'],4:['CADILLAC', 'Tagline: Creating a Higher Standard.'],5:['LAMBORGHINI', 'Tagline: Expect the Unexpected.'],6:['CITROEN', 'Tagline: Spirit of avant-garde.'],7:['PONTIAC', 'Tagline: We are driving excitement.'],8:['SUBARU', 'Tagline: Love is now bigger than ever.'],9:['VOLKSWAGEN', 'Tagline: Das Auto'],10:['BUGATTI', 'Tagline: Breaking New Dimensions']}

    pickle.dump(easywords, f)
    pickle.dump(diffwords, f)

with open(r'WordsCelestialBodies.dat','wb') as f:
    easywords={1:['JUPITER', 'The largest planet in the Solar System.'],2:['GANYMEDE', 'Largest of Jupiter\'s many moons.'],3:['EARTH', 'The Green Planet.'],4:['VENUS', 'Planet named after the Roman goddess of love and beauty.'],5:['MERCURY', 'Smallest planet in the Solar System.'],6:['CERES', 'Largest object in the main asteroid belt that lies between the orbits of Mars and Jupiter.'],7:['ERIS', 'Most massive and second-largest known dwarf planet in the Solar System.'],8:['ANDROMEDA GALAXY', 'Barred spiral galaxy which is the nearest major galaxy to the Milky Way.'],9:['HALEY\'S COMET', 'The only known short-period comet that is regularly visible to the naked eye from Earth.'],10:['SIRIUS', 'The brightest star in the night sky.']}
    diffwords={1:['ENCELADUS', 'The sixth-largest moon of Saturn.'],2:['MIMAS', 'Moon of Saturn which was discovered in 1789 by William Herschel.'],3:['DIONE', 'Moon of Saturn discovered by Italian astronomer Giovanni Domenico Cassini in 1684.'],4:['IAPETUS', 'The third-largest natural satellite of Saturn and the largest body in the Solar System known not to be in hydrostatic equilibrium.'],5:['HYPERION', 'Moon of Saturn which was the first non-round moon to be discovered.'],6:['CALYPSO', 'A Trojan (trailing moon) of the larger moon Tethys.'],7:['TRITON', 'The largest natural satellite of the planet Neptune.'],8:['NEREID', 'Neptune\'s third largest moon, with the most eccentric orbit in the Solar System.'],9:['PROTEUS', 'The second-largest Neptunian moon, and Neptune\'s largest inner satellite.'],10:['GALATEA', ' The fourth-closest inner satellite of Neptune.']}

    pickle.dump(easywords, f)
    pickle.dump(diffwords, f)

with open(r'WordsCompanies.dat','wb') as f:
    easywords={1:['COCA COLA', 'An American multinational beverage corporation incorporated under Delaware\'s General Corporation Law.'],2:['PEPSI', 'A carbonated soft drink manufactured by PepsiCo.'],3:['APPLE', 'An American multinational technology company that designs, develops and sells consumer electronics, computer software, and online services.'],4:['AMAZON', 'An American multinational technology company which focuses on e-commerce, cloud computing, digital streaming, and AI.'],5:['MICROSOFT', 'American multinational technology company that develops, manufactures, licenses, supports, and sells computer software, consumer electronics, personal computers, and related services.'],6:['WALMART', 'American multinational retail corporation that operates a chain of hypermarkets, discount department stores, and grocery stores.'],7:['BIG BAZAAR', 'Indian retail chain of hypermarkets, discount department stores, and grocery stores.'],8:['GOOGLE', 'American multinational technology company that specializes in Internet-related services and products, which include online advertising technologies, a search engine, cloud computing, software, and hardware.'],9:['FACEBOOK', 'American technology conglomerate founded by Mark Zuckerberg.'],10:['JOHNSON & JOHNSON', 'American multinational corporation that develops medical devices, pharmaceutical, and consumer packaged goods']}
    diffwords={1:['HILTON', 'American multinational hospitality company that manages and franchises a broad portfolio of hotels and resorts.'],2:['SAMSUNG ELECTRONICS', 'A major manufacturer of electronic components such as lithium-ion batteries, semiconductors, image sensors, camera modules and displays'],3:['VERIZON COMMUNICATIONS', 'American multinational telecommunications conglomerate and a corporate component of the Dow Jones Industrial Average.'],4:['SIEMENS', 'A German multinational conglomerate company headquartered in Munich and the largest industrial manufacturing company in Europe with branch offices abroad.'],5:['UNILEVER', 'British multinational consumer goods company headquartered in London, England.'],6:['HITACHI', 'Japanese multinational conglomerate company headquartered in Chiyoda, Tokyo, Japan.'],7:['PHILIPS', 'Formerly one of the largest electronics companies in the world, currently focused in the area of health technology, with other divisions being divested.'],8:['TARGET', 'An American retail corporation.'],9:['MCDONALD\'S', 'American fast food company.'],10:['PANASONIC', 'Japanese multinational electronics company, formerly known as the Matsushita Electric Industrial Co., Ltd.']}

    pickle.dump(easywords, f)
    pickle.dump(diffwords, f)

with open(r'WordsGadgets.dat','wb') as f:
    easywords={1:['FAX', 'Telephonic transmission of scanned printed material, normally to a telephone number connected to a printer or other output device'],2:['COMPUTER', 'A machine that can be instructed to carry out sequences of arithmetic or logical operations automatically.'],3:['CAMERA', 'Used to take photos and videos.'],4:['TELEVISION', 'Commonly known as the idiot-box.'],5:['LAPTOP', 'A portable computer.'],6:['TABLET', 'A small portable computer that accepts input directly on to its screen rather than via a keyboard or mouse.'],7:['PRINTER', 'A machine for printing text or pictures.'],8:['RADIO', 'An apparatus capable of both receiving and transmitting radio messages.'],9:['DVD PLAYER', 'A device that plays from a compact disc able to store large amounts of data.'],10:['REMOTE CONTROL', 'A device that controls an apparatus by means of radio or infrared signals.']}
    diffwords={1:['DRONE', 'An unmanned aerial vehicle.'],2:['PAGER', 'A wireless telecommunications device that receives and displays alphanumeric or voice messages.'],3:['EARPHONES', 'Small speakers placed inside the outer part of the ear canal.'],4:['HEADPHONES', 'Small speakers worn around the ears.'],5:['CHARGER', 'A device used to recharge a battery-powered equipment.'],6:['KEYBOARD', 'A typewriter-style device used to input data in a computer.'],7:['MOBILE PHONE', 'A portable telephone that can make and receive calls within a telephone service area.'],8:['SPEAKER', 'A device that helps to amplify sound.'],9:['PLAYSTATION', 'A type of games console.'],10:['AIR CONDITIONER', 'A device used to maintain a cool atmosphere in warm conditions.']}

    pickle.dump(easywords, f)
    pickle.dump(diffwords, f)

with open(r'WordsBooks.dat','wb') as f:
    easywords={1:['PRIDE AND PREJUDICE', 'An 1813 romantic novel of manners written by Jane Austen.'],2:['ANNE OF GREEN GABLES', 'A 1908 novel by Canadian author Lucy Maud Montgomery that follows the life of an imaginative red-head.'],3:['GREAT EXPECTATIONS', 'The thirteenth novel by Charles Dickens which depicts the education of an orphan nicknamed Pip.'],4:['A TALE OF TWO CITIES', 'An 1859 historical novel by Charles Dickens, set in London and Paris before and during the French Revolution.'],5:['TO KILL A MOCKINGBIRD', 'A novel by Harper Lee published in 1960.'],6:['RAILWAY CHILDREN', 'A children\'s book by Edith Nesbit, originally serialised in The London Magazine during 1905 and first published in book form in 1906.'],7:['LITTLE WOMEN', 'A coming-of-age novel written by American novelist Louisa May Alcott which was originally published in two volumes in 1868 and 1869.'],8:['JANE EYRE', 'A novel by English writer Charlotte Brontë about a girl that searches for a sense of being valued, of belonging.'],9:['THE GREAT GATSBY', 'A 1925 novel by American writer F. Scott Fitzgerald, set in the Jazz Age on Long Island.'],10:['WUTHERING HEIGHTS', 'A novel by Emily Brontë published in 1847 under her pseudonym, Ellis Bell.']}
    diffwords={1:['ANNA KARENINA', 'A novel by the Russian author Leo Tolstoy, first published in book form in 1878'],2:['THE WIND IN THE WILLOWS', 'A children\'s book by Scottish novelist Kenneth Grahame, first published in 1908.'],3:['THE PICTURE OF DORIAN GRAY', 'A Gothic and philosophical novel by Oscar Wilde, first published complete in the July 1890 issue of Lippincott\'s Monthly Magazine.'],4:['THE MAYOR OF CASTERBRIDGE', 'An 1886 novel by the English author Thomas Hardy.'],5:['THE CALL OF THE WILD', 'A short adventure novel by Jack London, published in 1903 and set in Yukon, Canada, during the 1890s Klondike Gold Rush, when strong sled dogs were in high demand.'],6:['LORD OF THE FLIES', 'A 1954 novel by Nobel Prize-winning British author William Golding that focuses on a group of British boys stranded on an uninhabited island and their disastrous attempt to govern themselves.'],7:['CHARLOTTE\'S WEB', 'A children\'s novel by American author E. B. White and illustrated by Garth Williams that tells the story of a livestock pig named Wilbur and his friendship with a barn spider named Charlotte.'],8:['JAMAICA INN', 'A novel by the English writer Daphne du Maurier, first published in 1936. '],9:['LORNA DOONE', 'A novel by English author Richard Doddridge Blackmore, published in 1869.'],10:['ONE HUNDRED YEARS OF SOLITUDE', 'A landmark 1967 novel by Colombian author Gabriel García Márquez that tells the multi-generational story of the Buendía family, whose patriarch, José Arcadio Buendía, founded the town of Macondo.']}

    pickle.dump(easywords, f)
    pickle.dump(diffwords, f)

with open(r'WordsFlowers.dat','wb') as f:
    easywords={1:['HIBISCUS', 'A large, trumpet-shaped flower without a scent.'],2:['POPPY', ''],3:['LILY', 'Flower that develops from a bulb that can be located near the surface of the ground.'],4:['PETUNIA', 'Usually 1 inch wide but of wide-ranging colours.'],5:['BLUEBELL', 'Narrow and tubular flowers shaped like a bell.'],6:['DAFFODIL', 'All parts of this plant contain a toxic chemical, lycorine.'],7:['TULIP', 'Large, showy and brightly coloured flowers that are usually red, pink, yellow or white.'],8:['ROSE', 'One of the oldest flowers, which is edible and used as fragrances.'],9:['SUNFLOWER', 'Flower whose head follows the direction of the sun.'],10:['JASMINE', 'Strong and sweet scented flowers commonly adorned by women in India.']}
    diffwords={1:['ORCHID', 'The largest family of flowering plants.'],2:['CARNATION', 'Edible flowers that can absorb any colour.'],3:['HYACINTH', 'Flower named after a young boy in Greek mythology that loved the god Apollo.'],4:['HYDRANGEA', 'Blue flowers that get their colour from the accumulation of Aluminium.'],5:['ANEMONE', 'Sea flower that has a ring of tentacles surrounding its central mouth.'],6:['CHRYSANTHEMUM', 'Edible plant first grown in China that has many different meanings.'],7:['FREESIA', 'Reknowned for its distinctive aroma and is used in the making of soaps and shampoos.'],8:['NARCISSUS', 'Name derived from the Greek word meaning numbness for its intoxicating fragrance.'],9:['BOUGAINVILLEA', 'The plants are made colourful by its magenta bracts, not its small white flowers!'],10:['BUTTERCUP', 'This poisonous flower has a layer of reflective cells that make it lustrous.']}

    pickle.dump(easywords, f)
    pickle.dump(diffwords, f)

with open(r'WordsElements.dat','wb') as f:
    easywords={1:['SILICON', 'Tetravalent metalloid and semiconductor whose oxide is found in sand.'],2:['GERMANIUM', 'Tetravalent semiconductor predominantly used in making alloys.'],3:['ARSENIC', 'Metalloid, long term exposure through water or food can cause cancer.'],4:['LEAD', 'Heavy metal that is denser than most materials.'],5:['BORON', 'Metalloid, which in the elemental state is found in meteroids.'],6:['BERYLLIUM', 'Usually occurs as a product of the spallation of larger atomic nuclei that have collided with cosmic rays.'],7:['LITHIUM', 'One of the three elements produced in large quantities by the Big Bang.'],8:['CADMIUM', 'Soft, silvery-white metal used in rechargeable batteries and as a corrosion-protection for iron and steel.'],9:['NEON', 'Noble gas used in fluoroscent lights.'],10:['CHLORINE', 'Yellow-green gas at room temperature that is used as a disinfectant.']}
    diffwords={1:['MOSCOVIUM', 'Radioactive, synthetic element used in the formation of other elements like Nihonium.'],2:['HAFNIUM', 'An element immediately after the split in the periodic table.'],3:['ASTATINE', 'Radioactive halide.'],4:['RHODIUM', 'Highly reflective silver-white metal that is resistant to corrosion and is the most valuable precious metal.'],5:['POLONIUM', 'A rare and highly volatile radioactive element used to remove dust from photographic film.'],6:['ACTINIUM', 'An element that glows in the dark due to its intense radioactivity and also functions as a neutron source.'],7:['RUTHERFORDIUM', 'An element named after a scientist that proposed one of the atomic models.'],8:['TANTALUM', 'Element named after a villain in Greek mythology who was punished by not being allowed to eat.'],9:['EUROPIUM', 'Most reactive lanthanide named after a continent.'],10:['NIOBIUM', 'Element that is used in alloys to strengthen them and has superconducting properties.']}

    pickle.dump(easywords, f)
    pickle.dump(diffwords, f)
