import numpy as np
import matplotlib.pyplot as plt
with open("settings.txt", "r") as settings:
    tmp = [float(i) for i in settings.read().split("\n")]
    print(tmp)


data_array = np.loadtxt("data.txt", dtype=int)

print(data_array)
time_array = []
voltage_array = tmp[0]*data_array*1.7
for i in range(len(voltage_array)):
    time_array.append(i*tmp[1])

fig, ax = plt.subplots(figsize = (8, 5), dpi = 150)
ax.plot(time_array, voltage_array, "m", linewidth = '2.0', marker = 'o', markevery = 30,color = 'blue', markersize = '7.0')
ax.minorticks_on()
ax.set_title("График напряжения U(B) от времени t(c)")
ax.set_xlabel("Время, t(c)")
ax.set_ylabel("Напряжение, U(B)")
ax.grid(which = 'major', linewidth = 0.5, color = 'red')
ax.grid(which = 'minor', linestyle = '--', linewidth = 0.5, color = 'k')
ax.plot(label = 'Напряжение от времени')
ax.tick_params(which = 'major', length = 5, width = 1)
ax.tick_params(which = 'minor', length = 4, width = 0.5)

plt.figtext(0.3, 0.345, "Время заряда 4.21")
plt.figtext(0.3, 0.29, "Время разряда 5,62 с")
plt.legend(["U,(B)"])
fig.set_figwidth(12)
fig.savefig("kar.png")
#fig.figlegend()
plt.show()