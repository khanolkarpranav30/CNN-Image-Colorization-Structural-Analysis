clc
clear
close all
strain_field=load('strain_field.dat');% strain data
defect_field=load('defects.dat');
x_min=min(strain_field(:,2));
y_min=min(strain_field(:,3));
x_max=max(strain_field(:,2));
y_max=max(strain_field(:,3));
resolution=min([x_max-x_min,y_max-y_min])/100;
[x, y]=meshgrid([x_min:resolution:x_max],[y_min:resolution:y_max]);
E11=griddata(strain_field(:,2),strain_field(:,3),strain_field(:,4),x,y);
E22=griddata(strain_field(:,2),strain_field(:,3),strain_field(:,5),x,y);
E12=griddata(strain_field(:,2),strain_field(:,3),strain_field(:,6),x,y);

% setting up to plot defects
theta=0:0.1:2*pi;
x_defect=(cos(theta)')*defect_field(:,3)'+defect_field(:,1)';
y_defect=(sin(theta)')*defect_field(:,3)'+defect_field(:,2)';

figure
subplot(3,1,1)
surface(x,y,E11,'edgecolor','none');
hold on
fill3(x_defect,y_defect,max(max(E11))*ones(size(x_defect)),'black')
title('E11')
xlabel('X (m)')
ylabel('Y (m)')
axis equal
colorbar
subplot(3,1,2)
surface(x,y,E22,'edgecolor','none');
hold on
fill3(x_defect,y_defect,max(max(E11))*ones(size(x_defect)),'black')
title('E22')
xlabel('X (m)')
ylabel('Y (m)')
axis equal
colorbar
subplot(3,1,3)
surface(x,y,E12,'edgecolor','none');
hold on
fill3(x_defect,y_defect,max(max(E11))*ones(size(x_defect)),'black')
title('E12')
xlabel('X (m)')
ylabel('Y (m)')
axis equal
colorbar

% analyzing the strain field
twoptcorr_area_Zernike
