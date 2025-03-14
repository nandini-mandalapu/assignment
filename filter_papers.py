
# def filter_authors(article_details):
#     """Filter authors with affiliations related to biotech or pharma."""
#     relevant_keywords = ["biotech", "pharma", "biopharmaceutical", "biotechnology", "pharmaceutical"]
    
#     filtered_authors = []
#     for author in article_details["authors"]:
#         if any(keyword.lower() in author["affiliation"].lower() for keyword in relevant_keywords):
#             filtered_authors.append(author["name"])
    
#     return filtered_authors

# def filter_authors(article_details):
#     """Filter authors with affiliations related to biotech or pharma."""
#     relevant_keywords = ["biotech", "pharma", "biopharmaceutical", "biotechnology", "pharmaceutical"]

#     filtered_authors = []
#     for author in article_details["authors"]:
#         if any(keyword.lower() in author["affiliation"].lower() for keyword in relevant_keywords):
#             filtered_authors.append({
#                 "name": author["name"],
#                 "company": author["company"],
#                 "email": author["email"],
#                 "title": article_details["title"]
#             })

#     return filtered_authors


def filter_authors(article_details):
    """Filter authors with affiliations related to biotech or pharma."""
    relevant_keywords = ["biotech", "pharma", "biopharmaceutical", "biotechnology", "pharmaceutical"]
    
    filtered_authors = []
    for author in article_details["authors"]:
        if any(keyword.lower() in author["company"].lower() for keyword in relevant_keywords):
            filtered_authors.append({
                "name": author["name"],
                "company": author["company"],
                "email": author["email"]
            })
    
    return filtered_authors
