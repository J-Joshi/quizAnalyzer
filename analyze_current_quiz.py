import json

# Load User Quiz Data (Contains the actual performance)
with open("data/user_quiz.json", "r") as file:
    user_quiz_data = json.load(file)

# Extract key performance metrics
total_questions_attempted = user_quiz_data["correct_answers"] + user_quiz_data["incorrect_answers"]
accuracy = float(user_quiz_data["accuracy"].replace("%", "")) if "accuracy" in user_quiz_data else 0
negative_score = float(user_quiz_data["negative_score"])
mistakes_corrected = user_quiz_data["mistakes_corrected"]

# Extract topic-level performance from user responses
topic_analysis = {}
response_map = user_quiz_data["response_map"]

# Identify topic-wise performance
for question_id, selected_option_id in response_map.items():
    topic = user_quiz_data["quiz"]["topic"]  # The topic is provided in user_quiz_data

    if topic not in topic_analysis:
        topic_analysis[topic] = {"correct": 0, "incorrect": 0}

    # Update correct/incorrect counts
    if selected_option_id:  # Assuming a response exists
        topic_analysis[topic]["correct"] += 1
    else:
        topic_analysis[topic]["incorrect"] += 1

# Separate weak and strong topics correctly
weak_topics = []
strong_topics = []

for topic, stats in topic_analysis.items():
    total_attempts = stats["correct"] + stats["incorrect"]
    
    # Check if correct answers are greater than 80% of total attempts
    if total_attempts > 0 and (stats["correct"] / total_attempts) >= 0.8:
        strong_topics.append((topic, stats))  # Add to strong topics
    else:
        weak_topics.append((topic, stats))  # Add to weak topics

# 🎭 **Define Student Persona Based on Performance**
if accuracy > 90 and negative_score < 3:
    student_persona = "The Perfectionist - High accuracy, minimal mistakes, always striving for 100%."
elif accuracy > 75 and negative_score < 5:
    student_persona = "The Consistent Achiever - Strong performer with steady results."
elif accuracy > 50:
    student_persona = "The Rising Star - Good performance but needs improvement in accuracy."
elif accuracy < 50 and user_quiz_data["incorrect_answers"] > user_quiz_data["correct_answers"]:
    student_persona = "The Underdog - Needs a boost in fundamentals to improve performance."
else:
    student_persona = "The Fast Learner - Learning from mistakes and improving over time."

# 🔍 **Generate Personalized Recommendations**
recommendations = {
    "Improve Accuracy": [
        "Review weak topics and understand key concepts.",
        "Practice more quizzes on challenging areas.",
        "Use spaced repetition for better retention."
    ],
    "Enhance Speed": [
        "Take more timed quizzes to improve time management.",
        "Review mistakes to avoid negative scores."
    ],
    "Suggested Topics to Focus On": [topic[0] for topic in weak_topics],
    "Strongest Topics": [topic[0] for topic in strong_topics],
    "Student Persona": student_persona
}

# 📊 **Create Performance Summary**
analysis_results = {
    "Total Questions Attempted": total_questions_attempted,
    "Correct Answers": user_quiz_data["correct_answers"],
    "Incorrect Answers": user_quiz_data["incorrect_answers"],
    "Accuracy (%)": round(accuracy, 2),
    "Negative Score": negative_score,
    "Mistakes Corrected": mistakes_corrected,
    "Weak Topics": weak_topics,
    "Strong Topics": strong_topics,
    "Recommendations": recommendations
}

# Save results to JSON
output_file = "result/current_quiz_analysis.json"
with open(output_file, "w") as f:
    json.dump(analysis_results, f, indent=4)

print(f"Analysis complete! Results saved in '{output_file}'.")
