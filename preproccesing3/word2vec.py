from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string
import pandas as pd
import nltk

nltk.download('stopwords')

# Veriyi oku
data = pd.read_excel(r"C:\Users\baran\OneDrive\Masaüstü\DDİ Ödevi Son Hal\temizlenmis_veri.xlsx")

# Stopwords'leri yükle
stop_words = set(stopwords.words("turkish"))

# Stopwords listesini genişlet
additional_stopwords = ["bir","'"," '"," ' ","' " ,"ben", "sen", "seni", "beni", "bi", "sana", "bana", "mi",  "yine", "benim", "değil", "senin", "artık","al","ol", "gün","böyle","şimdi","onu", "bak","kadar","offf","hayde","bile","öyle","biraz","senden","benden","ha","haydi","çingenem","hadi","başka","seninle","hele"]
stop_words.update(additional_stopwords)

# Temizleme işlemlerini yapmak için bir fonksiyon tanımla
def clean_lyric(lyric):
    lyric_lower = lyric.lower()
    lyric_no_punctuation = lyric_lower.translate(str.maketrans("", "", string.punctuation))
    tokens = word_tokenize(lyric_no_punctuation)
    filtered_tokens = [token for token in tokens if token not in stop_words]
    return " ".join(filtered_tokens)

# Her satır için temizleme işlemini uygula
data["Cleaned_Lyric"] = data["Lyric"].apply(clean_lyric)

# Stopwords içeren satırları sil
empty_rows = data[data["Cleaned_Lyric"].str.strip() == ""].index
data = data.drop(empty_rows)

# Temizlenmiş veriyi yazdır
data.to_excel("stopwords.xlsx", index=False)
print(data)


