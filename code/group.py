import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import PillowWriter


# --- Group 1A Data ---
heads_1a = [0, 1, 1, 2, 3, 4, 5, 5, 6, 6, 7, 7, 8, 9, 9, 10, 11, 12, 12, 13, 14, 15, 15, 15, 16, 17, 18, 19, 20, 21, 22, 22, 23, 24, 25, 25, 25, 26, 27, 27, 27, 27, 28, 28, 28, 29, 30, 31, 32, 32, 33, 33, 33, 34, 34, 34, 35, 35, 36, 37, 37, 37, 37, 38, 38, 39, 40, 41, 41, 41, 41, 42, 42, 42, 42, 43, 43, 44, 45, 45, 46, 47, 47, 48, 49, 50, 50, 51, 52, 53, 54, 55, 55, 56, 57, 57, 58, 58, 59, 59]
tails_1a = [1, 1, 2, 2, 2, 2, 2, 3, 3, 4, 4, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 9, 9, 9, 9, 9, 9, 9, 9, 10, 10, 10, 10, 11, 12, 12, 12, 13, 14, 15, 15, 16, 17, 17, 17, 17, 17, 18, 18, 19, 20, 20, 21, 22, 22, 23, 23, 23, 24, 25, 26, 26, 27, 27, 27, 27, 28, 29, 30, 30, 31, 32, 33, 33, 34, 34, 34, 35, 35, 35, 36, 36, 36, 36, 37, 37, 37, 37, 37, 37, 38, 38, 38, 39, 39, 40, 40, 41]

# --- Group 1B Data ---
heads_1b = [1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 5, 5, 6, 6, 7, 8, 8, 8, 8, 8, 8, 9, 9, 10, 11, 12, 13, 13, 14, 15, 15, 16, 16, 16, 16, 17, 17, 18, 18, 19, 20, 21, 21, 21, 21, 21, 21, 22, 22, 22, 23, 23, 23, 24, 24, 25, 25, 25, 26, 26, 27, 27, 27, 27, 27, 27, 27, 28, 28, 29, 29, 30, 31, 32, 33, 33, 34, 34, 34, 34, 34, 34, 35, 36, 37, 38, 39, 39, 40, 40, 40, 41, 41, 41, 41, 41, 41, 42, 42, 43]
tails_1b = [0, 0, 1, 1, 2, 3, 3, 4, 4, 5, 6, 7, 7, 8, 8, 8, 9, 10, 11, 12, 13, 13, 14, 14, 14, 14, 14, 15, 15, 15, 16, 16, 17, 18, 19, 19, 20, 20, 21, 21, 21, 21, 22, 23, 24, 25, 26, 26, 27, 28, 28, 29, 30, 30, 31, 31, 32, 33, 33, 34, 34, 35, 36, 37, 38, 39, 40, 40, 41, 41, 42, 42, 42, 42, 42, 43, 43, 44, 45, 46, 47, 48, 48, 48, 48, 48, 48, 49, 49, 50, 51, 51, 52, 53, 54, 55, 56, 56, 57, 57]

# --- Combined Data (1A + 1B) ---
heads_comb = [1, 3, 3, 5, 6, 7, 9, 9, 11, 11, 12, 12, 14, 15, 16, 18, 19, 20, 20, 21, 22, 24, 24, 25, 27, 29, 31, 32, 34, 36, 37, 38, 39, 40, 41, 42, 42, 44, 45, 46, 47, 48, 49, 49, 49, 50, 51, 53, 54, 54, 56, 56, 56, 58, 58, 59, 60, 60, 62, 63, 64, 64, 64, 65, 65, 66, 67, 69, 69, 70, 70, 72, 73, 74, 75, 76, 77, 78, 79, 79, 80, 81, 82, 84, 86, 88, 89, 90, 92, 93, 94, 96, 96, 97, 98, 98, 99, 100, 101, 102]
tails_comb = [1, 1, 3, 3, 4, 5, 5, 7, 7, 9, 10, 12, 12, 13, 14, 14, 15, 16, 18, 19, 20, 20, 22, 23, 23, 23, 23, 24, 24, 24, 25, 26, 27, 28, 29, 30, 32, 32, 33, 34, 35, 36, 37, 39, 41, 42, 43, 43, 44, 46, 46, 48, 50, 50, 52, 53, 54, 56, 56, 57, 58, 60, 62, 63, 65, 66, 67, 67, 69, 70, 72, 72, 73, 74, 75, 76, 77, 78, 79, 81, 82, 83, 84, 84, 84, 84, 85, 86, 86, 87, 88, 88, 90, 91, 92, 94, 95, 96, 97, 98]

# Create trial numbers (1 to 100)
trials = list(range(1, 101))


fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 12), sharex=True)

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
line_h1, line_t1 = setup_axis(ax1, "Running Total 1A", max_1a)

# Setup 1B
max_1b = max(max(heads_1b), max(tails_1b))
line_h2, line_t2 = setup_axis(ax2, "Running Total 1B", max_1b)

# Setup Combined
max_comb = max(max(heads_comb), max(tails_comb))
line_h3, line_t3 = setup_axis(ax3, "Combined Total (A + B)", max_comb)
ax3.set_xlabel('Number of Tosses') # Only bottom graph needs X label


def update(frame):
    # Determine the slice of data to show (up to current frame)
    current_x = trials[:frame]
    
    # Update 1A
    line_h1.set_data(current_x, heads_1a[:frame])
    line_t1.set_data(current_x, tails_1a[:frame])
    
    # Update 1B
    line_h2.set_data(current_x, heads_1b[:frame])
    line_t2.set_data(current_x, tails_1b[:frame])
    
    # Update Combined
    line_h3.set_data(current_x, heads_comb[:frame])
    line_t3.set_data(current_x, tails_comb[:frame])
    
    return line_h1, line_t1, line_h2, line_t2, line_h3, line_t3

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=range(1, 101), interval=50, blit=True)

plt.tight_layout()
plt.show()