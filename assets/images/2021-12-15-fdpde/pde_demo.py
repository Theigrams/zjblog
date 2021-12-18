# %%
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import os
from PIL import Image
# %%


class WaveEquation2D:
    """
    对二维情况下的波动方程进行模拟
    使用第一类齐次边界条件
    """

    def __init__(self, Lx, Ly, Lt, N, K):
        """
        设定网格范围和划分个数
        """
        self.U = np.zeros((K+1, N+1, N+1))
        self.N = N
        self.K = K
        self.Lt = Lt
        self.Lx = Lx
        self.Ly = Ly
        self.dx = Lx/N
        self.dy = Ly/N
        self.dt = T/K
        self.rx = (self.dt/self.dx)**2
        self.ry = (self.dt/self.dy)**2
        self.X = np.arange(N+1) * self.dx
        self.Y = np.arange(N+1) * self.dy
        self.T = np.arange(K+1) * self.dt

    def set_u0(self):
        """
        定义 t=0 时刻的初值函数
        """
        Fx = np.sin(np.pi * self.X / self.Lx)
        Fy = np.sin(np.pi * self.Y / self.Ly)
        self.U[0, :, :] = np.outer(Fx, Fy)

    def set_u1(self):
        """
        通过 u0 的 Laplace 算子计算 u1
        """
        Fx = np.sin(np.pi * self.X / self.Lx)
        Fy = np.sin(np.pi * self.Y / self.Ly)
        DeltaU = -(np.pi/self.Lx)**2 * np.outer(Fx, Fy) - \
            (np.pi/self.Ly)**2 * np.outer(Fx, Fy)
        self.U[1, :, :] = self.U[0, :, :] + self.dt**2 / 2*DeltaU

    def simulation(self):
        """
        仿真模拟
        """
        # 计算 u0
        self.set_u0()
        # 计算 u1
        self.set_u1()
        rx = self.rx
        ry = self.ry
        # 从 t=2 的时刻开始迭代更新
        for n in range(1, self.K):
            #  边界处的值由边界条件确定, 我们只更新内部
            for i in range(1, self.N):
                for j in range(1, self.N):
                    self.U[n+1, i, j] = 2*(1-rx-ry)*self.U[n, i, j]
                    self.U[n+1, i, j] -= self.U[n-1, i, j]
                    self.U[n+1, i, j] += rx * \
                        (self.U[n, i+1, j]+self.U[n, i-1, j])
                    self.U[n+1, i, j] += ry * \
                        (self.U[n, i, j+1]+self.U[n, i, j-1])
            # 更新边界条件
            self.U[n+1, [0, -1], :] = 0
            self.U[n+1, :, [0, -1]] = 0

    def animate(self):
        """
        通过动画演示, 保存为 gif 动图
        """
        if not os.path.exists("Figure"):
            os.makedirs("Figure")
        fig = plt.figure(2)
        ax = fig.add_subplot(111, projection='3d')
        X, Y = np.meshgrid(self.X, self.Y)
        imgs = []
        # 隔 4 次计算保存一次图
        for n in range(0, self.K+1, 4):
            t = self.T[n]
            ax.plot_surface(
                X, Y, self.U[n, :, :], cmap='rainbow', linewidth=2, antialiased=False)
            ax.set_xlim3d(0, self.Lx)
            ax.set_ylim3d(0, self.Ly)
            ax.set_zlim3d(-1.5, 1.5)
            ax.set_xlabel("x")
            ax.set_ylabel("y")
            ax.set_zlabel("U")
            ax.text(1, 1, 1, "T = {:.2f}s".format(t),
                    size=plt.rcParams["axes.titlesize"],
                    ha="center", transform=ax.transAxes, )
            plt.savefig("Figure/"+str(n), dpi=300)
            print("Save figure in Figure/"+str(n)+".png")
            img = Image.open("Figure/"+str(n)+'.png')
            imgs.append(img)
            ax.cla()
        img.save('wave.gif', save_all=True, append_images=imgs, duration=0.1)

    def evaluate(self):
        """
        评估与真实函数的误差
        """
        Fx = np.sin(np.pi * self.X / self.Lx)
        Fy = np.sin(np.pi * self.Y / self.Ly)
        Fu = np.outer(Fx, Fy)
        c = np.pi*np.sqrt(1/self.Lx**2+1/self.Ly**2)
        Error = []
        for n in range(self.K+1):
            t = PDE.T[n]
            Ut = Fu*np.cos(c*t)
            err = np.linalg.norm(Ut-self.U[n, :, :])
            Error.append(err)
            # print(err)
        self.Err = Error
        plt.figure(1)
        plt.plot(self.Err)
        plt.savefig("Error.png", dpi=300)


# %%
if __name__ == "__main__":
    Lx = 2
    Ly = 2
    T = 2
    N = 30
    K = 200
    PDE = WaveEquation2D(Lx, Ly, T, N, K)
    PDE.simulation()
    print(PDE.rx)
    print(PDE.U.shape)
    PDE.evaluate()
    # PDE.animate()