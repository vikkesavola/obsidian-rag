from ask import search

test_set = [
  {"q": "how does a self-balancing tree stay balanced?",
   "note": "Atlas\\Notes\\AVL Tree.md"},
  {"q": "How do signals travel in the human brain?",
   "note": "Atlas\\Notes\\Hermosolut.md"},
  {"q": "How do people stay motivated according to modern research?",
   "note": "Atlas\\Notes\\Itsemääräämisteoria (SDT).md"},
  {"q": "Miksi signaalit eivät ole ikinä täydellisiä?",
   "note": "Atlas\\Notes\\Kohina.md"},
  {"q": "How can I represent relationships between things as data?",
   "note": "Atlas\\Notes\\Relational data.md"},
]

hits = 0
for case in test_set:
  results = search(case["q"], k=3)
  doc_names = [doc_name for doc_name, text in results]
  if case["note"] in doc_names:
    hits += 1
  else:
    print(f"MISS: {case['q']} -> got {doc_names}")
recall = hits / len(test_set)

print(f"recall@3: {recall:.2f} ({hits}/{len(test_set)})")