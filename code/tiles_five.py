import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import PillowWriter

# --- Running Total 5A Data (Tiles Sheet) ---
heads_5a = [0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 3, 4, 4, 5, 6, 6, 7, 8, 8, 9, 10, 11, 11, 11, 12, 12, 13, 14, 15, 15, 16, 16, 17, 18, 18, 19, 20, 20, 21, 21, 21, 22, 22, 23, 23, 24, 25, 25, 25, 26, 27, 27, 28, 28, 29, 29, 29, 29, 29, 30, 31, 32, 33, 33, 34, 35, 35, 35, 35, 35, 36, 36, 37, 37, 38, 38, 39, 40, 41, 42, 43, 43, 43, 44, 45, 46, 46, 46, 47, 48, 49, 49, 50, 50, 51, 51, 51, 52, 53, 54]
tails_5a = [1, 2, 3, 4, 5, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10, 11, 11, 11, 11, 12, 13, 13, 14, 14, 14, 14, 15, 15, 16, 16, 16, 17, 17, 17, 18, 18, 19, 20, 20, 21, 21, 22, 22, 22, 23, 24, 24, 24, 25, 25, 26, 26, 27, 28, 29, 30, 30, 30, 30, 30, 31, 31, 31, 32, 33, 34, 35, 35, 36, 36, 37, 37, 38, 38, 38, 38, 38, 38, 39, 40, 40, 40, 40, 41, 42, 42, 42, 42, 43, 43, 44, 44, 45, 46, 46, 46, 46]

# --- Running Total 5B Data (Tiles Sheet) ---
heads_5b = [3, 5, 9, 11, 13, 14, 15, 18, 21, 22, 25, 27, 29, 29, 30, 33, 35, 39, 41, 43, 46, 47, 49, 52, 53, 54, 56, 58, 58, 61, 65, 67, 70, 72, 75, 77, 79, 82, 83, 84, 85, 89, 93, 96, 100, 101, 101, 103, 105, 109, 110, 112, 115, 119, 121, 122, 125, 127, 129, 130, 131, 132, 134, 134, 136, 140, 142, 144, 144, 146, 147, 151, 151, 154, 156, 159, 162, 163, 166, 169, 170, 173, 175, 178, 179, 182, 185, 187, 190, 190, 193, 194, 194, 195, 197, 199, 200, 201, 203, 207]
tails_5b = [1, 3, 3, 5, 7, 10, 13, 14, 15, 18, 19, 21, 23, 27, 30, 31, 33, 33, 35, 37, 38, 41, 43, 44, 47, 50, 52, 54, 58, 59, 59, 61, 62, 64, 65, 67, 69, 70, 73, 76, 79, 79, 79, 80, 80, 83, 87, 89, 91, 91, 94, 96, 97, 97, 99, 102, 103, 105, 107, 110, 113, 116, 118, 122, 124, 124, 126, 128, 132, 134, 137, 137, 141, 142, 144, 145, 146, 149, 150, 151, 154, 155, 157, 158, 161, 162, 163, 165, 166, 170, 171, 174, 178, 181, 183, 185, 188, 191, 193, 193]

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
line_h1, line_t1 = setup_axis(ax1, "Running Total 5A (Tiles Sheet)", max_5a)

# Setup 5B
max_5b = max(max(heads_5b), max(tails_5b))
line_h2, line_t2 = setup_axis(ax2, "Running Total 5B (Tiles Sheet)", max_5b)
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

ani.save('tiles_sheet_5_race.gif', writer=PillowWriter(fps=15))