import matlab.engine
import numpy as np
import random
import csv
import pandas as pd
import itertools

eng = matlab.engine.start_matlab()
Eb_N0_test = [0, 1, 2, 3, 4, 5, 6, 7]
# Definicja kodu binarnego jako ciągu
awgn_sign_codeword_binary = '1.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0'

# # Wywołanie funkcji bch_decode w Matlabie z Pythonem
# original_message_str = eng.bch_decode(awgn_sign_codeword_binary)
# original_message_list = [f"{float(bit)}" for bit in original_message_str]
#
# # Dołączenie elementów do ciągu z przecinkami
# formatted_message_str = ", ".join(original_message_list)
# # Wyświetlenie wyników
# print("Original message:", formatted_message_str)

for elem in Eb_N0_test:
    # Wczytanie pliku CSV
    file_path = f"output/output_{elem}.csv"
    df = pd.read_csv(file_path)

    # Definicja nazw kolumn
    codeword_column = f"awgn_sign_codeword_binary_{elem}"
    mlp_column = f"mlp_denoised_{elem}"
    cnn_column = f"cnn_denoised"

    # Pobieranie danych z kolumn jako listy
    codeword_list = df[codeword_column].tolist()
    mlp_denoised_list = df[mlp_column].tolist()
    cnn_denoised_list = df[cnn_column].tolist()

    # Wywołanie funkcji bch_decode dla każdej kolumny
    bch_dec_results = eng.bch_decode(codeword_list)
    mlp_bch_dec_results = eng.bch_decode(mlp_denoised_list)
    cnn_bch_dec_results = eng.bch_decode(cnn_denoised_list)


    # Konwersja wyników na format float z przecinkami
    def format_results(bch_results):
        formatted_results = []
        for message in bch_results:
            # Zamiana każdego bitu w stringu na float z przecinkami
            formatted_message = ", ".join([f"{float(bit)}" for bit in message.split(", ")])
            formatted_results.append(formatted_message)
        return formatted_results


    # Formatowanie wyników
    formatted_bch_dec_results = format_results(bch_dec_results)
    formatted_mlp_bch_dec_results = format_results(mlp_bch_dec_results)
    formatted_cnn_bch_dec_results = format_results(cnn_bch_dec_results)

    # Dodanie nowych kolumn do DataFrame
    df["bch_decoded"] = formatted_bch_dec_results
    df["mlp_bch_decoded"] = formatted_mlp_bch_dec_results
    df["cnn_bch_decoded"] = formatted_cnn_bch_dec_results

    # Zapis do pliku
    df.to_csv(file_path, index=False)
    print(f"Updated file saved: {file_path}")