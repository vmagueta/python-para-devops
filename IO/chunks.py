def process_chunks(chunk_size=3):
    """Processa entrada em blocos"""
    chunk = []
    line_count = 0

    try:
        while True:
            line = input()
            chunk.append(line)
            line_count += 1

            if len(chunk) >= chunk_size:
                print(f"=== Chunk de {len(chunk)} linhas ===")
                for item in chunk:
                    print(f"  > {item}")
                    chunk = []

    except EOFError:
        if chunk:  # Ultimo chunk parcial
            print(f"=== Último chunk com {len(chunk)} linhas ===")

process_chunks()
