import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('wordnet')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger_eng')
nltk.download('maxent_ne_chunker_tab')


#PCFG
import nltk
from nltk import PCFG

grammar1 = PCFG.fromstring("""
S -> NP VP [1.0]


VP -> V NP PP [0.4]
VP -> V NP [0.6]

NP -> NP NP [0.1]
NP -> NP PP [0.2]
NP -> N [0.7]

PP -> P NP [1.0]

N -> 'people' [0.5]
N -> 'fish' [0.2]
N -> 'tanks' [0.2]
N -> 'rods' [0.1]

V -> 'people' [0.1]
V -> 'fish' [0.6]
V -> 'tanks' [0.3]

P -> 'with' [1.0]
""")

sentence = "people fish tanks with rods"
s1 = sentence.split()
parsar = nltk.ViterbiParser(grammar1)
for tree in parsar.parse(s1):
  tree.draw()


#CFG
import nltk
from nltk import CFG

grammar = CFG.fromstring("""
S -> NP VP
VP -> VBG NNS
VP -> VBZ VP
VP -> VBZ NP
NP -> DT NN
NP -> JJ NNS
DT -> 'A'
DT -> 'a'
NN -> 'pilot'
VBZ -> 'likes'
VBG -> 'flying'
JJ -> 'flying'
NNS -> 'planes'
""")

parser = nltk.ChartParser(grammar)

sentence = "A pilot likaes flying plnes".split()

print(sentence)

for tree in parser.parse(sentence):
    tree.draw()
    print(tree)


#edit distance
from nltk.metrics import edit_distance
s1 = 'siva'
s2 ='guru'

print(edit_distance(s1,s2,substitution_cost=2))


#transalation
from nltk.corpus import swadesh

words = swadesh.words('en')
transalte = dict(swadesh.entries(['en','fr']))
print(transalte)
transalte['he']


#chunking

from nltk import ne_chunk,pos_tag,word_tokenize
sentence = "A pilot likaes flying plnes"
tokens = nltk.word_tokenize(sentence)
tags = nltk.pos_tag(tokens)
tree = ne_chunk(tags)
print(tree)
print(tags)


#ngrams
from nltk import word_tokenize,FreqDist
from nltk.util import ngrams

sentence = '''
Machine learning is a branch of artificial intelligence. Machine learning algorithms learn from data. Machine learning models improve with more data. Many machine learning applications use large data sets. Machine learning techniques are widely used today. Machine learning is a branch of artificial intelligence. Machine learning algorithms learn from data. Machine learning models improve with more data. Many machine learning applications use large data sets. Machine learning techniques are widely used today.'''

tokens = word_tokenize(sentence)

bigram = list(ngrams(tokens,2))
print(bigram)
fd = FreqDist(bigram)
print(f"Total words: {len(tokens)}")
sum = 0
for i in tokens:
    sum += len(i)
print(f"Averaged word Length {sum/len(tokens)}")

print(f"Total unique words :{len(set(tokens))}")
print(set(tokens))



#wordnet and synset
from nltk.corpus import wordnet as wn
syn = wn.synsets('car')

#synonyms
synonyms = set()

for synset in syn:
    for lemma in synset.lemmas():
        synonyms.add(lemma.name())

print(synonyms)

#antonyms
antonoyms = set()

for synset in wn.synsets('full'):
    for lemma in synset.lemmas():
        if lemma.antonyms():
            antonoyms.add(lemma.antonyms()[0].name())

antonoyms

#definitions & examples
for word in syn:
    print(f'The definition of {word} is {word.definition()}')
    print(word.examples())


#hypernyms (super class)

print(syn[0].hypernyms())

# hyponyms (subclass)

print(syn[0].hyponyms())

#path similarity

car = wn.synsets('car')
bus = wn.synsets('bus')
cat = wn.synsets('cat')

print(car[0].path_similarity(bus[0]))
print(car[0].path_similarity(cat[0]))


#stemming
from nltk import SnowballStemmer, LancasterStemmer, WordNetLemmatizer,PorterStemmer
from nltk.corpus import stopwords
from nltk.corpus import gutenberg
snowball = SnowballStemmer('english')
porter = PorterStemmer()
lancaster = LancasterStemmer()
lemmatizer = WordNetLemmatizer()

stopwords = stopwords.words('english')
words = gutenberg.words('austen-sense.txt')[:200]
words = [word for word in words if word not in stopwords and word.isalpha()]
for word in words:
    print(word);print(snowball.stem(word));print(porter.stem(word));print(lemmatizer.lemmatize(word))



#pos tags

from nltk import pos_tag,word_tokenize

sentence = "The cat sat on mat"
tokens = word_tokenize(sentence)
tags = pos_tag(tokens)
print(tags)


#FreqDist
from nltk import FreqDist
from nltk.corpus import gutenberg
words = gutenberg.words('chesterton-ball.txt')
words = [w for w in words if w.isalpha()]
fd = FreqDist(words)
fd.most_common(50)

#stopwords
from nltk.corpus import stopwords

stopwords = stopwords.words('english')
stopwords

#tokenization
from nltk import word_tokenize,sent_tokenize
sentences = 'Machine learning is a branch of artificial intelligence. Machine learning algorithms learn from data. Machine learning models improve with more data. Many machine learning applications use large data sets. Machine learning techniques are widely used today. Machine learning is a branch of artificial intelligence. Machine learning algorithms learn from data. Machine learning models improve with more data. Many machine learning applications use large data sets. Machine learning techniques are widely used today.'
print(sent_tokenize(sentences))
print(word_tokenize(sentences))


#regex
import re 

import nltk
from nltk.tokenize import sent_tokenize
text = """Dr. Siva completed his M.Sc. in Data Science. He scored 9.1 CGPA in the first semester.
Mr. Arun joined later.
The meeting started at 10.30 a.m. and ended quickly.
"""

abb = ['Dr.','M.Sc.','Mr.','a.m.']
for ab in abb:
    safe_abb = ab.replace('.','<dot>')
    text = text.replace(ab,safe_abb)

Safetext = re.sub(r'(\d+)\.(\d+)',r'\1<decimal>\2',text)

sentences = sent_tokenize(Safetext)
final =[]
for sentence in sentences:
    sentence = sentence.replace("<dot>",".")
    sentence = sentence.replace("<decimal>",".")
    final.append(sentence)

print(final)

#np chunk and parsing tree
import nltk
from nltk import pos_tag,word_tokenize
sentence ="The young programmer wrote complex code yesterday in microsoft in chennai"
tokens = word_tokenize(sentence)
tags = pos_tag(tokens)

grammar = r"NP: {<DT>?<JJ>*<NN>+}"
cp = nltk.RegexpParser(grammar)
tree = cp.parse(tags)
tree.draw()

#the holonym-meronym relations for 4 nouns
from nltk.corpus import wordnet as wn 
noun1 = wn.synsets('car')[0]
noun2 = wn.synsets('dog')[0]
noun1.part_holonyms()
noun2.part_holonyms()
noun2.part_meronyms()
noun1.part_meronyms()


