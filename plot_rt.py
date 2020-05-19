# Libraries
import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pandas as pd
from datetime import datetime, timedelta

# Create figure for plotting
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
xs = []
ys1 = []
ys2 = []

# This function is called periodically from FuncAnimation
def animate(i, xs, ys1, ys2):

    # Read data from csv file
    data = pd.read_csv('data.csv')

    # Last elements of csv file
    x_time = pd.to_datetime(data['updated'].iloc[-1], unit='s', origin='unix') - timedelta(hours=5) # Local time
    x_last = x_time.strftime('%H:%M:%S') # Better time format
    y1_last = data['buy'].iloc[-1]
    y2_last = data['sell'].iloc[-1]

    print(x_last, '\t', y1_last, '\t', y2_last) #Print main elements

    # Append last elements to respective list
    xs.append(x_last)
    ys1.append(y1_last)
    ys2.append(y2_last)

    # Limit x and y lists to 20 items
    xs = xs[-20:]
    ys1 = ys1[-20:]
    ys2 = ys2[-20:]

    # Draw x and y lists
    ax.clear()
    ax.plot(xs, ys1, label='buy')
    ax.plot(xs, ys2, label='sell')
    plt.legend(loc='upper right')

    # Format plot
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title('eth_btc vs time')
    plt.ylabel('eth_btc')

# Set up plot to call animate() function periodically
print("hour", '\t\t', "sell", '\t\t', "buy") #Print main elements
ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys1, ys2), interval=1000)
plt.show()
