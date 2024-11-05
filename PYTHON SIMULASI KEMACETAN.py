import numpy as np
import matplotlib.pyplot as plt

# Parameter simulasi
arrival_rate = 10        # Rata-rata kendaraan masuk per menit
road_capacity = 100      # Kapasitas maksimal jalan
initial_speed = 60       # Kecepatan rata-rata awal kendaraan (km/jam)
speed_reduction_factor = 0.5  # Faktor pengurangan kecepatan per kendaraan
time_steps = 60          # Durasi simulasi dalam menit

# Variabel untuk simulasi
vehicles_on_road = 0
speeds = []
congestion_levels = []
vehicle_counts = []

for t in range(time_steps):
    # Kendaraan baru yang masuk
    new_vehicles = np.random.poisson(arrival_rate)
    vehicles_on_road += new_vehicles

    # Menghitung tingkat kemacetan
    congestion_level = max(0, (vehicles_on_road - road_capacity) / road_capacity)
    congestion_levels.append(congestion_level)

    # Menghitung kecepatan rata-rata
    current_speed = max(0, initial_speed - speed_reduction_factor * vehicles_on_road)
    speeds.append(current_speed)

    # Menyimpan jumlah kendaraan di jalan
    vehicle_counts.append(vehicles_on_road)

    # Memperbarui jumlah kendaraan di jalan
    if vehicles_on_road > road_capacity:
        # Mengurangi kendaraan yang keluar dari jalan
        vehicles_on_road -= np.random.randint(0, int(0.1 * vehicles_on_road))

# Plot hasil simulasi
fig, ax1 = plt.subplots(figsize=(10, 6))

# Plotting speed
ax1.set_xlabel('Waktu (menit)')
ax1.set_ylabel('Kecepatan rata-rata (km/jam)', color='tab:blue')
ax1.plot(speeds, color='tab:blue', label='Kecepatan rata-rata')
ax1.tick_params(axis='y', labelcolor='tab:blue')

# Plotting congestion level on the same axis
ax2 = ax1.twinx()
ax2.set_ylabel('Tingkat kemacetan', color='tab:red')
ax2.plot(congestion_levels, color='tab:red', linestyle='--', label='Tingkat Kemacetan')
ax2.tick_params(axis='y', labelcolor='tab:red')

fig.tight_layout()
plt.title('Simulasi Kemacetan Lalu Lintas')
plt.show()
