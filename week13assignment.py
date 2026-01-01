import requests

def fetch_dog_data():
    """Function to get data from API and handle errors."""
    try:
        print("Connecting to internet...")
        response = requests.get("https://random.dog/woof.json", timeout=10)
        response.raise_for_status()
        
        data = response.json()
        return data["url"]
    except Exception as e:
        print(f"Error occurred: {e}")
        return None

def main():
    print("--- Dog Image Finder ---")   
    try:
        count = int(input("How many images"))
    except ValueError:
        print("Please enter a number!")
        return

    images = []
    while len(images) < count:
        link = fetch_dog_data()   
        if link:
             if ".mp4" and ".webm" not in link:
                images.append(link)
                print(f"Found {len(images)} of {count}")

    print("\n--- Your Results ---")
    number = 1
    for url in images:
        print(f"{number}. {url}")
        number = number + 1

    save = input("\nSave to file? (y/n): ")
    if save.lower() == 'y':
        with open("results.txt", "w") as f:
            for url in images:
                f.writelines(url + "\n")
        print("Saved to results.txt")

if __name__ == "__main__":
    main()