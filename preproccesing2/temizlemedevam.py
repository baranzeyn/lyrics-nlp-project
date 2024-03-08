import pandas as pd
#bir kez dahah temizlemem gerekti

# Excel dosyanızın adını belirtin
excelDosyaAdi = r"C:\Users\baran\OneDrive\Masaüstü\DDİ Ödevi Son Hal\Temizlenmiş.xlsx"

# Excel dosyasını oku
veri = pd.read_excel(excelDosyaAdi)
# 'Lyric' sütununu metin veri tipine dönüştür ve metin olmayan değerleri NaN ile değiştir
veri['Lyric'] = veri['Lyric'].apply(lambda x: str(x) if pd.notna(x) else x)

# Boş string içeren satırları ve NaN değerlere sahip satırları sil
veri = veri.replace('', pd.NA).dropna(subset=['Lyric'])

# Tekrar eden satırları bul ve sil
veri = veri.drop_duplicates()

veri['Lyric'] = veri['Lyric'].astype(str)

veri['Lyric'] = veri['Lyric'].replace(r'\b(?:ra-ra|ra-ra-ra|ra-ra-ra-ra|ah ay|hı hı|a|dj artz|ya|da-da-da-dah|aha|a-a|aah|oh|ooh|of|off|o a-aa|ahh|ah|la la|la-la|--a-|---a-|---a-| --a-|oo|o-o-o|---a-ah|ah-ah-ah a-ah|~instrumental break~|x|oooooooo|-|ahhhhhh|da-da-da|ona buna bulunacak bahane yok|yok|ay canlar|ye ye|he-he|of of|ooo|sal sal sal|ye-e-eah|şşşt)\b', '', regex=True)
veri["Lyric"] = veri["Lyric"].apply(lambda x: str(x).strip() if pd.notna(x) else x)
# Boş string içeren satırları sil
veri = veri.replace('', pd.NA).dropna(subset=['Lyric'])

veri.to_excel('temizlenmis_veri.xlsx', index=False)

print('Tekrar eden satırlar başarıyla silindi ve yeni dosya oluşturuldu.')
