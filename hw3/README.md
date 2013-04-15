Jonathan Barker
Hw 3

Approaches:

Swapping:
	For this approach I took the best output of the default decoder then tried swapping adjacent words and phrases. If swapping a word or
	phrase improved the LM score then I keep the swap. This naive approach did provide some gains, but not a lot on it's own. The code is
	in "swapdecode".

Full decoder:
	Here I altered the decoder to allow for reordering of phrases by skipping phrases then translating them later as described in
	the lecture slides. I calculate a future cost for all spans before decoding the integrate this with the TM and LM scores as
	well as a distortion score. My distortion function is a specified alpha raised to the absolute value of the reordering
	distance, as described in lecture and the book.
