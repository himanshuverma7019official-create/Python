import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Boxplot , shows CUET Cutoff Scores for Departments

data = {
    'CS': [320, 330, 340, 345, 350],
    'Electronics': [300, 305, 315, 320, 325],
    'Chemistry': [295, 305, 310, 315, 320],
    'Physics': [290, 295, 300, 305, 310],
    'Maths': [310, 315, 320, 325, 330],
    'Botany': [280, 285, 290, 295, 300],
    'Zoology': [285, 290, 295, 300, 305],
    'BMS': [300, 305, 310, 315, 320]
}

fig, axes = plt.subplots(2, 2, figsize=(16, 12))
ax1 = axes[0, 0]
bp = ax1.boxplot(data.values(), labels=data.keys(), patch_artist=True, showmeans=True, meanline=False, showbox=True)
box_colors = ['skyblue', 'lightgreen', 'lightcoral', 'lightsalmon', 'lightpink', 'lightyellow', 'lightblue', 'lightgrey']
for patch, color in zip(bp['boxes'], box_colors):
    patch.set_facecolor(color)
for mean_marker in bp['means']:
    mean_marker.set(marker='o', color='g', markersize=5)
ax1.set_title('CUET Cutoff Scores for Departments')
ax1.set_xlabel('Departments')
ax1.set_ylabel('Cut-off Scores')
ax1.grid(True)

# Pie chart , shows student strength in each department entered through CUET

departments = ['CS', 'Electronics', 'Chemistry', 'Physics', 'Maths', 'Botany', 'Zoology', 'BMS']
student_count = [150, 120, 100, 130, 110, 90, 95, 115]
max_student_index = student_count.index(max(student_count))
explode = [0.2 if i == max_student_index or i == departments.index('Botany') else 0 for i in range(len(departments))]
ax2 = axes[0, 1]
ax2.pie(student_count, labels=departments, explode=explode, autopct='%1.1f%%', startangle=140)
ax2.set_title('Student Strength in Each Department entered through CUET')
ax2.axis('equal')

# Histogram , shows CUET Scores Distribution and Comparison (Previous Year vs. Current Year)
previous_year_scores = np.array([320, 433, 340, 350, 380, 360, 398, 260, 576, 589, 456, 480, 560, 530, 470, 200, 240, 260, 520, 512, 168, 620, 705, 280, 555, 595])
current_year_scores = np.array([380, 465, 440, 595, 480, 680, 510, 565, 630, 645, 670, 700, 500, 420, 550, 560, 500, 600, 605, 620, 640, 580, 688, 700, 705, 695, 750, 780, 768])
ax3 = axes[1, 0]
ax3.hist(previous_year_scores, bins=10, alpha=0.7, label='Previous Year', histtype="stepfilled", color="b")
ax3.hist(current_year_scores, bins=10, alpha=0.7, label='Current Year', histtype="step", color="r", hatch="+++")
ax3.set_title('CUET Scores Distribution and Comparison (Previous Year vs. Current Year)')
ax3.set_xlabel('CUET Scores')
ax3.set_ylabel('Frequency')
ax3.legend()
ax3.grid(axis='y')
ax3.set_xticks(np.arange(0, 801, 50))

# bar graph ,shows satisfactory scores i,e ,,Student Satisfaction with Admitted Branches

departments = ['BSc CS', 'BSc Electronics', 'BSc Mathematics', 'BSc Physics', 'BSc Chemistry', 'BSc Zoology', 'BSc Botany', 'BSc BMS', 'B.Commerce']
satisfaction_scores = [9.5, 8.9, 9.0, 8.7, 7.5, 8.2, 7.8, 8.5, 6.7]
data = {'Department': departments, 'Satisfaction_Score': satisfaction_scores}
df = pd.DataFrame(data)
bar_colors = ['cyan', 'green', 'orange', 'red', 'purple', 'brown', 'pink', 'skyblue', 'gray']
ax4 = axes[1, 1]
bars = ax4.bar(df['Department'], df['Satisfaction_Score'], color=bar_colors, alpha=0.7)
ax4.set_title('Student Satisfaction with Admitted Branches')
ax4.set_xlabel('Departments')
ax4.set_ylabel('Satisfaction Scores (out of 10)')
ax4.set_ylim(0, 10)
ax4.set_xticks(range(len(df['Department'])))
ax4.set_xticklabels(df['Department'], rotation=45)
ax4.grid(axis='y')
for bar, score in zip(bars, df['Satisfaction_Score']):
    ax4.text(bar.get_x() + bar.get_width() / 2, score + 0.1, f'{score:.1f}', ha='center', va='bottom')

fig.tight_layout(rect=[0, 0, 1, 0.98])
fig.subplots_adjust(hspace=0.45, wspace=0.25)
plt.show()
 
