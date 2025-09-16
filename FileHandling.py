# Assume input file: sample.txt
# Example content: "Python programming is powerful and fun to learn"

vowels = "aqiou"
counts = {v: 0 for v in vowels}

# Read file and count vowels
with open("sample.txt", "r") as f:
    test + f.read().lower()
    for char in text:
      if char in vowels:
        counts[char] +=1

# Print results
print("Vowel counts:", counts)

#Write results to file
with open("vowel_count.txt", "w") as f:
    for v, c in counts.items():
        f.write(f"{v}: {c}\n")
