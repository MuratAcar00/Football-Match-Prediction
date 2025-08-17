<img src="https://twemoji.maxcdn.com/v/latest/svg/1f1ec-1f1e7.svg" width="20"/> English
<br>
<h3>⚽ Football Match Outcome Prediction System</h3>

This project is a machine learning system that predicts the outcome of football matches. It utilizes historical game data to train a Random Forest Classifier model to forecast whether a match will result in a home win, an away win, or a draw.

🚀 Project Goal
The main objective of this project is to build a predictive model that can forecast the result of a football match based on the historical performance of the two competing clubs.

📊 Dataset
The system uses a comprehensive football dataset containing various CSV files, including:

games.csv: Match details like goals, dates, and club IDs.

clubs.csv: Club information.

Other files (appearances, club_games, etc.) are used for data preparation.
You can also find this dataset at the following link: https://www.kaggle.com/datasets/davidcariboo/player-scores

🧠 Methodology

Data Preprocessing: Relevant columns from the games and clubs datasets were selected and merged. The date column was formatted, and a new result column was created to label match outcomes (1 for home win, 0 for draw, -1 for away win).

Feature Engineering: The model's features were engineered by calculating each club's average goals scored at home and away from the historical data. These averages serve as the key predictors for the match outcome.

Model Training: The data was split into training and testing sets. A Random Forest Classifier model was trained on the training data using the engineered features.

Prediction & Evaluation: The model was used to predict outcomes on the test set. Its performance was evaluated using Accuracy Score, Confusion Matrix, and a Classification Report.

✨ Results
The trained model achieved a specific level of accuracy in predicting match outcomes. The classification report provides detailed metrics (precision, recall, F1-score) for each outcome class, offering a comprehensive view of the model's performance. The system can then be used to predict the outcome of a new match based on the average goal statistics of the two teams.

<br><br><br>

<img src="https://twemoji.maxcdn.com/v/latest/svg/1f1f9-1f1f7.svg" width="20"/> Türkçe
<br>
<h3>⚽ Futbol Maç Sonucu Tahmin Sistemi</h3>

Bu proje, futbol maçlarının sonucunu tahmin eden bir makine öğrenimi sistemidir. Tarihsel maç verilerini kullanarak, bir maçın ev sahibi galibiyetiyle, deplasman galibiyetiyle veya beraberlikle sonuçlanıp sonuçlanmayacağını tahmin etmek için bir Random Forest Sınıflandırıcısı modeli eğitir.

🚀 Proje Amacı
Bu projenin temel amacı, iki rakip kulübün tarihsel performansına dayalı olarak bir futbol maçının sonucunu tahmin edebilecek bir öngörü modeli oluşturmaktır.

📊 Veri Seti
Sistem, çeşitli CSV dosyalarını içeren kapsamlı bir futbol veri setini kullanır:

games.csv: Goller, tarihler ve kulüp kimlikleri gibi maç detayları.

clubs.csv: Kulüp bilgileri.

Diğer dosyalar (appearances, club_games, vb.) veri hazırlığı için kullanılır.
Bu veri setine şu linkten de ulaşabilirsiniz: https://www.kaggle.com/datasets/davidcariboo/player-scores

🧠 Metodoloji

Veri Ön İşleme: games ve clubs veri setlerinden ilgili sütunlar seçilip birleştirildi. Tarih sütunu formatlandı ve maç sonuçlarını etiketlemek için yeni bir result sütunu oluşturuldu (ev sahibi galibiyeti için 1, beraberlik için 0, deplasman galibiyeti için -1).

Özellik Mühendisliği: Modelin özellikleri, her kulübün tarihsel verilerden evinde ve deplasmanda attığı ortalama gollerin hesaplanmasıyla oluşturuldu. Bu ortalamalar, maç sonucu için ana tahminciler olarak hizmet eder.

Model Eğitimi: Veri, eğitim ve test setlerine ayrıldı. Oluşturulan özellikler kullanılarak eğitim verisi üzerinde bir Random Forest Sınıflandırıcısı modeli eğitildi.

Tahmin ve Değerlendirme: Model, test setindeki maç sonuçlarını tahmin etmek için kullanıldı. Performansı, Doğruluk Oranı, Karışıklık Matrisi ve Sınıflandırma Raporu kullanılarak değerlendirildi.

✨ Sonuçlar
Eğitilen model, maç sonuçlarını tahmin etmede belirli bir doğruluk seviyesine ulaşmıştır. Sınıflandırma raporu, her bir sonuç sınıfı için ayrıntılı metrikler (kesinlik, hatırlama, F1 skoru) sunarak modelin performansı hakkında kapsamlı bir bakış sağlar. Sistem, daha sonra iki takımın ortalama gol istatistiklerine dayanarak yeni bir maçın sonucunu tahmin etmek için kullanılabilir.
