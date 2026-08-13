from ask import search

# 50 questions, grouped by which aspect they test
# Every label was verified against the actual note content
test_set = [

  # Uses the note's own vocabulary
  {"q": "Mikä on vastaväriteoria?",
   "notes": ["Atlas\\Notes\\Vastaväriteoria.md"]},
  {"q": "What is relational data?",
   "notes": ["Atlas\\Notes\\Relational data.md"]},
  {"q": "Mitä näytteistys tarkoittaa signaalinkäsittelyssä?",
   "notes": ["Atlas\\Notes\\Näytteistys.md"]},
  {"q": "Mikä on SNR eli signaali-kohinasuhde?",
   "notes": ["Atlas\\Notes\\Kohina.md"]},
  {"q": "What is dimensionality reduction?",
   "notes": ["Atlas\\Notes\\Dimensionality reduction.md"]},
  {"q": "Mitä stereotypiat ovat?",
   "notes": ["Atlas\\Notes\\Stereotypia.md"]},
  {"q": "What is a priority queue?",
   "notes": ["Atlas\\Notes\\Priority queue.md"]},
  {"q": "Mitä itsesäätely tarkoittaa?",
   "notes": ["Atlas\\Notes\\Itsesäätely.md"]},

  # Paraphrased: same concept, different words than the note
  {"q": "How can I find the shortest path from a source to every other node?",
   "notes": ["Atlas\\Notes\\Breadth-first search.md"]},
  {"q": "What algorithm explores a graph as deep as possible before backtracking?",
   "notes": ["Atlas\\Notes\\Depth-first search.md"]},
  {"q": "When is a set of vectors linearly independent?",
   "notes": ["Atlas\\Notes\\Linear dependence.md"]},
  {"q": "How do you fit a model when there are more measurements than parameters?",
   "notes": ["Atlas\\Notes\\Least squares problems.md"]},
  {"q": "How does a system's output relate to a time-shifted version of its input?",
   "notes": ["Atlas\\Notes\\LTI-järjestelmä.md"]},
  {"q": "What are the components that make up prejudice?",
   "notes": ["Atlas\\Notes\\Ennakkoluuloisuus.md"]},
  {"q": "How is a graph stored in memory?",
   "notes": ["Atlas\\Notes\\Graphs.md"]},
  {"q": "What decides the fundamental frequency of a plucked string?",
   "notes": ["Atlas\\Notes\\Kielisoittimet.md"]},
  {"q": "Millaisia hallusinaatioita ihmiset näkevät, jos heille ei anneta aistiärsykkeitä?",
   "notes": ["Atlas\\Courses\\CS-C2000 - Ihminen havaitsijana.md"]},

  # Natural / indirect: no direct reference to content
  {"q": "I just sorted my closet. Was the algorithm stable?",
   "notes": ["Atlas\\Notes\\Sorting.md"]},
  {"q": "Which data structure in Scala corresponds to Python's list?",
   "notes": ["Atlas\\Notes\\Resizable array.md"]},
  {"q": "Miten kaiutin saa aikaan ääntä sähkövirrasta?",
   "notes": ["Atlas\\Notes\\Audio.md"]},
  {"q": "Miksi kielletty hedelmä houkuttaa?",
   "notes": ["Atlas\\Notes\\Motivaatio.md"]},
  {"q": "Miksi valkoinen paperi näyttää valkoiselta sekä auringonvalossa että sisävalaistuksessa?",
   "notes": ["Atlas\\Notes\\Värivakioisuus.md"]},
  {"q": "Miten aivot sopeutuvat esimerkiksi ulkomaille muuttamiseen?",
   "notes": ["Atlas\\Notes\\Aivojen muovautuvuus.md"]},
  {"q": "Miksi vertaan itseäni jatkuvasti muihin ihmisiin?",
   "notes": ["Atlas\\Notes\\Sosiaalisen vertailun teoria.md"]},
  {"q": "How can I tell if a news headline is trying to mislead me?",
   "notes": ["Atlas\\Notes\\Critical thinking.md"]},
  {"q": "Miten hajut voivat tuoda mieleen vanhoja muistoja?",
   "notes": ["Atlas\\Notes\\Hajuaisti.md"]},
  {"q": "They injected something radioactive into my blood and scanned my brain. What were they doing?",
   "notes": ["Atlas\\Notes\\Tutkimusmenetelmät biologisessa psykologiassa.md"]},

  # Exact terms
  {"q": "Missä sijaitsee LGN eli polvitumake?",
   "notes": ["Atlas\\Notes\\Näkö.md", "Atlas\\Notes\\Verkkokalvo.md",
             "Atlas\\Notes\\Sensoriset ja motoriset järjestelmät.md"]},
  {"q": "Mitä Brocan alue tekee?",
   "notes": ["Atlas\\Notes\\Kieli.md", "Atlas\\Notes\\Motorinen järjestelmä.md",
             "Atlas\\Notes\\Aivot.md"]},
  {"q": "What is the 'cone of confusion' in spatial hearing?",
   "notes": ["Atlas\\Notes\\Suuntakuulo.md"]},
  {"q": "Mitä tarkoittaa erotettavuus d' signaalindetektioteoriassa?",
   "notes": ["Atlas\\Notes\\Signal detection theory.md"]},
  {"q": "Kuinka monta desibeliä äänitaso nousee, kun kaksi samanlaista äänilähdettä summataan?",
   "notes": ["Atlas\\Notes\\Äänilaskut.md"]},
  {"q": "What is amortized constant time?",
   "notes": ["Atlas\\Notes\\Resizable array.md"]},
  {"q": "What is the Prägnanz principle in perception?",
   "notes": ["Atlas\\Notes\\Hahmolait.md"]},
  {"q": "Onko A konsonantti?",
   "notes": ["Atlas\\Notes\\Puhe.md"]},

  # Cross-language: English question, Finnish-titled note
  {"q": "How is a continuous signal converted into a discrete one?",
   "notes": ["Atlas\\Notes\\Näytteistys.md"]},
  {"q": "How do we tell which direction a sound comes from?",
   "notes": ["Atlas\\Notes\\Suuntakuulo.md"]},
  {"q": "How does a clarinet produce its sound?",
   "notes": ["Atlas\\Notes\\Puhallinsoittimet.md"]},
  {"q": "How do we perceive depth using both eyes?",
   "notes": ["Atlas\\Notes\\Kolmiulotteisuuden havaitseminen.md"]},
  {"q": "What is contrast sensitivity in vision?",
   "notes": ["Atlas\\Notes\\Kontrastiherkkyys.md"]},
  {"q": "What are glial cells and what do they do?",
   "notes": ["Atlas\\Notes\\Hermosolut.md"]},
  {"q": "How does room size affect reverberation time?",
   "notes": ["Atlas\\Notes\\Huoneakustiikka.md"]},
  {"q": "What is a passband and a stopband in a filter?",
   "notes": ["Atlas\\Notes\\Suodatus.md"]},

  # Multiple valid notes: the answer is in more than one note
  {"q": "How do signals travel in the human brain?",
   "notes": ["Atlas\\Notes\\Hermosolut.md", "Atlas\\Notes\\Aivot.md"]},
  {"q": "Is other people's bad behavior always due to their bad intentions?",
   "notes": ["Atlas\\Notes\\Attribuutiot.md",
             "Atlas\\Notes\\Attribuutioiden erheitä ja vääristymiä.md"]},
  {"q": "What is it called when something in the background distracts me?",
   "notes": ["Atlas\\Notes\\Visuaalinen tarkkaavaisuus.md", "Atlas\\Notes\\Tarkkaavaisuus.md"]},
  {"q": "What does Tufte say about the relationship between the amount of data and the area used to display it?",
   "notes": ["Atlas\\Notes\\Tufte's theory of data graphics.md",
             "Atlas\\Notes\\Tufte, graphical integrity and excellence.md"]},
  {"q": "How do you implement a priority queue efficiently?",
   "notes": ["Atlas\\Notes\\Binary heap.md", "Atlas\\Notes\\Priority queue.md"]},
  {"q": "What's the difference between a LIFO and a FIFO container?",
   "notes": ["Atlas\\Notes\\Stack.md", "Atlas\\Notes\\Queue and deque.md"]},
  {"q": "Miksi vähemmistöihin liitetään helposti kielteisiä stereotypioita?",
   "notes": ["Atlas\\Notes\\Illusorinen korrelaatio.md", "Atlas\\Notes\\Stereotypia.md"]},
  {"q": "Miten ryhmään kuuluminen vaikuttaa ihmisen identiteettiin?",
   "notes": ["Atlas\\Notes\\Sosiaalisen identiteetin teoria.md",
             "Atlas\\Notes\\Ryhmät ja ryhmäprosessit.md"]},
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
