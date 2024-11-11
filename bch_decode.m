function original_message_str_array = bch_decode(codeword_array)

    % Parametry BCH
    n = 15;  % Długość kodu
    k = 7;   % Długość danych
    dec = comm.BCHDecoder(n, k);

    % Dekodowanie wszystkich kodów z codeword_array
    num_codes = length(codeword_array);
    original_message_str_array = cell(num_codes, 1);

    for i = 1:num_codes
        % Konwersja i dekodowanie
        num = textscan(codeword_array{i}, '%f', 'Delimiter', ',');
        num = logical(cell2mat(num)');
        original_message = dec(num');
        original_message_str_array{i} = strjoin(arrayfun(@num2str, double(original_message'), 'UniformOutput', false), ', ');
    end
end

