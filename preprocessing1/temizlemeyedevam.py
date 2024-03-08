import pandas as pd
import re

# Ayırılmış Excel dosyalarının isimleri ve yolları
separated_excel_names = {
    "Merged_Song": r"C:\Users\baran\OneDrive\Masaüstü\lyric-separated\Merged_Songs.xlsx"
}

for name, excel_file_path in separated_excel_names.items():
    # Excel dosyasını oku
    df = pd.read_excel(excel_file_path)

    # Boş DataFrame oluştur
    df_updated = pd.DataFrame(columns=["Lyric"])

    # Her satırı kontrol et
    for index, row in df.iterrows():
        # Satırdaki sanatçı adı, şarkı adı ve şarkı sözlerini al
        artist_name = row["Artist's Name"]
        track_name = row["Song Name"]
        lyrics_cell = row["Lyric"]

        # Eğer "Lyric" hücresi bir float değilse devam et
        if not isinstance(lyrics_cell, float):
            # İstemediğimiz karakterleri temizle
            cleaned_lyrics = re.sub(r'[.,;:!?\'"(){}[\]<>]', '', lyrics_cell)
            
            # Yeni DataFrame'e satır ekleme
            df_updated = pd.concat([df_updated, pd.DataFrame({"Lyric": [cleaned_lyrics]})], ignore_index=True)

    # Güncellenmiş DataFrame'i yeni bir Excel dosyasına yazma
    df_updated.to_excel(name + "_updated.xlsx", index=False)
