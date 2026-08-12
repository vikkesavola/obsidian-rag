from ask import search

test_set = [
  {"q": "how does a self-balancing tree stay balanced?",
   "notes": ["Atlas\\Notes\\AVL Tree.md"]},
  {"q": "How do signals travel in the human brain?",
   "notes": ["Atlas\\Notes\\Aivot.md", "Atlas\\Notes\\Hermosolut.md"]},
  {"q": "How do people stay motivated according to modern research?",
   "notes": ["Atlas\\Notes\\Itsemääräämisteoria (SDT).md"]},
  {"q": "Miksi signaalit eivät ole ikinä täydellisiä?",
   "notes": ["Atlas\\Notes\\Kohina.md"]},
  {"q": "How can I represent relationships between things as data?",
   "notes": ["Atlas\\Notes\\Relational data.md"]},
  {"q": "How does the human vision work?",
   "notes": ["Atlas\\Notes\\Näkö.md"]},
  {"q": "What does Tufte say about the relationship between the number of data entries and area?",
   "notes": ["Atlas\\Notes\\Tufte's theory of data graphics.md"]},
  {"q": "They injected something radioactive into my blood and scanned my brain. What were they doing?",
   "notes": ["Atlas\\Notes\\Tutkimusmenetelmät biologisessa psykologiassa.md"]},
  {"q": "What is it called when something in the background and I'm distracted by it?",
   "notes": ["Atlas\\Notes\\Visuaalinen tarkkaavaisuus.md"]},
  {"q": "How do I perceive the pitch of a sound?",
   "notes": ["Atlas\\Notes\\Ääni.md"]},
  {"q": "How can I change my behavior long-term?",
   "notes": ["Atlas\\Notes\\Toiminnan säätely.md"]},
  {"q": "Is other people's bad behavior always due to their bad intentions?",
   "notes": ["Atlas\\Notes\\Attribuutiot.md"]},
  {"q": "The hot pan felt cold to my skin for a while. Why?",
   "notes": ["Atlas\\Notes\\Tuntoaisti.md"]},
  {"q": "I just sorted my closet. Was the algorithm stable?",
   "notes": ["Atlas\\Notes\\Sorting.md"]},
  {"q": "Which data structure in Scala corresponds to Python's list?",
   "notes": ["Atlas\\Notes\\Resizable array.md"]},
  {"q": "Onko A konsonantti?",
   "notes": ["Atlas\\Notes\\Puhe.md"]},
  {"q": "Mihin soitinluokkaan nokkahuilu kuuluu?",
   "notes": ["Atlas\\Notes\\Puhallinsoittimet.md"]},
  {"q": "Miten ihminen muistaa asioita?",
   "notes": ["Atlas\\Notes\\Muisti.md"]},
  {"q": "Mitkä aivorakenteet vastaavat asioiden muistamisesta?",
   "notes": ["Atlas\\Notes\\Muisti.md"]},
  {"q": "Mitä Brocan alue tekee?",
   "notes": ["Atlas\\Notes\\Aivot.md", "Atlas\\Notes\\Motorinen järjestelmä.md"]},
  {"q": "Mikä on internet?",
   "notes": ["Atlas\\Courses\\CS-C3170 - Web Software Development.md"]},
  {"q": "Millaisia hallusinaatioita ihmiset näkevät, jos heille ei anneta aistiärsykkeitä?",
   "notes": ["Atlas\\Courses\\CS-C2000 - Ihminen havaitsijana.md"]},
  {"q": "Missä sijaitsee LGN polvitumake?",
   "notes": ["Atlas\\Courses\\NBE-C2300 - Biologinen psykologia.md"]},
  {"q": "Millainen subwoofer minun kannattaisi hankkia kotiin?",
   "notes": ["Atlas\\Notes\\Audio.md"]},
  {"q": "Mitä erilaisia värijärjestelmiä on olemassa?",
   "notes": ["Atlas\\Notes\\Color.md"]}
]

hits = 0
for case in test_set:
  results = search(case["q"], k=3)
  doc_names = [doc_name for doc_name, text in results]
  if any(n in doc_names for n in case["notes"]):
    hits += 1
  else:
    print(f"MISS: {case['q']}\nwanted one of {case['notes']}\ngot {doc_names}")
recall = hits / len(test_set)

print(f"recall@3: {recall:.2f} ({hits}/{len(test_set)})")