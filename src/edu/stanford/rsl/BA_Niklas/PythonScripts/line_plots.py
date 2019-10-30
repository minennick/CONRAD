import csv
import matplotlib.pyplot as plt
import numpy as np

params = {'legend.fontsize': 14,
          'legend.handlelength': 2,
          'axes.labelsize' : 20,
          'axes.labelweight': 'bold'
          }

plt.rcParams.update(params)
font = {'family' : 'normal',
        'weight' : 'bold',
        'size'   : 20}

plt.rc('font', **font)


filegt = 'C:/Reconstruction/CONRAD/src/edu/stanford/rsl/BA_Niklas/DataSheets/line_gt.csv'
filereco = 'C:/Reconstruction/CONRAD/src/edu/stanford/rsl/BA_Niklas/DataSheets/line_reco.csv'
filetrunc = 'C:/Reconstruction/CONRAD/src/edu/stanford/rsl/BA_Niklas/DataSheets/line_trunc.csv'

gt = []
reco = []
trunc = []


with open(filegt) as csv_file:
    reader = csv.reader(csv_file, delimiter=';')

    for index, in reader:
        gt.append(index)

with open(filereco) as csv_file:
    reader = csv.reader(csv_file, delimiter=';')

    for index, in reader:
        reco.append(index)

with open(filetrunc) as csv_file:
    reader = csv.reader(csv_file, delimiter=';')

    for index, in reader:
        trunc.append(index)




gt = np.array(gt)
reco = np.array(reco)
trunc = np.array(trunc)


gt = gt.astype(np.float)
reco = reco.astype(np.float)
trunc = trunc.astype(np.float)

scale = (max(gt) - min(gt)) / (max(trunc) - min(trunc))

trunc = [i * scale for i in trunc]
pixels = np.linspace(0, 128, 128)


plt.plot(pixels, gt,"b-", label="Ground-Truth")
plt.plot(pixels, reco,"r-" ,label="Reconstructed")
plt.plot(pixels, trunc, "y-" ,label="Truncated")
plt.legend()
plt.ylabel("Value")
plt.xlabel("Pixels")
# plt.axis([0, len(error), 0, 1])
# plt.savefig("test.png",bbox_inches='tight')
plt.savefig('C:/Users/Niklas/Documents/Uni/Bachelorarbeit/Tex und Schreibarbeit/bt/pictures_corrected/line_plots.pdf', bbox_inches='tight')
plt.show()