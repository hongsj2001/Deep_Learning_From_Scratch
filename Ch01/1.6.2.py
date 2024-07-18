#1.6.2 pyplot의 기능
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,6,0.1) #0부터 6까지 0.1간격으로 생성 (x축)
y1 = np.sin(x) #sin 그래프 생성 (y축)
y2 = np.cos(x) #cos 그래프 생성 (y축)
plt.plot(x,y1, label = "sin") #함수 표시
plt.plot(x,y2, linestyle= "--", label = "cos") #cos함수는 점선으로 표시
plt.xlabel("x") #x축 이름
plt.ylabel("y") #y축 이름
plt.title("sin & cos") #제목

plt.legend() #범례 추가 (라인 구분)
plt.show()