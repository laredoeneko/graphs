from matplotlib import pyplot as plt 

dev_x= ["2024-2-21","2024-2-26","2024-2-27","2024-2-28","2024-2-29","2024-2-30","2024-2-312","32",33,34,35]

dev_y= [1234,12345,12312,12331,14232,13123,33123,2313,13213,13123,545]

py_dev_y= [12234,132345,132312,121331,164232,163123,373123,28313,153213,513123,5545]

js_dev_y= [456,4566,345,345,345,345,3456,3454,345,675,6757]

plt.plot(dev_x,dev_y, color='b', marker=".", label="noraml" )
plt.plot(dev_x,py_dev_y, color='r', marker=".", linewidth=2, label="PYTHON" )
plt.plot(dev_x,js_dev_y, color='y', marker=".", label="java" )

plt.title("el titilo de la grafica")
plt.xlabel("eje X")


plt.legend("adsfsdfsdf")

plt.grid("True")

plt.show()
