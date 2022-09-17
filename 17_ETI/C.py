while True:
    vowel = str(input()).strip().lower()
    if vowel == '':
        break
    sample = str(input()).strip().lower()

    v_count = 0
    for char in sample:
        if char in vowel:
            v_count += 1

    print(v_count)