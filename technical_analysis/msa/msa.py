import yfinance as yf
import mplfinance as mpf
import matplotlib.pyplot as plt

df = yf.download("AAPL", start="2021-01-01", end="2021-07-01")
df['sam_20'] = df['Close'].rolling(20).mean()
df['sam_50'] = df['Close'].rolling(50).mean()
fig = mpf.figure(style='yahoo',figsize=(7,8))
ax4 = fig.add_subplot(4,1,4)
ax1 = fig.add_subplot(4,1,1, sharex=ax4)
ax2 = fig.add_subplot(4,1,2, sharex=ax4)
ax3 = fig.add_subplot(4,1,3,   sharex=ax4)


ap0 = [
    mpf.make_addplot(df['sam_20'], color='#00FF00', panel=0, title='sma_20', ax=ax1),
    mpf.make_addplot(df['sam_50'], color='#FFa500', panel=1, title='sma_50', ax=ax2)
]

mpf.plot(df,ax=ax3, addplot=ap0, volume=ax4, )
fig.subplots_adjust(hspace=0.2)
ax1.tick_params(labelbottom=False)
ax2.tick_params(labelbottom=False)
ax3.tick_params(labelbottom=False)
ax3.yaxis.set_label_position('left')
ax3.yaxis.tick_left()

plt.show()