import pandas as pd
import re

def clean_lyrics(lyrics):
    # "You might also like" ve "Embed" ifadelerini temizle
    cleaned_lyrics = re.sub(r'You might also like|Embed', '', lyrics, flags=re.IGNORECASE)
    
    # Nokta, virgül, noktalı virgül, iki nokta, üç nokta, soru, ünlem, tırnak, ayraç, kesme işaretleri ve boş satırları sil
    cleaned_lyrics = re.sub(r'([.,;:?!\"()\[\]{}\'‘’“”\s]+)', ' ', cleaned_lyrics)
    
    return cleaned_lyrics.strip()

cleaned_ver2_excel_names = {
    "MERGED":r"C:\Users\baran\OneDrive\Masaüstü\lyric-separated\Merged_Songs.xlsx"
}

for name, excel_file_path in cleaned_ver2_excel_names.items():
    df = pd.read_excel(excel_file_path)
    df_updated = pd.DataFrame(columns=["Artist's Name", "Song Name", "Lyric"])
    
    for index, row in df.iterrows():
        track_name = str(row["Song Name"])
        artist_name = str(row["Artist's Name"])
        
        # Şarkı sözlerini temizleme işlemi
        cleaned_lyrics = clean_lyrics(str(row["Lyric"]))
        
        new_row = pd.Series({"Artist's Name": artist_name,
                             "Song Name": track_name,
                             "Lyric": cleaned_lyrics})
        
        df_updated = pd.concat([df_updated, new_row.to_frame().T], ignore_index=True)

    # Boş satırları filtreleme
    df_updated = df_updated.dropna(subset=["Lyric"], how="all")

    df_updated.to_excel(name + "_updated.xlsx", index=False)

