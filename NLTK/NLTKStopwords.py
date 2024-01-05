#NLTK includes a list of common stopwords (words that are often excluded from text analysis because they are deemed to be of little value).
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
stop_words=set(stopwords.words('english'))
print(stop_words)
#{'needn', 'for', 'a', 'ain', 'which', 'am', 'below', 'each', 'or', 'such', 'very', 'down', 'than', 'are', "wasn't", "you'd", 'ourselves', 've', 'how', 'll', 'they', 'whom', 'just', 'under', "weren't", 'against', 'does', 'you', "hasn't", 'yourself', 'these', 'i', 'before', 'until', 'too', 'this', 'after', 'is', 'she', 'it', 'mightn', "shan't", 'their', 'as', 'do', 'doing', 'at', 'o', "hadn't", 'won', 'then', 'in', 'me', 'will', 'yourselves', 'themselves', 'your', 'why', 'itself', 'no', 's', 'once', "you're", 'and', "don't", "you'll", 'who', 'be', 'all', 'haven', 'ma', "mustn't", "won't", 'did', 'other', 'out', "aren't", 'isn', 'here', 'between', 'over', 'any', 'his', 'there', 'myself', 'most', 'wouldn', 'both', 'of', "it's", 'can', 'few', 'that', 'to', 'hadn', 'should', "should've", 'what', 'them', 'being', 'more', 'y', 'those', "couldn't", 'have', 'during', 'nor', 'only', "wouldn't", 'himself', 'shan', 'because', 'hasn', "you've", "isn't", "mightn't", 'through', 'not', 'herself', 'up', 'were', 'd', 'when', 'off', "doesn't", 'weren', 'where', 'we', "that'll", 'but', 'm', 'couldn', 'didn', 'was', "needn't", 'own', 'about', 'its', 'don', 'above', 'some', "didn't", 'ours', 'from', 'him', 'been', 'he', 'aren', 'again', 'an', 'having', 'the', 're', 'had', 'doesn', 'yours', "shouldn't", 'same', 'by', 'shouldn', 'now', 'on', 'while', 'our', 'has', 'theirs', 'mustn', 'her', 'my', 'hers', 't', "she's", 'wasn', 'further', 'so', "haven't", 'with', 'if', 'into'}
