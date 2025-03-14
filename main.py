

# from api_request import search_pubmed, fetch_article_details
# from filter_papers import filter_authors
# from output import save_to_csv

# def main():
#     query = input("Enter the topic to search on PubMed: ").strip()

#     pubmed_ids = search_pubmed(query, max_results=20)
#     if not pubmed_ids:
#         print("❌ No results found!")
#         return

#     filtered_results = []
    
#     for pubmed_id in pubmed_ids:
#         print(f"🔍 Fetching details for PubMed ID: {pubmed_id}")
#         article_details = fetch_article_details(pubmed_id)
#         if not article_details:
#             continue

#         authors = filter_authors(article_details)
#         for author in authors:
#             filtered_results.append((pubmed_id, author))

#     if filtered_results:
#         save_to_csv(filtered_results)
#         print("✅ Data saved to `filtered_papers.csv`.")
#     else:
#         print("❌ No biotech/pharma affiliations found.")
#         save_to_csv([])  # Create an empty CSV

# if __name__ == "__main__":
#     main()


# from api_request import search_pubmed, fetch_article_details
# from filter_papers import filter_authors
# from output import save_to_csv

# def main():
#     query = input("Enter the topic to search on PubMed: ").strip()

#     pubmed_ids = search_pubmed(query, max_results=20)
#     if not pubmed_ids:
#         print("❌ No results found!")
#         return

#     filtered_results = []

#     for pubmed_id in pubmed_ids:
#         print(f"🔍 Fetching details for PubMed ID: {pubmed_id}")
#         article_details = fetch_article_details(pubmed_id)
#         if not article_details:
#             continue

#         authors = filter_authors(article_details)
#         for author in authors:
#             filtered_results.append((
#                 pubmed_id,
#                 author["name"],
#                 author["company"],
#                 author["email"] if author["email"] else "No email",
#                 author["title"]
#             ))

#     if filtered_results:
#         save_to_csv(filtered_results)
#         print("✅ Data saved to `filtered_papers.csv`.")
#     else:
#         print("❌ No biotech/pharma affiliations found.")
#         save_to_csv([])

# if __name__ == "__main__":
#     main()


from api_request import search_pubmed, fetch_article_details
from filter_papers import filter_authors
from output import save_to_csv

def main():
    query = input("Enter the topic to search on PubMed: ").strip()

    pubmed_ids = search_pubmed(query, max_results=20)
    if not pubmed_ids:
        print("❌ No results found!")
        return

    filtered_results = []
    
    for pubmed_id in pubmed_ids:
        print(f"🔍 Fetching details for PubMed ID: {pubmed_id}")
        article_details = fetch_article_details(pubmed_id)
        if not article_details:
            continue

        authors = filter_authors(article_details)
        for author in authors:
            filtered_results.append((
                pubmed_id,
                article_details["title"],
                article_details["publication_date"],
                author["name"],
                author["company"],
                author["email"]
            ))

    if filtered_results:
        save_to_csv(filtered_results)
        print("✅ Data saved to `filtered_papers.csv`.")
    else:
        print("❌ No biotech/pharma affiliations found.")
        save_to_csv([])  # Create an empty CSV

if __name__ == "__main__":
    main()
