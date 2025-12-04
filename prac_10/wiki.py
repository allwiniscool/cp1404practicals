import wikipedia

def main():
    print("Wikipedia Page Search")
    title = input("Enter page title: ").strip()

    while title != "":
        try:
            page = wikipedia.page(title, auto_suggest=False)

            print(f"{page.title}")
            if len(page.summary) >= 2000:
                print(f"{page.summary}")
            else:
                print(f"{page.summary[:60]} ...")
            print(f"{page.url}")
        except wikipedia.DisambiguationError as title:
            print("We need a more specific title. Try one of the following, or a new search:")
            print("(BeautifulSoup warning)")
            print(title.options[:5])

        except wikipedia.PageError as title:
            print(f"'{title}'")

        print()
        title = input("Enter a page title: ").strip()

    print("Thank you.")



main()