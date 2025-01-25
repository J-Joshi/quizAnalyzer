import json
import pandas as pd

# Load JSON files
def load_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

# File paths
historical_file = "data/historical_quiz.json"
current_file = "data/current_quiz.json"
user_file = "data/user_quiz.json"

# Load data
historical_data = load_json(historical_file)
current_data = load_json(current_file)
user_data = load_json(user_file)

# Convert historical quiz data into DataFrame
historical_df = pd.DataFrame(historical_data)

# Convert accuracy to numeric values
historical_df['accuracy'] = historical_df['accuracy'].str.replace('%', '').astype(float)

# Convert date strings to datetime
historical_df['submitted_at'] = pd.to_datetime(historical_df['submitted_at'])

# Extract topic from nested JSON
historical_df['topic'] = historical_df['quiz'].apply(lambda x: x['topic'])

# Group Performance by Topic
topic_performance = historical_df.groupby("topic").agg({
    "accuracy": "mean",
    "score": "mean",
    "mistakes_corrected": "mean",
    "incorrect_answers": "sum"
}).reset_index()

# Identify Weak Areas (Topics with Lowest Accuracy)
weak_topics = topic_performance.sort_values(by="accuracy").head(3)
strong_topics = topic_performance.sort_values(by="accuracy", ascending=False).head(3)

# Generate Insights
average_accuracy = float(historical_df["accuracy"].mean())
average_score = float(historical_df["score"].mean())
average_final_score = float(historical_df["final_score"].astype(float).mean())
average_negative_score = float(historical_df["negative_score"].astype(float).mean())

# 🎭 **Student Persona Definition**
if average_accuracy > 90 and average_negative_score < 3:
    student_persona = "The Perfectionist - High accuracy, minimal mistakes, always striving for 100%."
elif average_accuracy > 75 and average_negative_score < 5:
    student_persona = "The Consistent Achiever - Strong performer with steady results."
elif average_accuracy > 50:
    student_persona = "The Rising Star - Good performance but needs improvement in accuracy."
elif average_accuracy < 50 and historical_df["incorrect_answers"].sum() > historical_df["correct_answers"].sum():
    student_persona = "The Underdog - Needs a boost in fundamentals to improve performance."
else:
    student_persona = "🔄 The Fast Learner - Learning from mistakes and improving over time."

# 📌 **Highlighting Strengths & Weaknesses**
insights = {
    "Total Questions Attempted": int(historical_df["total_questions"].sum()),
    "Correct Answers": int(historical_df["correct_answers"].sum()),
    "Incorrect Answers": int(historical_df["incorrect_answers"].sum()),
    "Accuracy (%)": round(average_accuracy, 2),
    "Negative Score": round(average_negative_score, 2),
    "Mistakes Corrected": int(historical_df["mistakes_corrected"].sum()),
    "Weak Topics": weak_topics.astype(object).to_dict(orient="records"),  # Convert Pandas DataFrame to dict
    "Strong Topics": strong_topics.astype(object).to_dict(orient="records"),
    "Student Persona": student_persona
}

# 🔍 **Personalized Recommendations**
recommendations = {
    "Improve Accuracy": [
        "Revise weak topics and review key concepts in depth.",
        "Take more quizzes on challenging areas for reinforcement.",
        "Use spaced repetition techniques for better long-term retention."
    ],
    "Enhance Speed": [
        "Practice time-bound quizzes to boost question-solving speed.",
        "Review previous mistakes to avoid common pitfalls.",
        "Optimize test-taking strategies for efficiency."
    ],
    "Suggested Topics to Focus On": [topic["topic"] for topic in weak_topics.astype(object).to_dict(orient="records")],
    "Strongest Topics": [topic["topic"] for topic in strong_topics.astype(object).to_dict(orient="records")],
    "Final Persona": student_persona
}

# Ensure all values are standard Python types
analysis_result = {
    "insights": json.loads(json.dumps(insights, default=str)),  # Ensures serialization
    "recommendations": json.loads(json.dumps(recommendations, default=str))
}

# Save analysis results
output_file = "result/quiz_analysis_results.json"
with open(output_file, "w") as output_file:
    json.dump(analysis_result, output_file, indent=4)

print("\n### 🔍 Performance Summary ###")
print(f"📊 **Average Accuracy:** {average_accuracy:.2f}%")
print(f"🏆 **Student Persona:** {student_persona}")
print("\n🔥 **Weak Topics to Improve:**")
print(weak_topics[['topic', 'accuracy', 'mistakes_corrected']].to_string(index=False))

print("\n💡 **Strong Topics to Maintain:**")
print(strong_topics[['topic', 'accuracy', 'score']].to_string(index=False))

print("\n📌 **Key Recommendations:**")
for rec in recommendations["Improve Accuracy"]:
    print(f"- {rec}")
for rec in recommendations["Enhance Speed"]:
    print(f"- {rec}")

print("\n✅ **Analysis complete!** Results saved in 'quiz_analysis_results.json'.")
