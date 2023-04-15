# Teste da função strip
nome1 = "   André" # Utilizar lstrip
nome2 = "Taciana    " # Utilizar rstrip
nome3 = "    Eduardo     " # Utilizar strip
nome4 = "  Rafael                    " # Utilizar strip
print("Nomes sem a função strip:" + "\n" + nome1 + "\n" + nome2 + "\n" + nome3 + "\n" + nome4)
print("\nUso da função strip:" + "\n\t" + nome1.lstrip() + " (lstrip)" + "\n\t" + nome2.rstrip() + " (rstrip)" + "\n\t" + nome3.strip() + " (strip)" + "\n\t" + nome4.strip() + " (strip)")
