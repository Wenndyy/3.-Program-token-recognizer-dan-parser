def TokenRecognizer(kalimat):
    subjek = ['Tina', 'Adi', 'Raka', 'Nina', 'Kris']
    predikat = ['menulis', 'memasak', 'membaca', 'mengukir', 'mendengarkan']
    objek = ['cerita', 'sop', 'surat', 'patung', 'musik']
    keterangan = ['di rumah', 'di dapur', 'di kamar', 'dari kayu', 'di taman']

    FA = {
        'S': set(subjek),
        'P': set(predikat),
        'O': set(objek),
        'K': set(keterangan)
    }
    
    current_state = 'q0'
  
    token_result = []
    for phrase in keterangan + subjek + predikat + objek:
        if len(phrase.split()) > 1:  
            kalimat = kalimat.replace(phrase, phrase.replace(' ', '_'))

    tokens = kalimat.split()

    for token in tokens:
        token = token.replace('_', ' ')
        found = False
        for group, fa in FA.items():
            if token in fa:
                if group == 'S' and current_state == 'q0':
                    current_state = 'q1'
                elif group == 'P' and current_state == 'q1':
                    current_state = 'q2'
                elif group == 'O' and current_state == 'q2':
                    current_state = 'q3'
                elif group == 'K' and current_state == 'q3':
                    current_state = 'q4'

                token_result.append((token, group))
                found = True
                break
        if not found:
            token_result.append((token, "invalid"))

    if current_state in ['q1', 'q2', 'q3', 'q4']:
        return token_result
    else:
        return False

def ParserKalimat(kalimat):
    rules = [
        ['S', 'P', 'O', 'K'],
        ['S', 'P', 'K'],
        ['S', 'P', 'O'],
        ['S', 'P']
    ]

    token_stack = []

    for word, status in kalimat:
        if status == "invalid":
            return False

        token_stack.append(status)
        print("Push:", status, "Stack:", token_stack)

    for rule in rules:
        if token_stack == rule:
            return True
    
    return False


kalimat = input("Masukkan kalimat: ")
token_result = TokenRecognizer(kalimat)

if token_result:
    print("\nTokenization Result:")
    for token, status in token_result:
        print(f"token: {token.replace('_', ' ')}, status: {status}")

    print("\n")

    if ParserKalimat(token_result):

        print("Kalimat valid.")
    else:
        print("Kalimat tidak valid.")
else:
    print("Kalimat tidak valid.")



