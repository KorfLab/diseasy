diseasy
=======

Ideas

+ Compare text vs. semantic similarity
+ Bake-off various language distance metrics
+ Various method of distance too
+ Compare to random

Can you use text comparison methods to find similarities between human diseases
and zebrafish phenotypes?

Or do you need a very custom mapping via ontologies? The original design was to
do something like this. Good idea to first do a bunch of comparisons and then
determine if you need to develop something new.

----

+ Download a bunch of python-based text comparision libraries
+ Start some simple bake-offs
+ Figure out how to do the random model
+ Which are our gold standards?

Q: What does failure look like?
A: Random is indistinguishable from real diseases

Q: What does success look like?
A: Gold standards are found

-----

## Clustering

Compare human diseases vs. human diseases
Compare zf phenotypes vs zf phenotypes


---

textcompare1.py

install conda
pip3 install nltk scikit-learn transformers torch fasttext

curl https://dl.fbaipublicfiles.com/fasttext/vectors-crawl/cc.en.300.bin.gz --output cc.en.300.bin

---

textcompare2.py

pip3 install -U sentence-transformers

works

----

textcompare3.py

pip3 install tensorflow tensorflow_hub

works