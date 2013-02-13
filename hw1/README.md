Jonathan Barker
Homework 1

The first thing I tried was implementing IBM Model 1 and running it on the raw text. This worked as well as the baseline on the leaderboard, but obviously there were other things to try.


Lower casing:
  I ended up lowercasing the inputs, which significantly helped the AER.

Stemming:
  I implemented a trivial stemmer (it removes the last 2 characters) but it worsened my score. I think stemming should definitely help but only with a proper stemmer.

Removing numeral<->nonnumeral and punctuation<->nonpunctuation alignments:
  Removing these links improved AER.

Symmetrizing:
  I trained my model on German to English and vice versa to attempt some symmetrization techniques.
  Union:
    This did not help as the gains in recall did not make up for the loss of precision.
  Intersection:
    This helped the most out of all techniques.
  Grow-Diag:
    This improved over not symmetrizing but it did not beat out intersection, which I find surprising since it should better balance precision and recall. The accuracy gained from intersection was just too good.

I also tried implementing IBM Model 2, but it demanded too much memory from my laptop. It worked on toy data but I could not get results from it to submit for the leaderboard unfortunately.