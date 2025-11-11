# 🔐 AI-Enhanced Password Manager (Python + Tkinter + Machine Learning)

A GUI-based **Password Manager** built using **Python** and **Tkinter**, integrated with a **Machine Learning model** that predicts password strength in real-time.  
The application combines traditional rule-based validation with ML classification for intelligent password evaluation.

---

## 🚀 Features

- ✅ Generate strong passwords automatically  
- 🧠 Real-time password strength prediction using ML (90% accuracy)  
- 🎨 Color-coded strength indicator (Weak = Red, Medium = Orange, Strong = Green)  
- 💾 Save and retrieve credentials securely using JSON  
- 📋 Auto-copy passwords to clipboard  
- ⚙️ Hybrid rule-based + ML strength evaluation logic  

---

## 🧠 Tech Stack

- **Python 3.x**
- **Tkinter** — GUI  
- **Scikit-learn** — ML Model  
- **Pandas** — Dataset handling  
- **Regex (`re`)** — Pattern-based validation  
- **JSON** — Local storage  

---

## ⚙️ How It Works

1. `password_strength_model.py` trains a **Logistic Regression** model on labeled password data.  
2. The model and vectorizer are saved as `.pkl` files (`strength_model.pkl`, `vectorizer.pkl`).  
3. `password_manager.py` loads these models and predicts password strength in real-time.  
4. The GUI displays password strength instantly with color feedback.  

---

## 🏗️ Project Structure

Password-Manager-AI/
├── password_manager.py # Tkinter GUI app
├── password_strength_model.py # ML training script
├── password_strength.csv # Dataset (used for training)
├── strength_model.pkl # Saved ML model
├── vectorizer.pkl # Saved text vectorizer
├── data.json # Saved passwords (auto-created)
├── logo.png # App logo
└── README.md # This file


---

## 🖼️ Screenshots


<img width="624" height="542" alt="Screenshot 2025-11-11 140959" src="https://github.com/user-attachments/assets/7c1b30de-8f30-4a34-b92a-2499baaa80a3" />
<img width="625" height="567" alt="Screenshot 2025-11-11 160822" src="https://github.com/user-attachments/assets/1d4441f8-5aa6-492c-9f69-2cc577e846f7" />
<img width="627" height="559" alt="Screenshot 2025-11-11 161147" src="https://github.com/user-attachments/assets/56a59a03-23be-445d-94e5-50231bfda749" />
<img width="631" height="565" alt="Screenshot 2025-11-11 161109" src="https://github.com/user-attachments/assets/f26eea68-c0c1-40ad-a931-51184357d6d6" />
<img width="646" height="566" alt="Screenshot 2025-11-11 161240" src="https://github.com/user-attachments/assets/8ad42f13-a31f-48c8-a28d-696d613b9ed8" />

Example:  
- Main UI  
- Password with strength indicator  
- JSON storage structure  

---

## 🧩 Future Improvements

- 🔒 Encrypt saved passwords  
- 🪪 Add login authentication  
- ☁️ Cloud sync and password export/import  
- 📊 Dashboard showing password strength trends  

---

## 👨‍💻 Author

**Samay Gangwal**  
📧 [samaygangwal21@gmail.com](mailto:samaygangwal21@gmail.com)  
🔗 [LinkedIn](https://linkedin.com/in/samay-gangwal21)  
💻 [GitHub](https://github.com/samay-gangwal)

---

## 🏷️ Keywords

`Python` `Tkinter` `Machine Learning` `Password Manager` `Scikit-learn` `AI` `Data Science` `Security` `Automation`
