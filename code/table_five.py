import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import PillowWriter



# --- Running Total 5A Data (Table Sheet)
heads_5a = [2, 4, 6, 7, 9, 11, 13, 15, 16, 19, 19, 22, 24, 25, 26, 27, 28, 29, 30, 32, 33, 36, 37, 39, 40, 42, 43, 44, 45, 47, 48, 48, 49, 50, 51, 52, 52, 54, 56, 57, 58, 59, 61, 61, 63, 64, 66, 68, 68, 70, 71, 74, 76, 78, 80, 81, 84, 87, 88, 90, 93, 95, 97, 98, 100, 102, 104, 106, 108, 110, 111, 112, 114, 117, 118, 118, 120, 121, 123, 125, 127, 130, 130, 133, 133, 135, 137, 139, 139, 140, 140, 143, 143, 145, 146, 149, 150, 153, 155, 158]
tails_5a = [1, 2, 3, 5, 6, 7, 8, 9, 11, 11, 14, 14, 15, 17, 19, 21, 23, 25, 27, 28, 30, 30, 32, 33, 35, 36, 38, 40, 42, 43, 45, 48, 50, 52, 54, 56, 59, 60, 61, 63, 65, 67, 68, 71, 72, 74, 75, 76, 79, 80, 82, 82, 83, 84, 85, 87, 87, 87, 89, 90, 90, 91, 92, 94, 95, 96, 97, 98, 99, 100, 102, 104, 105, 105, 107, 110, 111, 113, 114, 115, 116, 116, 119, 119, 122, 123, 124, 125, 128, 130, 133, 133, 136, 137, 139, 139, 141, 141, 142, 142]

# --- Running Total 5B Data (Table Sheet)
heads_5b = [1, 3, 4, 5, 6, 7, 8, 9, 9, 11, 12, 13, 14, 15, 16, 18, 20, 21, 22, 22, 24, 25, 26, 27, 27, 28, 29, 31, 31, 31, 31, 33, 35, 37, 37, 38, 39, 39, 40, 41, 41, 42, 43, 44, 44, 46, 48, 49, 50, 51, 52, 53, 54, 55, 56, 56, 56, 58, 59, 59, 60, 62, 62, 63, 63, 65, 65, 66, 67, 68, 69, 70, 72, 73, 74, 76, 78, 79, 80, 81, 82, 83, 84, 84, 85, 86, 86, 88, 89, 91, 91, 92, 94, 95, 95, 95, 96, 96, 98, 99]
tails_5b = [1, 1, 2, 3, 4, 5, 6, 7, 9, 9, 10, 11, 12, 13, 14, 14, 14, 15, 16, 18, 18, 19, 20, 21, 23, 24, 25, 25, 27, 29, 31, 31, 31, 31, 33, 34, 35, 37, 38, 39, 41, 42, 43, 44, 46, 46, 46, 47, 48, 49, 50, 51, 52, 53, 54, 56, 58, 58, 59, 61, 62, 62, 64, 65, 67, 67, 69, 70, 71, 72, 73, 74, 74, 75, 76, 76, 76, 77, 78, 79, 80, 81, 82, 84, 85, 86, 88, 88, 89, 89, 91, 92, 92, 93, 95, 97, 98, 100, 100, 101]

# Create trial numbers (1 to 100)
trials = list(range(1, 101))


fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)

# Function to initialize a subplot
def setup_axis(ax, title, max_y):
    ax.set_title(title, fontsize=12, fontweight='bold')
    ax.set_ylabel('Count')
    ax.set_xlim(0, 100)
    ax.set_ylim(0, max_y * 1.1)
    ax.grid(True, alpha=0.3)
    line_h, = ax.plot([], [], label='Heads', color='blue', linewidth=2)
    line_t, = ax.plot([], [], label='Tails', color='red', linewidth=2)
    ax.legend(loc='upper left')
    return line_h, line_t

# Setup 5A
max_5a = max(max(heads_5a), max(tails_5a))
line_h1, line_t1 = setup_axis(ax1, "Running Total 5A (Table Sheet)", max_5a)

# Setup 5B
max_5b = max(max(heads_5b), max(tails_5b))
line_h2, line_t2 = setup_axis(ax2, "Running Total 5B (Table Sheet)", max_5b)
ax2.set_xlabel('Number of Tosses') # Bottom graph gets X label


def update(frame):
    current_x = trials[:frame]
    
    # Update 5A
    line_h1.set_data(current_x, heads_5a[:frame])
    line_t1.set_data(current_x, tails_5a[:frame])
    
    # Update 5B
    line_h2.set_data(current_x, heads_5b[:frame])
    line_t2.set_data(current_x, tails_5b[:frame])
    
    return line_h1, line_t1, line_h2, line_t2

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=range(1, 101), interval=50, blit=True)

plt.tight_layout()
plt.show()

ani.save('table_sheet_5_race.gif', writer=PillowWriter(fps=15))