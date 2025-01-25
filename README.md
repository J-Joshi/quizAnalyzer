# 📊 Quiz Analyzer

## 🚀 Overview

**Quiz Analyzer** is a Python-based tool that analyzes quiz performance data, identifies strengths and weaknesses, and provides personalized recommendations for students. It helps users improve their learning by offering data-driven insights and tracking progress over time.

---

## 📌 Features

✅ Analyze historical quiz data to track performance trends.  
✅ Identify strong and weak topics based on accuracy and mistakes.  
✅ Generate personalized recommendations for improvement.  
✅ Define a student persona based on patterns in the data.  
✅ Provide insights on speed, accuracy, and efficiency.

---

## 🛠️ Technologies Used

- **Python** 🐍
- **Pandas** 📊 (Data Analysis)
- **Matplotlib** 📈 (Data Visualization)
- **JSON** 📂 (Data Handling)
- **GitHub** 🔗 (Version Control)

---

## 📂 Folder Structure

```bash
quiz-analyzer/
│── data/                 # Stores JSON quiz data
│   ├── current_quiz.json  # Current quiz performance data
│   ├── historical_quiz.json  # Historical quiz performance data
│   ├── user_quiz.json  # User-related quiz data
│── results/              # Stores analysis outputs
│   ├── quiz_analysis_results.json  # Final JSON output
│── scripts/              # Python scripts
│   ├── fetch_data.py       # Fetch quiz data from API
│   ├── analyze_data.py     # Analyze historical quiz performance
│   ├── analyze_current_quiz.py  # Analyze current quiz performance
│── README.md              # Project documentation
│── requirements.txt       # Required Python dependencies
```

---

## ⚙️ Installation & Setup

### **1️⃣ Clone the Repository**

```bash
git clone https://github.com/your-username/quiz-analyzer.git
cd quiz-analyzer
```

### **2️⃣ Create a Virtual Environment (Optional but Recommended)**

```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows
```

### **3️⃣ Install Dependencies**

```bash
pip install -r requirements.txt
```

### **4️⃣ Run the Data Fetching Script**

This script will fetch quiz data from an API and save it locally.

```bash
python scripts/fetch_data.py
```

### **5️⃣ Run the Analysis Scripts**

#### **Analyze Historical Quiz Data**

```bash
python scripts/analyze_data.py
```

#### **Analyze Current Quiz Data**

```bash
python scripts/analyze_current_quiz.py
```

---

## 🔍 Sample Output

### **📊 Performance Summary**

```json
{
  "Average Accuracy": 72.21,
  "Average Score": 60.29,
  "Weak Topics": [
    { "topic": "Principles of Inheritance", "accuracy": 30.0 },
    { "topic": "Human Reproduction", "accuracy": 38.0 }
  ],
  "Strong Topics": [
    { "topic": "Microbes in Human Welfare", "accuracy": 100.0 },
    { "topic": "Human Health and Disease", "accuracy": 93.0 }
  ],
  "Recommendations": [
    "Practice quizzes on weak topics",
    "Improve speed by timing responses",
    "Review mistakes in previous quizzes",
    "Use topic-specific learning resources"
  ]
}
```

---

## 🎭 Student Persona Insights

📌 **Persona Type:** 🎯 The Rising Star - Good performance but needs improvement in accuracy.  
📉 **Weak Areas:** Needs more practice in `Principles of Inheritance`, `Human Reproduction`, and `Reproductive Health`.  
📈 **Strong Areas:** Excels in `Microbes in Human Welfare` and `Human Health and Disease`.

---

## 📌 Key Recommendations

✔️ Revise weak topics and review key concepts in depth.  
✔️ Take more quizzes on challenging areas for reinforcement.  
✔️ Use spaced repetition techniques for better long-term retention.  
✔️ Practice time-bound quizzes to boost question-solving speed.  
✔️ Review previous mistakes to avoid common pitfalls.  
✔️ Optimize test-taking strategies for efficiency.

---

## 📸 Screenshots

📊 Sample Insights Summary:  
![Accuracy Trend](results/accuracy_trend.png)  
![Mistakes Corrected](results/mistakes_corrected_trend.png)  
![Score Trend](results/score_trend.png)

---

## 📝 Future Improvements

- ✅ Implement an interactive web dashboard for visualization.
- ✅ Add an AI-based recommendation system for smarter insights.
- ✅ Integrate with a mobile app for real-time quiz tracking.

---

## 🏆 Contributors

💡 **Your Name** - Developer & Data Analyst  
📧 Contact: [your-email@example.com](mailto:your-email@example.com)

---

## ⭐️ Support

If you found this project useful, please ⭐️ the repository and share your feedback!

```bash
git add .
git commit -m "Updated analysis & recommendations"
git push origin main
```
