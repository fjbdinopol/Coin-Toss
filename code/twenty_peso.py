import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import PillowWriter



# --- Running Total Data (Sheet 20) ---
heads_20 = [0, 1, 4, 7, 9, 11, 11, 13, 14, 16, 18, 19, 21, 23, 24, 25, 26, 26, 27, 28, 31, 31, 32, 32, 33, 34, 36, 38, 39, 39, 41, 42, 42, 43, 44, 46, 48, 49, 50, 50, 52, 54, 57, 58, 58, 60, 61, 63, 63, 65, 67, 69, 71, 73, 74, 75, 78, 81, 82, 83, 85, 87, 88, 89, 91, 92, 93, 93, 95, 97, 98, 99, 100, 101, 102, 104, 104, 104, 106, 107, 109, 111, 112, 112, 114, 116, 118, 119, 120, 121, 122, 125, 128, 130, 132, 135, 136, 138, 140, 142]
tails_20 = [3, 5, 5, 5, 6, 7, 10, 11, 13, 14, 15, 17, 18, 19, 21, 23, 25, 28, 30, 32, 32, 35, 37, 40, 42, 44, 45, 46, 48, 51, 52, 54, 57, 59, 61, 62, 63, 65, 67, 70, 71, 72, 72, 74, 77, 78, 80, 81, 84, 85, 86, 87, 88, 89, 91, 93, 93, 93, 95, 97, 98, 99, 101, 103, 104, 106, 108, 111, 112, 113, 115, 117, 119, 121, 123, 124, 127, 130, 131, 133, 134, 135, 137, 140, 141, 142, 143, 145, 147, 149, 151, 151, 151, 152, 153, 153, 155, 156, 157, 158]

# Create trial numbers (1 to 100)
trials = list(range(1, 101))


fig, ax = plt.subplots(figsize=(10, 6))

# Determine max Y value for scaling
max_y = max(max(heads_20), max(tails_20))

# Setup the axis
ax.set_title("Running Total: 20 Peso Coin (Sheet 20)", fontsize=14, fontweight='bold')
ax.set_xlabel('Number of Tosses')
ax.set_ylabel('Cumulative Count')
ax.set_xlim(0, 100)
ax.set_ylim(0, max_y * 1.1)
ax.grid(True, alpha=0.3)

# Initialize empty lines
line_h, = ax.plot([], [], label='Heads', color='blue', linewidth=2)
line_t, = ax.plot([], [], label='Tails', color='red', linewidth=2)
ax.legend(loc='upper left')

# Text box for live stats
stats_text = ax.text(0.02, 0.85, '', transform=ax.transAxes, 
                     bbox=dict(boxstyle="round", fc="white", ec="gray", alpha=0.8))


def update(frame):
    # Slice data up to current frame
    current_x = trials[:frame]
    current_heads = heads_20[:frame]
    current_tails = tails_20[:frame]
    
    # Update lines
    line_h.set_data(current_x, current_heads)
    line_t.set_data(current_x, current_tails)
    
    # Update stats text
    if frame > 0:
        h_val = current_heads[-1]
        t_val = current_tails[-1]
        stats_text.set_text(f'Tosses: {frame}\nHeads: {h_val}\nTails: {t_val}')
    
    return line_h, line_t, stats_text

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=range(1, 101), interval=50, blit=True)

plt.tight_layout()
plt.show()