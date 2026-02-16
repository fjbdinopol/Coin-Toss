import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import PillowWriter



# --- Running Total Data (Sheet 2) ---
heads_2 = [0, 1, 1, 2, 3, 3, 4, 4, 5, 6, 7, 7, 7, 7, 8, 8, 8, 9, 10, 10, 11, 12, 12, 13, 14, 14, 15, 15, 15, 15, 16, 16, 17, 18, 19, 19, 19, 20, 21, 22, 22, 23, 23, 23, 24, 24, 24, 25, 25, 26, 27, 28, 29, 29, 29, 29, 30, 31, 32, 32, 33, 34, 34, 34, 34, 34, 35, 35, 35, 36, 37, 38, 38, 39, 39, 40, 41, 42, 43, 43, 43, 44, 44, 44, 45, 45, 45, 45, 46, 47, 48, 49, 49, 49, 49, 50, 51, 52, 53, 54]
tails_2 = [1, 1, 2, 2, 2, 3, 3, 4, 4, 4, 4, 5, 6, 7, 7, 8, 9, 9, 9, 10, 10, 10, 11, 11, 11, 12, 12, 13, 14, 15, 15, 16, 16, 16, 16, 17, 18, 18, 18, 18, 19, 19, 20, 21, 21, 22, 23, 23, 24, 24, 24, 24, 24, 25, 26, 27, 27, 27, 27, 28, 28, 28, 29, 30, 31, 32, 32, 33, 34, 34, 34, 34, 35, 35, 36, 36, 36, 36, 36, 37, 38, 38, 39, 40, 40, 41, 42, 43, 43, 43, 43, 43, 44, 45, 46, 46, 46, 46, 46, 46]

# Create trial numbers (1 to 100)
trials = list(range(1, 101))


fig, ax = plt.subplots(figsize=(10, 6))

# Determine max Y value for scaling
max_y = max(max(heads_2), max(tails_2))

# Setup the axis
ax.set_title("Running Total: 2 Peso Coin (Sheet 2)", fontsize=14, fontweight='bold')
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
    current_heads = heads_2[:frame]
    current_tails = tails_2[:frame]
    
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