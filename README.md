# Rice Image Classification (CNN using MobileNetV2 Transfer Learning)
Dalam pembuatan projek ini dataset yang digunakan tersedia di Kaggle dengan link: https://www.kaggle.com/datasets/muratkokludataset/rice-image-dataset. Di dalam dataset terdapat 75.000 foto dengan 15.000 foto di tiap kelas beras yakni: Arborio, Basmati, Ipsala, Jasmine, Karacadag. 

Projek bertujuan untuk klasifikasi 5 jenis beras. 
Pada projek ini menggunakan Convolutional Neural Network(CNN) dengan transfer learning MobileNetV2. 

# Tahap Pengerjaan
- Pencarian Dataset
- Loading Dataset
- Splitting Dataset menjadi training, testing, dan validation set
- Modelling
- Evaluasi dan Visualisasi
- Interference Testing
- Model Export

# Hasil Model

Classification Report:
              precision    recall  f1-score   support

     Arborio       0.99      0.97      0.98      2250
     Basmati       0.99      0.99      0.99      2250
      Ipsala       1.00      1.00      1.00      2250
     Jasmine       0.99      0.99      0.99      2250
   Karacadag       0.98      0.99      0.98      2250

    accuracy                           0.99     11250
   macro avg       0.99      0.99      0.99     11250
weighted avg       0.99      0.99      0.99     11250

