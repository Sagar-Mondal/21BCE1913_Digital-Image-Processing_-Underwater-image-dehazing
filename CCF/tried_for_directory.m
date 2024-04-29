diary('output.txt');
imageDir = '../results/';
imageFiles = dir(fullfile(imageDir, '*.png'));

% Array to store quality values
qualityArray = zeros(1, numel(imageFiles));

% Loop through each image in the directory
for i = 1:numel(imageFiles)
    % Read the image
    im = imread(fullfile(imageDir, imageFiles(i).name));
    % Calculate quality using CCF function and store in the array
    quality = CCF(im);
    qualityArray(i) = quality;
    % Display the file name and quality value
    disp(['Image: ', imageFiles(i).name]);
end

% Calculate the mean quality value
meanQuality = mean(qualityArray);
disp(['Mean Quality: ', num2str(meanQuality)]);

diary off