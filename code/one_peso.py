import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import PillowWriter



# --- Running Total 1A Data ---
heads_1a = [2, 5, 7, 11, 15, 18, 22, 25, 28, 32, 36, 39, 42, 44, 45, 48, 52, 54, 57, 60, 62, 67, 69, 72, 76, 80, 83, 85, 89, 91, 95, 95, 96, 99, 102, 103, 104, 108, 110, 111, 113, 115, 118, 120, 122, 124, 127, 130, 131, 133, 135, 137, 140, 142, 143, 146, 149, 151, 153, 156, 158, 160, 163, 167, 169, 172, 175, 177, 180, 182, 185, 187, 190, 191, 193, 196, 197, 200, 203, 204, 205, 207, 208, 213, 215, 217, 218, 220, 223, 225, 227, 230, 232, 235, 238, 238, 239, 240, 244, 245]
tails_1a = [3, 5, 8, 9, 10, 12, 13, 15, 17, 18, 19, 21, 23, 26, 30, 32, 33, 36, 38, 40, 43, 43, 46, 48, 49, 50, 52, 55, 56, 59, 60, 65, 69, 71, 73, 77, 81, 82, 85, 89, 92, 95, 97, 100, 103, 106, 108, 110, 114, 117, 120, 123, 125, 128, 132, 134, 136, 139, 142, 144, 147, 150, 152, 153, 156, 158, 160, 163, 165, 168, 170, 173, 175, 179, 182, 184, 188, 190, 192, 196, 200, 203, 207, 207, 210, 213, 217, 220, 222, 225, 228, 230, 233, 235, 237, 242, 246, 250, 251, 255]

# --- Running Total 1B Data ---
heads_1b = [3, 5, 10, 14, 17, 19, 22, 25, 30, 32, 35, 38, 43, 47, 51, 53, 56, 60, 63, 66, 69, 74, 75, 78, 83, 86, 91, 91, 94, 98, 101, 105, 107, 112, 115, 118, 120, 123, 126, 130, 133, 136, 138, 140, 143, 147, 148, 151, 153, 156, 160, 162, 165, 169, 173, 177, 181, 184, 189, 190, 193, 195, 198, 201, 203, 207, 209, 211, 213, 216, 219, 223, 225, 228, 231, 233, 237, 240, 244, 246, 249, 251, 252, 257, 259, 264, 267, 268, 272, 274, 277, 281, 284, 284, 286, 288, 289, 292, 295, 297]
tails_1b = [3, 7, 8, 10, 13, 17, 20, 23, 24, 28, 31, 34, 35, 37, 39, 43, 46, 48, 51, 54, 57, 58, 63, 66, 67, 70, 71, 77, 80, 82, 85, 87, 91, 92, 95, 98, 102, 105, 109, 110, 114, 116, 121, 124, 127, 129, 134, 137, 141, 144, 146, 150, 153, 155, 158, 159, 161, 164, 165, 170, 173, 177, 180, 183, 187, 189, 193, 197, 201, 204, 207, 209, 213, 216, 219, 223, 225, 228, 230, 234, 237, 241, 246, 247, 251, 252, 255, 260, 262, 266, 269, 271, 274, 280, 284, 288, 293, 296, 299, 303]

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
line_h1, line_t1 = setup_axis(ax1, "Running Total 1A (Sheet 1)", max_1a)

# Setup 1B
max_1b = max(max(heads_1b), max(tails_1b))
line_h2, line_t2 = setup_axis(ax2, "Running Total 1B (Sheet 1)", max_1b)
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