import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import PillowWriter



# --- Running Total 1A Data (Tiles Sheet) ---
heads_1a = [2, 3, 5, 7, 9, 11, 13, 15, 17, 20, 23, 25, 26, 27, 28, 29, 31, 32, 34, 35, 36, 39, 41, 43, 45, 48, 50, 51, 53, 53, 56, 56, 56, 58, 59, 59, 60, 62, 63, 64, 66, 68, 69, 71, 73, 74, 75, 76, 76, 77, 78, 79, 82, 82, 82, 84, 85, 86, 87, 89, 90, 92, 94, 96, 98, 99, 100, 101, 103, 104, 107, 108, 110, 110, 111, 113, 113, 114, 115, 116, 116, 116, 117, 120, 121, 121, 122, 122, 124, 125, 126, 127, 129, 130, 131, 131, 131, 132, 134, 134]
tails_1a = [1, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 11, 13, 15, 17, 19, 20, 22, 23, 25, 27, 27, 28, 29, 30, 30, 31, 33, 34, 37, 37, 40, 43, 44, 46, 49, 51, 52, 54, 56, 57, 58, 60, 61, 62, 64, 66, 68, 71, 73, 75, 77, 77, 80, 83, 84, 86, 88, 90, 91, 93, 94, 95, 96, 97, 99, 101, 103, 104, 106, 106, 108, 109, 112, 114, 115, 118, 120, 122, 124, 127, 130, 132, 132, 134, 137, 139, 142, 143, 145, 147, 149, 150, 152, 154, 157, 160, 162, 163, 166]

# --- Running Total 1B Data (Tiles Sheet) ---
heads_1b = [0, 0, 2, 4, 5, 6, 6, 7, 9, 10, 11, 13, 15, 17, 17, 17, 17, 19, 21, 23, 24, 26, 26, 26, 27, 28, 29, 29, 29, 31, 32, 34, 35, 37, 38, 38, 38, 39, 40, 42, 43, 44, 45, 46, 47, 49, 49, 49, 49, 50, 52, 52, 54, 56, 57, 58, 60, 62, 63, 63, 63, 63, 65, 67, 68, 69, 70, 70, 71, 72, 73, 74, 74, 75, 76, 77, 78, 80, 82, 82, 82, 83, 83, 85, 86, 88, 89, 89, 91, 91, 92, 94, 95, 95, 96, 96, 96, 98, 99, 100]
tails_1b = [2, 4, 4, 4, 5, 6, 8, 9, 9, 10, 11, 11, 11, 11, 13, 15, 17, 17, 17, 17, 18, 18, 20, 22, 23, 24, 25, 27, 29, 29, 30, 30, 31, 31, 32, 34, 36, 37, 38, 38, 39, 40, 41, 42, 43, 43, 45, 47, 49, 50, 50, 52, 52, 52, 53, 54, 54, 54, 55, 57, 59, 61, 61, 61, 62, 63, 64, 66, 67, 68, 69, 70, 72, 73, 74, 75, 76, 76, 76, 78, 80, 81, 83, 83, 84, 84, 85, 87, 87, 89, 90, 90, 91, 93, 94, 96, 98, 98, 99, 100]

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
line_h1, line_t1 = setup_axis(ax1, "Running Total 1A (Tiles Sheet)", max_1a)

# Setup 1B
max_1b = max(max(heads_1b), max(tails_1b))
line_h2, line_t2 = setup_axis(ax2, "Running Total 1B (Tiles Sheet)", max_1b)
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

ani.save('tiles_sheet_race.gif', writer=PillowWriter(fps=15))