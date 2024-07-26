import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# Define classes and their colors
classes = ['road', 'sidew.', 'build.', 'wall', 'fence', 'pole', 'tr. light', 'tr. sign',
           'veget.', 'terrain', 'sky', 'person', 'rider', 'car', 'truck', 'bus', 'train', 'm.bike', 'bike', 'n/a.']

palette = [[128, 64, 128], [244, 35, 232], [70, 70, 70], [102, 102, 156],
           [190, 153, 153], [153, 153, 153], [250, 170, 30], [220, 220, 0],
           [107, 142, 35], [152, 251, 152], [70, 130, 180], [220, 20, 60],
           [255, 0, 0], [0, 0, 142], [0, 0, 70], [0, 60, 100],
           [0, 80, 100], [0, 0, 230], [119, 11, 32], [0, 0, 0]]

# Convert the palette to a format that Matplotlib understands (normalize to [0,1])
palette = [[c / 255.0 for c in color] for color in palette]

# Create a figure and axis with higher resolution
fig, ax = plt.subplots(figsize=(16, 2), dpi=300)

# Hide axes
ax.axis('off')

# Create color patches with text inside
for i, (class_name, color) in enumerate(zip(classes, palette)):
    rect = mpatches.Rectangle((i, 0), 1, 1, facecolor=color)
    ax.add_patch(rect)
    ax.text(i + 0.5, 0.5, class_name, ha='center', va='center', fontsize=10, color='white' if sum(color) < 1.5 else 'black', fontweight='bold')

# Set limits and aspect
ax.set_xlim(0, len(classes))
ax.set_ylim(0.3, 0.7)
ax.set_aspect('equal')

# plt.savefig('color_bar.png', bbox_inches='tight') # for debug
plt.savefig('color_bar.pdf', bbox_inches='tight') # for paper
