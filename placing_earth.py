
import datetime
import math

semi_major_axis_dist = 1.00000261
semi_major_axis_dist_cent = 0.00000562

eccentricity = 0.01671123
eccentricity_cent = -0.00004392

incl_degs = -0.00001531
incl_degs_cent = -0.01294668

mean_long_degs = 100.46457166
mean_long_degs_cent = 35999.37244981

perihelion_long_degs = 102.93768193
perihelion_long_degs_cent = 0.32327364

asc_node_degs = 0.0
asc_node_degs_cent = 0.0

epoch = datetime.datetime(2000, 1, 1, 12)
now = datetime.datetime.now()
time_since_epoch = (now - epoch).days / 36525
#print(time_since_epoch)

semi_major_axis = semi_major_axis_dist + semi_major_axis_dist_cent * time_since_epoch
eccen = eccentricity + eccentricity_cent * time_since_epoch
inclination = incl_degs + incl_degs_cent * time_since_epoch
mean_longitude = mean_long_degs + mean_long_degs_cent * time_since_epoch
long_perihelion = perihelion_long_degs + perihelion_long_degs_cent * time_since_epoch
ascending_node = asc_node_degs + asc_node_degs_cent * time_since_epoch

#print(semi_major_axis)
#print(eccentricity)
#print(inclination)
#print(mean_longitude)
#print(long_perihelion)
#print(ascending_node)

perihelion = perihelion_long_degs - ascending_node
mean_anomaly = mean_longitude - perihelion_long_degs
#print("mean anomaly is" + str(mean_anomaly))
if mean_anomaly < -180:
    mean_anomaly = 0.0 - (mean_anomaly % 180)
if mean_anomaly > 180:
    mean_anomaly = mean_anomaly % 180
#print("mean anomaly is" + str(mean_anomaly))

#print(perihelion)
#print(mean_anomaly)

def kep_eq(e, M):
    delta_M = 0
    delta_E = 0
    E0 = M + math.degrees(e) * math.degrees(math.sin(math.radians(M)))
    #print(abs(E0))
    while abs(delta_E) <= 0.000001:
        print("This loop ran")
        delta_M = M - (E0 - math.degrees(e) * math.sin(E0))
        delta_E = delta_M / (1 - e * math.cos(E0))
        E0 = E0 + delta_E

    return E0

#print(kep_eq(eccen, mean_anomaly))
eccentric_anomaly = kep_eq(eccen, mean_anomaly)

heliocentric_x = semi_major_axis * (math.cos(eccentric_anomaly) - eccen)
heliocentric_y = semi_major_axis * math.sqrt(1 - eccen*eccen) * math.sin(eccentric_anomaly)
heliocentric_z = 0

print(heliocentric_x)
print(heliocentric_y)
print(heliocentric_z)
