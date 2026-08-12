## baseline | 11.8.2026
recall@3 = 0.60 (3/5)
Misses:
- "signals in the brain" (Hermosolu) -> got Aivot/Sensoriset/Attention. Likely a bad label.
  Aivot is a valid answer, question has multiple correct notes.
- "miksi signaalit ei täydellisiä" (Kohina) -> got LTI/sampling/Fourier.
  Real miss: "not perfect" should have resulted in "Kohina".
  
Next: allow multiple correct notes per question; expand test set to ~20.

## allow multiple valid notes; expand test set to 25 | 11.8.2026
recall@3: 0.68 (17/25)
Problems with multiple languages.
- "värijärjestelmä" (Color.md, color systems) -> värien havaitseminen/värikontrasti/vastaväriteoria
Problems with granularity/exact terms.
- "missä sijaitsee LGN polvitumake" (NBE-C2300 - Biologinen psykologia.md) -> Motorinen järjestelmä/LTI-järjestelmä

Inspection: the chunk in Biologinen psykologia.md containing LGN polvitumake has 6250 chars and 
embedding model only reads the first ~500 of them -> the term is probably diluted and truncated. 
This means that splitting chunks on \n## isn't reliable on long notes with less h2 headings.

**Conclusion**: add a max length of 400-500 chars (the model's window), keeping paragraphs whole. 
So split into paragraphs and combine them. If it doesn't work, hybrid search with BM25 should fix it.

## Add paragraph split -> 1345 smaller chunks | 12.8.2026
recall@3: 0.68 (17/25)
Problem: same doc repeats in results due to smaller chunks.  
Fix: retreive more candidates and keep only the best chunk per note until we have 3 different notes.

## Return best chunk per note | 12.8.2026
recall@3: 0.72 (18/25)
Problem 1: Some of the evaluation questions are bad and should be changed.
- subwoofer isn't really mentioned in Audio.md, it's just connected to the topic of speakers.
- LGN is mentioned very briefly in a course MOC bullet point.

Problem 2: Chunk splitting when there are no paragraphs (e.g., bullet lists).
- Question about Hebb's experiments should be easy, but the information is diluted into a massive chunk.
- Bullet point list counts as one paragraph. Fix: splitting long paragraphs, maybe at line level.

Problem 3: Exact terms get diluted.
- Fix: using Hybrid search with, e.g., BM25