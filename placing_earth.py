import datetime

semi_major_axis_dist = 1.00000261
semi_major_axis_dist_cent = .00000562

eccentricity = 0.01621123
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
time_since_epoch = (epoch - now).days
#print(time_since_epoch)

semi_major_axis = semi_major_axis_dist + (semi_major_axis_dist_cent * time_since_epoch)
eccentricity = eccentricity + (eccentricity_cent * time_since_epoch)
inclination = incl_degs + (incl_degs_cent * time_since_epoch)
mean_longitude = mean_long_degs + (mean_long_degs_cent * time_since_epoch)
perihelion = perihelion_long_degs + (perihelion_long_degs_cent * time_since_epoch)
ascending_node = asc_node_degs + (asc_node_degs_cent * time_since_epoch)

print(semi_major_axis)
print(eccentricity)
print(inclination)
print(mean_longitude)
print(perihelion)
print(ascending_node)
