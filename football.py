# ==============================
#  FUTBOL MAÇ SONUCU TAHMİN SİSTEMİ
# ==============================

# 1) Gerekli Kütüphaneler
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# 2) CSV Dosyalarını Yükleme
appearances = pd.read_csv("appearances.csv")
clubs = pd.read_csv("clubs.csv")
club_games = pd.read_csv("club_games.csv")
competitions = pd.read_csv("competitions.csv")
games = pd.read_csv("games.csv")
game_events = pd.read_csv("game_events.csv")
game_lineups = pd.read_csv("game_lineups.csv")
players = pd.read_csv("players.csv")
player_valuations = pd.read_csv("player_valuations.csv")
transfers = pd.read_csv("transfers.csv")

# 3) Gereksiz Kolonları Atma (sadece lazım olacakları bırakıyoruz)
games = games[['game_id', 'competition_id', 'season', 'date',
               'home_club_id', 'away_club_id',
               'home_club_goals', 'away_club_goals',
               'home_club_name', 'away_club_name']]

clubs = clubs[['club_id', 'name', 'domestic_competition_id']]

# 4) Tarih Formatlama
games['date'] = pd.to_datetime(games['date'], errors="coerce")

# 5) Maç Sonucu Etiketi Oluşturma
# (1 = Ev sahibi kazandı, 0 = Beraberlik, -1 = Deplasman kazandı)
def get_result(row):
    if row['home_club_goals'] > row['away_club_goals']:
        return 1
    elif row['home_club_goals'] < row['away_club_goals']:
        return -1
    else:
        return 0

games['result'] = games.apply(get_result, axis=1)

# 6) Takım İstatistikleri Hesaplama (ortalama goller vb.)
home_stats = games.groupby('home_club_id')['home_club_goals'].mean().reset_index()
home_stats.columns = ['club_id', 'avg_home_goals']

away_stats = games.groupby('away_club_id')['away_club_goals'].mean().reset_index()
away_stats.columns = ['club_id', 'avg_away_goals']

# 7) İstatistikleri Kulüplerle Birleştirme
club_stats = pd.merge(home_stats, away_stats, on='club_id', how='outer')
club_stats.fillna(0, inplace=True)

# 8) Her Maç için Özellikler Hazırlama
games = games.merge(club_stats, left_on='home_club_id', right_on='club_id', how='left')
games = games.merge(club_stats, left_on='away_club_id', right_on='club_id', suffixes=('_home', '_away'), how='left')

# 9) Özellikler (X) ve Hedef (y)
X = games[['avg_home_goals_home', 'avg_away_goals_home', 'avg_home_goals_away', 'avg_away_goals_away']]
y = games['result']

# Eksik verileri doldurma
X.fillna(0, inplace=True)

# 10) Eğitim/Test Bölme
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# 11) Model Oluşturma
model = RandomForestClassifier(n_estimators=200, random_state=42)
model.fit(X_train, y_train)

# 12) Tahmin
y_pred = model.predict(X_test)

# 13) Değerlendirme
print("Doğruluk Oranı:", accuracy_score(y_test, y_pred))
print("Karışıklık Matrisi:\n", confusion_matrix(y_test, y_pred))
print("Sınıflandırma Raporu:\n", classification_report(y_test, y_pred))

# ==============================
# ÖRNEK TAHMİN
# ==============================
# Yeni bir maç tahmini (örneğin: ev sahibi X, deplasman Y takımı)
sample_match = np.array([[1.5, 1.0, 1.2, 0.8]])  # ortalama goller
print("Tahmin (1=Ev sahibi, 0=Beraberlik, -1=Deplasman):", model.predict(sample_match))
