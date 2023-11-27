def calculate_acceleration_y(v, k=0.035, mass=1.0, gravity=-9.81):

    force_gravity = mass*gravity
    force_air = -sign(v)*k*v**2
    total_force = force_gravity + force_air
    ay = total_force/mass
    
    return ay

def calculate_acceleration_x(v, k=0.035, mass=1.0):
    
    force_air = -sign(v)*k*v**2
    ax = force_air/mass
    
    return ax


def update_state(t, x, v, a, dt=0.1):
    distance_moved = v*dt + (1/2)*a*(dt**2)
    v += a*dt
    t += dt

    x += distance_moved
    
    return t, x, v


def flying_mass(x0, y0, vx0, vy0, k=0.035, mass=1.0, dt=0.1):

    # Fixed input values
    start_vx0 = vx0 # m/s
    start_vy0 = vy0 # m/s
    gravity = -9.81 # m/s2

    # Initial values for our parameters
    distance_moved_x = 0
    distance_moved_y = 0
    x = x0
    y = y0
    vx = start_vx0
    vy = start_vy0
    t = 0.0

    # Create empty lists which we will update
    x_pos = []
    y_pos = []
    x_vel = []
    y_vel = []
    time = []

    # Keep looping while the object is still falling
    while y > 0:
        # Evaluate the state of the system - start by calculating the total force on the object
        ax = calculate_acceleration_x(vx, k=k, mass=mass)
        ay = calculate_acceleration_y(vy, k=k, mass=mass)

        # Append values to list and then update
        x_pos.append(x)
        y_pos.append(y)
        x_vel.append(vx)
        y_vel.append(vy)
        time.append(t)

        # Update the state for time, height and velocity
        t, x, vx = update_state(t, x, vx, ax, dt=dt)
        t, y, vy = update_state(t, y, vy, ay, dt=dt)
    
    return time, x_pos, y_pos, x_vel, y_vel
