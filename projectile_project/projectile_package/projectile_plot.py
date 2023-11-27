def plot_xy(t, x, y, vx, vy):
    
    fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, 1, sharex=True, figsize=(8, 10))

    ax1.plot(t, x)
    ax1.set_ylabel("x (m)")

    ax2.plot(t, y)
    ax2.set_ylabel("y (m)")

    ax3.plot(t, vx)
    ax3.set_ylabel("x Velocity (m/s)")

    ax4.plot(t, vy)
    ax4.set_ylabel("y Velocity (m/s)")
    ax4.set_xlabel("t (s)")
