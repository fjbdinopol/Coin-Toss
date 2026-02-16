import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import PillowWriter

# --- Running Total 10A (Tiles Sheet) ---
heads_10a = [0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 3, 4, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 7, 8, 9, 9, 10, 11, 11, 12, 13, 14, 15, 15, 16, 16, 17, 17, 18, 18, 19, 19, 20, 21, 21, 22, 23, 23, 24, 25, 26, 27, 27, 28, 28, 28, 28, 28, 28, 28, 29, 30, 31, 32, 33, 33, 33, 34, 35, 36, 36, 37, 37, 37, 37, 38, 39, 40, 40, 40, 40, 41, 42, 42, 43, 43, 43, 44, 45, 45, 46, 46, 47, 47, 48]
tails_10a = [1, 2, 3, 3, 4, 5, 6, 6, 7, 8, 9, 10, 11, 12, 12, 12, 12, 13, 14, 15, 15, 16, 17, 18, 19, 20, 21, 21, 21, 21, 22, 22, 22, 23, 23, 23, 23, 23, 24, 24, 25, 25, 26, 26, 27, 27, 28, 28, 28, 29, 29, 29, 30, 30, 30, 30, 30, 31, 31, 32, 33, 34, 35, 36, 37, 37, 37, 37, 37, 37, 38, 39, 39, 39, 39, 40, 40, 41, 42, 43, 43, 43, 43, 44, 45, 46, 46, 46, 47, 47, 48, 49, 49, 49, 50, 50, 51, 51, 52, 52]

# --- Running Total 10B (Tiles Sheet) ---
heads_10b = [1, 1, 2, 2, 3, 5, 5, 7, 8, 8, 9, 11, 12, 13, 13, 15, 15, 16, 17, 19, 20, 22, 22, 23, 25, 27, 27, 29, 31, 32, 33, 34, 35, 35, 36, 37, 38, 38, 40, 40, 42, 43, 44, 46, 47, 47, 48, 48, 49, 51, 52, 53, 54, 55, 56, 57, 58, 60, 61, 61, 62, 62, 63, 64, 65, 65, 67, 67, 68, 68, 68, 69, 70, 72, 74, 74, 76, 78, 80, 80, 81, 82, 83, 84, 85, 85, 87, 87, 88, 89, 91, 92, 93, 94, 95, 96, 97, 98, 99, 99]
tails_10b = [1, 3, 4, 6, 7, 7, 9, 9, 10, 12, 13, 13, 14, 15, 17, 17, 19, 20, 21, 21, 22, 22, 24, 25, 25, 25, 27, 27, 27, 28, 29, 30, 31, 33, 34, 35, 36, 38, 38, 40, 40, 41, 42, 42, 43, 45, 46, 48, 49, 49, 50, 51, 52, 53, 54, 55, 56, 56, 57, 59, 60, 62, 63, 64, 65, 67, 67, 69, 70, 72, 74, 75, 76, 76, 76, 78, 78, 78, 78, 80, 81, 82, 83, 84, 85, 87, 87, 89, 90, 91, 91, 92, 93, 94, 95, 96, 97, 98, 99, 101]

# --- Running Total 20 Peso (Tiles Sheet) ---
heads_20 = [0, 1, 3, 5, 7, 9, 9, 10, 11, 12, 13, 14, 16, 17, 17, 18, 19, 19, 20, 21, 23, 23, 23, 23, 23, 24, 25, 27, 27, 27, 28, 29, 29, 30, 31, 33, 34, 35, 35, 35, 37, 38, 40, 41, 41, 43, 43, 44, 44, 46, 47, 48, 49, 50, 51, 52, 54, 56, 57, 58, 59, 60, 61, 62, 63, 63, 63, 63, 64, 66, 67, 68, 68, 69, 70, 71, 71, 71, 72, 73, 74, 75, 75, 75, 77, 79, 80, 80, 81, 82, 82, 84, 86, 87, 88, 90, 91, 92, 93, 94]
tails_20 = [2, 3, 3, 3, 3, 3, 5, 6, 7, 8, 9, 10, 10, 11, 13, 14, 15, 17, 18, 19, 19, 21, 23, 25, 27, 28, 29, 29, 31, 33, 34, 35, 37, 38, 39, 39, 40, 41, 43, 45, 45, 46, 46, 47, 49, 49, 51, 52, 54, 54, 55, 56, 57, 58, 59, 60, 60, 60, 61, 62, 63, 64, 65, 66, 67, 69, 71, 73, 74, 74, 75, 76, 78, 79, 80, 81, 83, 85, 86, 87, 88, 89, 91, 93, 93, 93, 94, 96, 97, 98, 100, 100, 100, 101, 102, 102, 103, 104, 105, 106]

# Create trial numbers (1 to 100)
trials = list(range(1, 101))

fig, axes = plt.subplots(3, 1, figsize=(10, 12), sharex=True)
(ax1, ax2, ax3) = axes

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

# Setup 10A
max_10a = max(max(heads_10a), max(tails_10a))
line_h1, line_t1 = setup_axis(ax1, "Running Total 10A (Tiles Sheet)", max_10a)

# Setup 10B
max_10b = max(max(heads_10b), max(tails_10b))
line_h2, line_t2 = setup_axis(ax2, "Running Total 10B (Tiles Sheet)", max_10b)

# Setup 20 Peso
max_20 = max(max(heads_20), max(tails_20))
line_h3, line_t3 = setup_axis(ax3, "Running Total 20 Peso (Tiles Sheet)", max_20)

ax3.set_xlabel('Number of Tosses')


def update(frame):
    current_x = trials[:frame]
    
    # Update 10A
    line_h1.set_data(current_x, heads_10a[:frame])
    line_t1.set_data(current_x, tails_10a[:frame])
    
    # Update 10B
    line_h2.set_data(current_x, heads_10b[:frame])
    line_t2.set_data(current_x, tails_10b[:frame])
    
    # Update 20 Peso
    line_h3.set_data(current_x, heads_20[:frame])
    line_t3.set_data(current_x, tails_20[:frame])
    
    return line_h1, line_t1, line_h2, line_t2, line_h3, line_t3

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=range(1, 101), interval=50, blit=True)

plt.tight_layout()
plt.show()

ani.save('tiles_sheet_rest_race.gif', writer=PillowWriter(fps=15))