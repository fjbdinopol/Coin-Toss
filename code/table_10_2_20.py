import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import PillowWriter



# --- Running Total 10A (Table Sheet) ---
heads_10a = [1, 2, 3, 4, 5, 6, 6, 7, 9, 10, 10, 10, 11, 11, 13, 14, 15, 16, 16, 17, 19, 20, 22, 24, 26, 28, 29, 31, 33, 35, 35, 36, 37, 37, 37, 38, 38, 39, 39, 39, 40, 42, 43, 44, 45, 46, 48, 50, 51, 52, 54, 55, 55, 57, 57, 58, 59, 61, 61, 62, 62, 64, 64, 66, 67, 68, 70, 72, 74, 75, 76, 78, 79, 79, 80, 81, 82, 82, 82, 82, 83, 84, 86, 87, 87, 89, 89, 91, 91, 92, 93, 94, 94, 95, 95, 97, 99, 101, 102, 102]
tails_10a = [1, 2, 3, 4, 5, 6, 8, 9, 9, 10, 12, 14, 15, 17, 17, 18, 19, 20, 22, 23, 23, 24, 24, 24, 24, 24, 25, 25, 25, 25, 27, 28, 29, 31, 33, 34, 36, 37, 39, 41, 42, 42, 43, 44, 45, 46, 46, 46, 47, 48, 48, 49, 51, 51, 53, 54, 55, 55, 57, 58, 60, 60, 62, 62, 63, 64, 64, 64, 64, 65, 66, 66, 67, 69, 70, 71, 72, 74, 76, 78, 79, 80, 80, 81, 83, 83, 85, 85, 87, 88, 89, 90, 92, 93, 95, 95, 95, 95, 96, 98]

# --- Running Total 10B (Table Sheet) ---
heads_10b = [0, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 5, 6, 7, 7, 8, 9, 10, 11, 11, 12, 12, 13, 13, 13, 14, 14, 15, 15, 15, 15, 16, 17, 18, 18, 18, 19, 19, 19, 20, 20, 21, 22, 22, 22, 23, 24, 25, 25, 26, 27, 28, 28, 28, 29, 29, 29, 30, 30, 30, 30, 31, 31, 32, 32, 33, 33, 34, 35, 35, 35, 36, 37, 37, 38, 39, 40, 40, 41, 42, 43, 44, 44, 44, 45, 46, 46, 47, 48, 49, 49, 50, 51, 51, 52, 53, 54, 54, 55, 56]
tails_10b = [1, 1, 2, 2, 3, 4, 4, 5, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 8, 9, 9, 10, 10, 11, 12, 12, 13, 13, 14, 15, 16, 16, 16, 16, 17, 18, 18, 19, 20, 20, 21, 21, 21, 22, 23, 23, 23, 23, 24, 24, 24, 24, 25, 26, 26, 27, 28, 28, 29, 30, 31, 31, 32, 32, 33, 33, 34, 34, 34, 35, 36, 36, 36, 37, 37, 37, 37, 38, 38, 38, 38, 38, 39, 40, 40, 40, 41, 41, 41, 41, 42, 42, 42, 43, 43, 43, 43, 44, 44, 44]

# --- Running Total 2 Peso (Table Sheet) ---
heads_2 = [0, 1, 1, 2, 3, 3, 4, 4, 5, 6, 7, 7, 7, 7, 8, 8, 8, 9, 10, 10, 11, 12, 12, 13, 14, 14, 15, 15, 15, 15, 16, 16, 17, 18, 19, 19, 19, 20, 21, 22, 22, 23, 23, 23, 24, 24, 24, 25, 25, 26, 27, 28, 29, 29, 29, 29, 30, 31, 32, 32, 33, 34, 34, 34, 34, 34, 35, 35, 35, 36, 37, 38, 38, 39, 39, 40, 41, 42, 43, 43, 43, 44, 44, 44, 45, 45, 45, 45, 46, 47, 48, 49, 49, 49, 49, 50, 51, 52, 53, 54]
tails_2 = [1, 1, 2, 2, 2, 3, 3, 4, 4, 4, 4, 5, 6, 7, 7, 8, 9, 9, 9, 10, 10, 10, 11, 11, 11, 12, 12, 13, 14, 15, 15, 16, 16, 16, 16, 17, 18, 18, 18, 18, 19, 19, 20, 21, 21, 22, 23, 23, 24, 24, 24, 24, 24, 25, 26, 27, 27, 27, 27, 28, 28, 28, 29, 30, 31, 32, 32, 33, 34, 34, 34, 34, 35, 35, 36, 36, 36, 36, 36, 37, 38, 38, 39, 40, 40, 41, 42, 43, 43, 43, 43, 43, 44, 45, 46, 46, 46, 46, 46, 46]

# --- Running Total 20 Peso (Table Sheet) ---
heads_20 = [0, 0, 1, 2, 2, 2, 2, 3, 3, 4, 5, 5, 5, 6, 7, 7, 7, 7, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 13, 13, 13, 13, 14, 14, 15, 15, 15, 16, 17, 17, 17, 17, 18, 19, 19, 19, 20, 21, 22, 23, 23, 23, 24, 25, 25, 25, 26, 27, 27, 27, 28, 29, 30, 30, 31, 31, 31, 31, 32, 32, 32, 33, 33, 33, 34, 34, 35, 36, 37, 37, 37, 37, 38, 39, 39, 39, 40, 41, 42, 43, 44, 45, 45, 46, 47, 48]
tails_20 = [1, 2, 2, 2, 3, 4, 5, 5, 6, 6, 6, 7, 8, 8, 8, 9, 10, 11, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17, 18, 18, 19, 20, 21, 22, 23, 23, 24, 24, 25, 26, 26, 26, 27, 28, 29, 29, 29, 30, 31, 31, 31, 31, 31, 32, 33, 33, 33, 34, 35, 35, 35, 36, 37, 37, 37, 37, 38, 38, 39, 40, 41, 41, 42, 43, 43, 44, 45, 45, 46, 46, 46, 46, 47, 48, 49, 49, 49, 50, 51, 51, 51, 51, 51, 51, 51, 52, 52, 52, 52]

# Create trial numbers (1 to 100)
trials = list(range(1, 101))

fig, axes = plt.subplots(4, 1, figsize=(10, 16), sharex=True)
(ax1, ax2, ax3, ax4) = axes

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
line_h1, line_t1 = setup_axis(ax1, "Running Total 10A (Table Sheet)", max_10a)

# Setup 10B
max_10b = max(max(heads_10b), max(tails_10b))
line_h2, line_t2 = setup_axis(ax2, "Running Total 10B (Table Sheet)", max_10b)

# Setup 2 Peso
max_2 = max(max(heads_2), max(tails_2))
line_h3, line_t3 = setup_axis(ax3, "Running Total 2 Peso (Table Sheet)", max_2)

# Setup 20 Peso
max_20 = max(max(heads_20), max(tails_20))
line_h4, line_t4 = setup_axis(ax4, "Running Total 20 Peso (Table Sheet)", max_20)

ax4.set_xlabel('Number of Tosses')

def update(frame):
    current_x = trials[:frame]
    
    # Update 10A
    line_h1.set_data(current_x, heads_10a[:frame])
    line_t1.set_data(current_x, tails_10a[:frame])
    
    # Update 10B
    line_h2.set_data(current_x, heads_10b[:frame])
    line_t2.set_data(current_x, tails_10b[:frame])
    
    # Update 2 Peso
    line_h3.set_data(current_x, heads_2[:frame])
    line_t3.set_data(current_x, tails_2[:frame])
    
    # Update 20 Peso
    line_h4.set_data(current_x, heads_20[:frame])
    line_t4.set_data(current_x, tails_20[:frame])
    
    return line_h1, line_t1, line_h2, line_t2, line_h3, line_t3, line_h4, line_t4

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=range(1, 101), interval=50, blit=True)

plt.tight_layout()
plt.show()

ani.save('table_sheet_10-2-20_race.gif', writer=PillowWriter(fps=15))