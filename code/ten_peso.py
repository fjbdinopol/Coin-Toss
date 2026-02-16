import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import PillowWriter



# --- Running Total 10A Data ---
heads_10a = [1, 2, 3, 5, 6, 7, 7, 9, 11, 12, 12, 12, 13, 13, 16, 18, 20, 21, 21, 22, 25, 26, 28, 30, 32, 34, 35, 38, 41, 44, 44, 46, 48, 48, 49, 51, 52, 54, 54, 55, 56, 59, 60, 62, 63, 65, 67, 70, 72, 73, 76, 78, 78, 81, 82, 84, 86, 88, 89, 90, 90, 92, 92, 94, 95, 97, 100, 103, 106, 108, 109, 111, 113, 114, 116, 117, 119, 119, 119, 119, 121, 123, 126, 127, 127, 129, 130, 133, 133, 135, 136, 137, 138, 140, 140, 143, 145, 148, 149, 150]
tails_10a = [2, 4, 6, 7, 9, 11, 14, 15, 16, 18, 21, 24, 26, 29, 29, 30, 31, 33, 36, 38, 38, 40, 41, 42, 43, 44, 46, 46, 46, 46, 49, 50, 51, 54, 56, 57, 59, 60, 63, 65, 67, 67, 69, 70, 72, 73, 74, 74, 75, 77, 77, 78, 81, 81, 83, 84, 85, 86, 88, 90, 93, 94, 97, 98, 100, 101, 101, 101, 101, 102, 104, 105, 106, 108, 109, 111, 112, 115, 118, 121, 122, 123, 123, 125, 128, 129, 131, 131, 134, 135, 137, 139, 141, 142, 145, 145, 146, 146, 148, 150]

# --- Running Total 10B Data ---
heads_10b = [1, 2, 3, 4, 5, 7, 8, 10, 11, 12, 13, 16, 18, 20, 20, 23, 24, 26, 28, 30, 32, 34, 35, 36, 38, 41, 41, 44, 46, 47, 48, 50, 52, 53, 54, 55, 57, 57, 59, 60, 62, 64, 66, 68, 69, 70, 72, 73, 74, 77, 79, 81, 82, 83, 85, 86, 87, 90, 91, 91, 92, 93, 94, 96, 97, 98, 100, 101, 103, 103, 103, 105, 107, 109, 112, 113, 116, 118, 121, 122, 124, 126, 127, 128, 130, 131, 133, 134, 136, 138, 140, 142, 144, 145, 147, 149, 151, 152, 154, 155]
tails_10b = [2, 4, 6, 8, 10, 11, 13, 14, 16, 18, 20, 20, 21, 22, 25, 25, 27, 28, 29, 30, 31, 32, 34, 36, 37, 37, 40, 40, 41, 43, 45, 46, 47, 49, 51, 53, 54, 57, 58, 60, 61, 62, 63, 64, 66, 68, 69, 71, 73, 73, 74, 75, 77, 79, 80, 82, 84, 84, 86, 89, 91, 93, 95, 96, 98, 100, 101, 103, 104, 107, 110, 111, 112, 113, 113, 115, 115, 116, 116, 118, 119, 120, 122, 124, 125, 127, 128, 130, 131, 132, 133, 134, 135, 137, 138, 139, 140, 142, 143, 145]

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

# Setup 10A
max_10a = max(max(heads_10a), max(tails_10a))
line_h1, line_t1 = setup_axis(ax1, "Running Total 10A (Sheet 10)", max_10a)

# Setup 10B
max_10b = max(max(heads_10b), max(tails_10b))
line_h2, line_t2 = setup_axis(ax2, "Running Total 10B (Sheet 10)", max_10b)
ax2.set_xlabel('Number of Tosses') # Bottom graph gets X label


def update(frame):
    current_x = trials[:frame]
    
    # Update 10A
    line_h1.set_data(current_x, heads_10a[:frame])
    line_t1.set_data(current_x, tails_10a[:frame])
    
    # Update 10B
    line_h2.set_data(current_x, heads_10b[:frame])
    line_t2.set_data(current_x, tails_10b[:frame])
    
    return line_h1, line_t1, line_h2, line_t2

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=range(1, 101), interval=50, blit=True)

plt.tight_layout()
plt.show()