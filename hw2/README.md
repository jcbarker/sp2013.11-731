Jonathan Barker
Homework 2

The first thing I implemented was a variant of the simple METEOR baseline. The change I made was assuming that each word in the hypothesis could only match one word in the reference. This way we avoid overcounting common words like "the" and skewing the score towards hypotheses with common words.

Tuning the balance between recall and precision helped. I enjoyed a decent gain from tokenizing the data, which one would expect. I also tried lowercasing the data but this hurt performance. This was not the only counterintuitive fact however.

I also tried implementing BLEU. My unigram BLEU beat the simple METEOR in training but not in testing. I thought this was odd but continued on. I also tried bigram , trigram, and 4gram BLEU. I combined all of the scores together to make a unified BLEU system. This combined system outperformed any single ngram BLEU and of course beat my simple METEOR. However, it still loses to simple METEOR in testing.

Another approach I took was trying to incorporate linguistic knowledge. I dependency parsed the data using the Stanford Dependency Parser and tried using my simple METEOR metric on the resulting dependencies. This performed terribly.