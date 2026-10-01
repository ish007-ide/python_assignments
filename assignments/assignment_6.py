import matplotlib.pyplot as plt

# --------------------------------------------------
# COMPLEX DATA
# --------------------------------------------------
# Weekly study hours
days = [
    "Monday", "Tuesday", "Wednesday", "Thursday",
    "Friday", "Saturday", "Sunday"
]
study_hours = [2.5, 4, 3.5, 5, 6.5, 8, 7]

# Books completed by students
students = [
    "Aarav", "Diya", "Rohan", "Meera",
    "Kabir", "Anaya", "Vivaan", "Isha"
]
books_read = [5, 8, 4, 6, 9, 7, 3, 10]

# Examination marks
exam_scores = [
    42, 48, 51, 55, 59,
    63, 65, 68, 71, 73,
    76, 78, 81, 84, 86,
    88, 91, 94, 96, 98
]

# --------------------------------------------------
# CREATE 3 COMPLEX VISUALIZATIONS
# --------------------------------------------------
fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(16, 5))

fig.suptitle(
    "Complex Student Performance Analysis",
    fontsize=18,
    fontweight="bold"
)

# --------------------------------------------------
# 1. LINE PLOT
# --------------------------------------------------
axes[0].plot(
    days,
    study_hours,
    marker="o",
    markersize=7,
    color="#2563EB",
    linewidth=2.5
)
axes[0].fill_between(
    days,
    study_hours,
    color="#93C5FD",
    alpha=0.25
)
axes[0].set_title("Weekly Study Hours", fontsize=13, fontweight="bold")
axes[0].set_xlabel("Days")
axes[0].set_ylabel("Study Hours")
axes[0].grid(True, linestyle="--", alpha=0.5)
axes[0].tick_params(axis="x", rotation=35)

# --------------------------------------------------
# 2. BAR CHART
# --------------------------------------------------
bar_colors = [
    "#FF6B6B", "#4ECDC4", "#45B7D1", "#F7B731",
    "#A55EEA", "#20BF6B", "#FC5C65", "#3867D6"
]

axes[1].bar(
    students,
    books_read,
    color=bar_colors,
    edgecolor="black",
    linewidth=0.7
)
axes[1].set_title("Books Completed by Students", fontsize=13, fontweight="bold")
axes[1].set_xlabel("Students")
axes[1].set_ylabel("Books Read")
axes[1].tick_params(axis="x", rotation=45)

# Add values above bars
for index, value in enumerate(books_read):
    axes[1].text(
        index,
        value + 0.2,
        str(value),
        ha="center",
        fontweight="bold"
    )

# --------------------------------------------------
# 3. HISTOGRAM
# --------------------------------------------------
axes[2].hist(
    exam_scores,
    bins=[40, 50, 60, 70, 80, 90, 100],
    color="#8E44AD",
    edgecolor="white",
    linewidth=1.5,
    alpha=0.9
)
axes[2].set_title("Examination Score Distribution", fontsize=13, fontweight="bold")
axes[2].set_xlabel("Score Range")
axes[2].set_ylabel("Number of Students")
axes[2].grid(axis="y", linestyle="--", alpha=0.4)

# --------------------------------------------------
# FINAL DISPLAY
# --------------------------------------------------
plt.tight_layout()
plt.show()
