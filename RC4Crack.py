def decryption(hex_string, key, n):
    # Convert hexadecimal string to binary
    bin_string = bin(int(hex_string, 16))[2:]
    bin_string = bin_string.zfill(len(hex_string) * 4)  # Pad with leading zeros if necessary
    
    # The initial state vector array
    S = [i for i in range(0, 2**n)]

    # Split key into n-bit segments
    key_list = [key[i:i + n] for i in range(0, len(key), n)]

    # Convert key segments to decimal
    for i in range(len(key_list)):
        key_list[i] = int(key_list[i], 2)

    # Convert binary string to n-bit segments
    pt = [bin_string[i:i + n] for i in range(0, len(bin_string), n)]

    # Convert binary segments to decimal
    for i in range(len(pt)):
        pt[i] = int(pt[i], 2)

    # Adjust key_list length to match S
    diff = int(len(S) - len(key_list))
    if diff != 0:
        for i in range(diff):
            key_list.append(key_list[i])

    print(" ")

    # KSA algorithm
    def KSA():
        j = 0
        N = len(S)
        for i in range(N):
            j = (j + S[i] + key_list[i]) % N
            S[i], S[j] = S[j], S[i]
            print(i, " ", end="")
            print(S)
        initial_permutation_array = S
        print(" ")
        print("The initial permutation array is : ", initial_permutation_array)

    print("KSA iterations : ")
    print(" ")
    KSA()
    print(" ")

    # PRGA algorithm
    def do_PRGA():
        N = len(S)
        i = j = 0
        key_stream = []
        for k in range(len(pt)):
            i = (i + 1) % N
            j = (j + S[i]) % N
            S[i], S[j] = S[j], S[i]
            t = (S[i] + S[j]) % N
            key_stream.append(S[t])
        return key_stream

    print("PGRA iterations : ")
    print(" ")
    key_stream = do_PRGA()
    print("Key stream : ", key_stream)
    print(" ")

    # XOR between key stream and plain text
    def do_XOR():
        original_text = []
        for i in range(len(pt)):
            p = key_stream[i] ^ pt[i]
            original_text.append(p)
        return original_text

    original_text = do_XOR()

    # Convert decrypted text to binary form
    decrypted_to_bits = ""
    for i in original_text:
        decrypted_to_bits += '0'*(n-len(bin(i)[2:]))+bin(i)[2:]

    print(" ")
    print("Decrypted text : ", decrypted_to_bits)

# Example usage
hex_string = "04257FD2444807837D439C30B8DC4D68F1A7ED83BCD9DE02A81645C083783E2B49C1418D1079B463716B03ABC5BC74717B664AE765F4C0534CE474B938D83C706A43"  # Example hex string
key = "010101000101010101010100010011110101001001010000010100110100100101010011"  # Example key in binary form
n = 64  # Bit length for splitting

decryption(hex_string, key, n)