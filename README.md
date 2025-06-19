# 🎬 Movie Recommendation System

This is a **content-based movie recommendation system** built using Python. The system takes a movie title as input and recommends a list of similar movies using natural language processing and cosine similarity.

---

## 🚀 Tech Stack

- **Python**
- **Pandas, NumPy** – for data preprocessing
- **Scikit-learn** – for TF-IDF vectorization and similarity computation
- **Flask** – for serving the recommendation engine via a web interface
- **HTML/CSS** – for a simple frontend

---

## 📁 Project Structure

```
├── app.py                        # Flask web app
├── movie_recommendation.ipynb   # Jupyter notebook for model building
├── dataset.csv                  # Movie metadata
├── movies_list.pkl              # Serialized data for fast inference
├── requirements.txt             # Python dependencies
├── LICENSE
└── README.md
```

---

## 📊 How It Works

1. **Preprocess the Dataset**: Read and clean `dataset.csv`, focusing on genres, keywords, cast, etc.
2. **Vectorization**: Apply TF-IDF vectorization on combined metadata.
3. **Similarity Calculation**: Compute cosine similarity between movie vectors.
4. **Recommendation Engine**: Recommend top 5 similar movies for a given input.

---

## 🧠 Sample Input & Output

> **Input**: _Inception_  
> **Output**:
```
1. Interstellar  
2. The Prestige  
3. The Dark Knight  
4. Shutter Island  
5. Memento
```

> 🎥 Output may vary based on dataset and metadata vector construction.

---

## 🛠️ Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/movie-recommendation-system.git
cd movie-recommendation-system
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the App

```bash
python app.py
```

Visit `http://localhost:5000` to use the web-based movie recommender.

---

## 💾 Dataset

- **File**: `dataset.csv`  
- The dataset includes movie titles, genres, cast, crew, keywords, etc.

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---

## 👨‍💻 Author

**Rakesh Sarma Ponukupati**  
📧 rakesh20050618@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/rakesh-sarma-ponukupati-6b3512259/) | [GitHub](https://github.com/Rakesh-005)

---

## 🙌 Contributing

Pull requests are welcome! Feel free to fork the project and suggest improvements to the algorithm or UI.

---
