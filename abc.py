import matplotlib.pyplot as plt
ax = plt.subplot(111, xlabel='x', ylabel='y', title='title')
for item in ([ax.title, ax.xaxis.label, ax.yaxis.label] +
 ax.get_xticklabels() + ax.get_yticklabels()):
 item.set_fontsize(20)