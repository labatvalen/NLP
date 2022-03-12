## Importations
import nltk
#nltk.download() #Permet d'ouvrir la fenetre d'installation pour les librairies de nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk import wordpunct_tokenize
from nltk import pos_tag
from nltk.corpus import wordnet as wn
from nltk.chunk import ne_chunk

## On print les mots "inutiles" des dictionnaires dans les différentes langues
# print(set(stopwords.words('French')))
# print(set(stopwords.words('English')))
# print(set(stopwords.words('Arabic')))

## Exemple de la manière dont on supprimeces mots dans un texte
text = 'In this tutorial, I\'m learning NLTK. It is an interesting platform.' # On définit un texte
stop_words = set(stopwords.words('english')) # On définit les stopwords
words = word_tokenize(text) # Permet de séparer la phrase en liste de mots
new_sentence = []
for word in words:
    if word not in stop_words:
        new_sentence.append(word)
# print(new_sentence) # new_sentence est ainsi la nouvelle phrase, sans les stop_words

## Recherche dans un texte
file = open('essaiTexte.txt', 'r')
read_file = file.read()
text = nltk.Text(nltk.word_tokenize(read_file))
# match = text.concordance('langage') # La fonction text.concordance affiche "No matches" si le mot n'existe pas, et affiche le(s) bout(s) de phrase sinon

## Détection automatique de la langue du texte en utilisant Python et NLTK
phrase = "That's thirty minutes away. I'll be there in ten."
tokens = wordpunct_tokenize(phrase) # On tokenize la phrase
# print(texte)
langues = stopwords.fileids() # Permet de voir toutes les langues dispos
# print(langues)
mots = stopwords.words('english')[0:10] # On ne garde que les dix premiers mots anglais
languages_ratios = {}
words = [word.lower() for word in tokens] # Permet de mettre tous les mots en minuscules
for language in stopwords.fileids(): # On parcours les langues
    stopwords_set = set(stopwords.words(language)) # On récupère les stopwords
    words_set = set(words) # On crée la liste des mots à partir de la liste de tokens
    common_elements = words_set.intersection(stopwords_set) # On regarde les mots qui sont dans la phrase et dans les stop words
    languages_ratios[language] = len(common_elements) # Liste des langues et du "score" des occurences de stopwords dans la phrase
# Ainsi, la langue qui aura le plus gros score sera certainement la langue du texte
# print(languages_ratios) # Avec un score de 7, la langue anglaise a largement été détectée
max = 0
for k,v in languages_ratios.items():
    if v > max:
        max = v
        language_selected = k
print("Language selected :",language_selected,"with",max,"occurencies")

## POS Tagging, pour regrouper des mots dans des catégories (verbes, noms,...)
tags = pos_tag(tokens)
# print(tags)

## Les sens de mots
human = wn.synsets('human')
# print(human)
def1 = wn.synsets('human')[0].definition
# print(def1)
bike = wn.synsets('bicycle')[0]
# print(bike)

## Reconnaissance d'entités
sentence = "Daryl A. is the head of the coworking place Commoncode Corp. from where many people w ork in Melbourne, Australia."
pos_tags = pos_tag(word_tokenize(sentence))
chunk = ne_chunk(pos_tags)
# print(chunk) # Coupe les mots et les classe en fonction de leur type
