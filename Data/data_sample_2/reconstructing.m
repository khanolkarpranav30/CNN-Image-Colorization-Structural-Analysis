clc
clear
close all
resolution_r=0.01;
resolution_theta=0.01;
[r_field,theta_field]=meshgrid(0:resolution_r:1,0:resolution_theta:2*pi);
[x_zernike,y_zernike]=pol2cart(theta_field,r_field);
reconstructed=zeros(size(x_zernike));
radii=r_field(1,:);
count=1;
coeff_list=load('coeff_list_E11.dat');
for n=0:40
    for m=-1*n:2:n     
        R_mn=0;
        for k=0:(n-abs(m))/2
            R_mn=R_mn+(((-1)^k*factorial(n-k))/(factorial(k)*factorial((n+abs(m))/2-k)*factorial((n-abs(m))/2-k)))*radii.^(n-2*k);
        end
        Zerenike_=ones(size(r_field,1),1)*R_mn;
        if m>=0
            Zerenike_=Zerenike_.*cos(m*theta_field);
        else
            Zerenike_=Zerenike_.*sin(m*theta_field);
        end 
        coeff=coeff_list(count,1);
        reconstructed=reconstructed+coeff*Zerenike_;
        count=count+1;
    end  
end
figure
surface(x_zernike,y_zernike,reconstructed,'edgecolor','none');
m_title=num2str(m);
n_title=num2str(n);
title_=['reconstructed Z_{' n_title '}^{' m_title '}'];
title(title_);
axis equal
colormap jet
colorbar
