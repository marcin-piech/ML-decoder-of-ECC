clc;
clear;

% Parameters for BCH encoding
n = 15;  % Length of the codeword
k = 7;   % Length of the data
t = 2;   % Number of correctable errors

% Create BCH encoder and decoder objects
enc = comm.BCHEncoder(n, k);
dec = comm.BCHDecoder(n, k);

% 1) Generate 2^k messages
num_messages = 2^k;  % Total number of messages
messages = dec2bin(0:num_messages-1) - '0'; % Convert to binary matrix
disp('Generated messages:');
disp(messages(3, :)); % Display the third generated message for confirmation

% 2) Encoding all messages
encoded_messages = zeros(num_messages, n); % Preallocate for encoded messages
for i = 1:num_messages
    encoded_messages(i, :) = enc(messages(i, :)'); % Encode each message
end

% Prepare data for CSV
data = table('Size', [num_messages, 2], ...
    'VariableTypes', {'string', 'string'}, ...
    'VariableNames', {'Message', 'Encoded_Message'});

% Fill the table with messages and encoded messages
for i = 1:num_messages
    % Convert messages and encoded messages to strings
    data.Message(i) = string(strrep(num2str(messages(i, :)), ' ', '')); % Remove spaces
    data.Encoded_Message(i) = string(strrep(num2str(encoded_messages(i, :)), ' ', '')); % Remove spaces
end

% Write the table to a CSV file
writetable(data, 'encoded_messages.csv');

disp('Data written to encoded_messages.csv');
