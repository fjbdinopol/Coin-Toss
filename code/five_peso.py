import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import PillowWriter



# --- Running Total 5A Data ---
heads_5a = [2, 4, 6, 7, 9, 11, 13, 16, 18, 21, 22, 26, 28, 30, 32, 33, 35, 37, 38, 41, 43, 47, 48, 50, 52, 54, 56, 58, 60, 62, 64, 64, 66, 68, 69, 71, 72, 74, 77, 78, 79, 81, 83, 84, 86, 88, 91, 93, 93, 96, 98, 101, 104, 106, 109, 110, 113, 116, 117, 120, 124, 127, 130, 131, 134, 137, 139, 141, 143, 145, 147, 148, 151, 154, 156, 156, 159, 161, 164, 167, 170, 173, 173, 177, 178, 181, 183, 185, 186, 188, 189, 192, 193, 195, 197, 200, 201, 205, 208, 212]
tails_5a = [2, 4, 6, 9, 11, 13, 15, 16, 18, 19, 22, 22, 24, 26, 28, 31, 33, 35, 38, 39, 41, 41, 44, 46, 48, 50, 52, 54, 56, 58, 60, 64, 66, 68, 71, 73, 76, 78, 79, 82, 85, 87, 89, 92, 94, 96, 97, 99, 103, 104, 106, 107, 108, 110, 111, 114, 115, 116, 119, 120, 120, 121, 122, 125, 126, 127, 129, 131, 133, 135, 137, 140, 141, 142, 144, 148, 149, 151, 152, 153, 154, 155, 159, 159, 162, 163, 165, 167, 170, 172, 175, 176, 179, 181, 183, 184, 187, 187, 188, 188]

# --- Running Total 5B Data ---
heads_5b = [4, 8, 13, 16, 19, 21, 23, 27, 30, 33, 37, 40, 43, 44, 46, 51, 55, 60, 63, 65, 70, 72, 75, 79, 80, 82, 85, 89, 89, 92, 96, 100, 105, 109, 112, 115, 118, 121, 123, 125, 126, 131, 136, 140, 144, 147, 149, 152, 155, 160, 162, 165, 169, 174, 177, 178, 181, 185, 188, 189, 191, 194, 196, 197, 199, 205, 207, 210, 211, 214, 216, 221, 223, 227, 230, 235, 240, 242, 246, 250, 252, 256, 259, 262, 264, 268, 271, 275, 279, 281, 284, 286, 288, 290, 292, 294, 296, 297, 301, 306]
tails_5b = [2, 4, 5, 8, 11, 15, 19, 21, 24, 27, 29, 32, 35, 40, 44, 45, 47, 48, 51, 55, 56, 60, 63, 65, 70, 74, 77, 79, 85, 88, 90, 92, 93, 95, 98, 101, 104, 107, 111, 115, 120, 121, 122, 124, 126, 129, 133, 136, 139, 140, 144, 147, 149, 150, 153, 158, 161, 163, 166, 171, 175, 178, 182, 187, 191, 191, 195, 198, 203, 206, 210, 211, 215, 217, 220, 221, 222, 226, 228, 230, 234, 236, 239, 242, 246, 248, 251, 253, 255, 259, 262, 266, 270, 274, 278, 282, 286, 291, 293, 294]

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
line_h1, line_t1 = setup_axis(ax1, "Running Total 5A (Sheet 5)", max_5a)

# Setup 5B
max_5b = max(max(heads_5b), max(tails_5b))
line_h2, line_t2 = setup_axis(ax2, "Running Total 5B (Sheet 5)", max_5b)
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