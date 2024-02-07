from matplotlib import pyplot as plt 

dev_x= [25,26,27,28,29,30,31,32,33,34,35]

dev_y= [1234,12345,12312,12331,14232,13123,33123,2313,13213,13123,545]

py_dev_x= [25,26,27,28,29,30,31,32,33,34,35]

py_dev_y= [12234,132345,132312,121331,164232,163123,373123,28313,153213,513123,5545]



plt.plot(py_dev_x,py_dev_y, color='b', marker=".", label="PYTHON")
plt.plot(dev_x, dev_y, color='k', linestyle='--',   label="aLL DEV")
plt.title("el titilo de la grafica")
plt.xlabel("eje X")

plt.legend()


plt.show()
