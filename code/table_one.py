import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import PillowWriter


# Running Total 1A Data (Table Sheet
heads_1a = [0, 2, 2, 4, 6, 7, 9, 10, 11, 12, 13, 14, 16, 17, 17, 19, 21, 22, 23, 25, 26, 28, 28, 29, 31, 32, 33, 34, 36, 38, 39, 39, 40, 41, 43, 44, 44, 46, 47, 47, 47, 47, 49, 49, 49, 50, 52, 54, 55, 56, 57, 58, 58, 60, 61, 62, 64, 65, 66, 67, 68, 68, 69, 71, 71, 73, 75, 76, 77, 78, 78, 79, 80, 81, 82, 83, 84, 86, 88, 88, 89, 91, 91, 93, 94, 96, 96, 98, 99, 100, 101, 103, 103, 105, 107, 107, 108, 108, 110, 111]
tails_1a = [2, 2, 4, 4, 4, 5, 5, 6, 7, 8, 9, 10, 10, 11, 13, 13, 13, 14, 15, 15, 16, 16, 18, 19, 19, 20, 21, 22, 22, 22, 23, 25, 26, 27, 27, 28, 30, 30, 31, 33, 35, 37, 37, 39, 41, 42, 42, 42, 43, 44, 45, 46, 48, 48, 49, 50, 50, 51, 52, 53, 54, 56, 57, 57, 59, 59, 59, 60, 61, 62, 64, 65, 66, 67, 68, 69, 70, 70, 70, 72, 73, 73, 75, 75, 76, 76, 78, 78, 79, 80, 81, 81, 83, 83, 83, 85, 86, 88, 88, 89]

# Running Total 1B Data (Table Sheet)
heads_1b = [3, 5, 8, 10, 12, 13, 16, 18, 21, 22, 24, 25, 28, 30, 34, 36, 39, 41, 42, 43, 45, 48, 49, 52, 56, 58, 62, 62, 65, 67, 69, 71, 72, 75, 77, 80, 82, 84, 86, 88, 90, 92, 93, 94, 96, 98, 99, 102, 104, 106, 108, 110, 111, 113, 116, 119, 121, 122, 126, 127, 130, 132, 133, 134, 135, 138, 139, 141, 142, 144, 146, 149, 151, 153, 155, 156, 159, 160, 162, 164, 167, 168, 169, 172, 173, 176, 178, 179, 181, 183, 185, 187, 189, 189, 190, 192, 193, 194, 196, 197]
tails_1b = [1, 3, 4, 6, 8, 11, 12, 14, 15, 18, 20, 23, 24, 26, 26, 28, 29, 31, 34, 37, 39, 40, 43, 44, 44, 46, 46, 50, 51, 53, 55, 57, 60, 61, 63, 64, 66, 68, 71, 72, 75, 76, 80, 82, 84, 86, 89, 90, 92, 94, 96, 98, 101, 103, 105, 105, 107, 110, 110, 113, 114, 116, 119, 122, 125, 126, 129, 131, 134, 136, 138, 139, 141, 143, 145, 148, 149, 152, 154, 156, 157, 160, 163, 164, 167, 168, 170, 173, 175, 177, 179, 181, 183, 187, 190, 192, 195, 198, 200, 203]

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

# Setup 1A
max_1a = max(max(heads_1a), max(tails_1a))
line_h1, line_t1 = setup_axis(ax1, "Running Total 1A (Table Sheet)", max_1a)

# Setup 1B
max_1b = max(max(heads_1b), max(tails_1b))
line_h2, line_t2 = setup_axis(ax2, "Running Total 1B (Table Sheet)", max_1b)
ax2.set_xlabel('Number of Tosses') # Bottom graph gets X label


def update(frame):
    current_x = trials[:frame]
    
    # Update 1A
    line_h1.set_data(current_x, heads_1a[:frame])
    line_t1.set_data(current_x, tails_1a[:frame])
    
    # Update 1B
    line_h2.set_data(current_x, heads_1b[:frame])
    line_t2.set_data(current_x, tails_1b[:frame])
    
    return line_h1, line_t1, line_h2, line_t2

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=range(1, 101), interval=50, blit=True)

plt.tight_layout()
plt.show()

ani.save('table_sheet_race.gif', writer=PillowWriter(fps=15))