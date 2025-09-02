import os
from collections import Counter

def word_counter():
    print("📝 Welcome to the Word Counter Program!")
    print("This program will read a text file and count the words for you.\n")
    
    # Ask user for file name
    filename = input("📂 Enter the filename (with extension, e.g., notes.txt): ")
    
    # Check if file exists
    if not os.path.exists(filename):
        print(f"❌ Oops! File '{filename}' not found. Please check the name and try again.")
        return
    
    try:
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()
            
            if not content.strip():
                print("⚠️ The file is empty. No words to count!")
                return
            
            words = content.split()
            total_words = len(words)
            
            print("\n✅ File successfully read!")
            print(f"📖 Total words in '{filename}': {total_words}")
            
            # Bonus: Show top 5 frequent words
            counter = Counter(words)
            common_words = [word for word, count in counter.items() if count > 1]
            
            if not common_words:
                print("\n✨ No words are repeated in this file!")
            else:
                print("\n🔎 Top 5 most common words:")
                for word, count in counter.most_common(5):
                    if count > 1:
                        print(f"   • {word} → {count} times")
                
    except Exception as e:
        print(f"⚠️ An error occurred while reading the file: {e}")

    print("\n🎉 Thanks for using Word Counter!")

if __name__ == "__main__":
    word_counter()
