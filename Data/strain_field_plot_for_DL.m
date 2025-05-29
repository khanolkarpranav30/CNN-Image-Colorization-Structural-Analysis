% Clear everything
clc; clear; close all;

% Get a list of files
files = dir('data_*');

% INstnatiates some variables
strain = {};
strain11 = {};
strain22 = {};
strain12 = {};
defects = {};

for j=1:1:length(files)
    
    strain_field=load([files(j).name '/' 'strain_field.dat']);% strain data
    defect_field=load([files(j).name '/' 'defects.dat']);
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

    % Zero out the defects
    in_defect = zeros(size(x));
    for i=1:1:length(defect_field)
        in_defect = ((y - defect_field(i, 2)).^2 + (x - defect_field(i, 1)).^2 ) < defect_field(i, 3)^2 + in_defect;
    end

    E00 = ones(size(E11));
    E00(in_defect) = 0;
    E11(in_defect) = 0;
    E22(in_defect) = 0;
    E12(in_defect) = 0;
    
    E(:, :, 1) = E11;
    E(:, :, 2) = E22;
    E(:, :, 3) = E12;
    
    strain{j} = E;
    strain11{j} = E11;
    strain22{j} = E22;
    strain12{j} = E12;
    defects{j} = E00;
end

save('data.mat', 'strain', 'strain11', 'strain12', 'strain22', 'defects');
