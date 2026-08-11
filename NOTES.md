## baseline - 2026-08-11
recall@3 = 0.60 (3/5), test set n=5
Misses:
- "signals in the brain" (Hermosolu) -> got Aivot/Sensoriset/Attention. Likely a bad label.
  Aivot is a valid answer, question has multiple correct notes.
- "miksi signaalit ei täydellisiä" (Kohina) -> got LTI/sampling/Fourier.
  Real miss: "not perfect" should have resulted in "Kohina".
Next: allow multiple correct notes per question; expand test set to ~20.