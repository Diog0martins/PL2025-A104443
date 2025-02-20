import re

def main():

    alphabetic_list = set()
    period_dictionary =	{}
    
    regex = r"^([^;]*);\"?((?:[^\"]|\"\")*?)\"?;\d{1,4};(.+);([^;]*);\d{2}(:\d{2}){2};.*?(?:\n|$)"
    
    with open("obras.csv") as file:
        content = file.read()

    matches = re.finditer(regex, content, flags=re.MULTILINE)

    match_count = 0
    for match in matches:
        match_count += 1
        title = match.group(1)  
        period = match.group(3) 
        composer = match.group(4)

        alphabetic_list.add(composer)
        
        if period not in period_dictionary:
            period_dictionary[period] = []
        period_dictionary[period].append(title)

    sorted(alphabetic_list)

    print("\n📜 **Alphabetical List of Composers:**")
    print(", ".join(alphabetic_list)) 

    print("\n" + "=" * 50 + "\n")  

    for period, titles in sorted(period_dictionary.items()):
        print(f"🎼 **Period:** {period}")
        print(f"   📌 Number of Pieces: {len(titles)}")
        
        titles.sort()
        formatted_titles = "\n   - ".join(titles)
        print(f"   🎶 **Pieces:**\n   - {formatted_titles}")

        print("\n" + "-" * 50)
        


if __name__ == '__main__':
        main()