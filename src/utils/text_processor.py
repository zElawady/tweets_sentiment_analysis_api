import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk import word_tokenize, pos_tag
from nltk.corpus import wordnet

from .config import EMOTIONS_DICT, NEGATION_STOPWORDS




class TextProcessor:
     def __init__(self):
          self.stop_words = set(stopwords.words('english')) - set(NEGATION_STOPWORDS)
          self.lemmatizer = WordNetLemmatizer()
          self.emotions_dic = EMOTIONS_DICT
          
     def _remove_stop_words(self, text: str) -> str:
          return " ".join([word for word in text.split() if word not in self.stop_words])
          
     def _remove_pattern(self, input_text: str, pattern: str) -> str:
          return re.sub(pattern, '', input_text)
     
     def _remove_hyberlinks(self, text: str) -> str:
          return re.sub(r'https?://\S+', '', text)
     
     def _remove_repeated_chars_more_than_2(self, text: str) -> str:
          return re.sub(r'(.)\1{2,}', r'\1', text)
     
     def _replace_emotions(self, text: str) -> str:
          for symbol, meaning in self.emotions_dic.items():
               text = re.sub(re.escape(symbol), f" {meaning} ", text)
          return text
     
     def _remove_punc(self, text: str) -> str:
          text = re.sub(r'\d+', '', text)
          text = re.sub(r'[^\w\s]', '', text)
          text = re.sub(r'\s+', ' ', text).strip()
          return text
     
     def _get_wordnet_pos(self, treebank_tag):
          if treebank_tag.startswith('J'):
               return wordnet.ADJ
          elif treebank_tag.startswith('V'):
               return wordnet.VERB
          elif treebank_tag.startswith('N'):
               return wordnet.NOUN
          elif treebank_tag.startswith('R'):
               return wordnet.ADV
          else:
               return wordnet.NOUN  

     def _tokeniz_lemm(self, text: str) -> str:
          tokens = word_tokenize(text)
          pos_tags = pos_tag(tokens)
          lemmatized = [self.lemmatizer.lemmatize(word, self._get_wordnet_pos(pos)) for word, pos in pos_tags]
          return " ".join(lemmatized)
     
     def process_text(self, text: str) -> str:
          text = text.lower()
          text = self._remove_pattern(text, r'@\w+')
          text = self._remove_hyberlinks(text)
          text = self._remove_repeated_chars_more_than_2(text)
          text = self._replace_emotions(text)
          text = self._remove_punc(text)
          text = self._remove_stop_words(text)
          text = self._tokeniz_lemm(text)
          return text