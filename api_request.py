
# from Bio import Entrez
# import xml.etree.ElementTree as ET

# # Replace with your email
# Entrez.email = "nandinim9391@gmail.com"

# def search_pubmed(query, max_results=20):
#     """Search PubMed for articles matching the query and return a list of PubMed IDs."""
#     handle = Entrez.esearch(db="pubmed", term=query, retmax=max_results)
#     record = Entrez.read(handle)
#     handle.close()
#     return record.get("IdList", [])

# def fetch_article_details(pubmed_id):
#     """Fetch article details from PubMed given a PubMed ID."""
#     handle = Entrez.efetch(db="pubmed", id=pubmed_id, retmode="xml")
#     data = handle.read()
#     handle.close()

#     # Parse XML
#     root = ET.fromstring(data)
#     article_info = {}

#     # Extract title
#     title_elem = root.find(".//ArticleTitle")
#     article_info["title"] = title_elem.text if title_elem is not None else "No title available"

#     # Extract author names and affiliations
#     authors = []
#     for author in root.findall(".//Author"):
#         name_elem = author.find("LastName")
#         initials_elem = author.find("ForeName")
#         full_name = f"{name_elem.text} {initials_elem.text}" if name_elem is not None and initials_elem is not None else None

#         affiliation_elem = author.find(".//Affiliation")
#         affiliation = affiliation_elem.text if affiliation_elem is not None else "No affiliation"

#         if full_name:
#             authors.append({"name": full_name, "affiliation": affiliation})

#     article_info["authors"] = authors
#     return article_info


# from Bio import Entrez
# import xml.etree.ElementTree as ET
# import re

# Entrez.email = "nandinim9391@gmail.com"

# def search_pubmed(query, max_results=20):
#     """Search PubMed for articles matching the query and return a list of PubMed IDs."""
#     handle = Entrez.esearch(db="pubmed", term=query, retmax=max_results)
#     print("qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq",handle)
#     record = Entrez.read(handle)
#     handle.close()
#     return record.get("IdList", [])

# def fetch_article_details(pubmed_id):
#     """Fetch article details from PubMed given a PubMed ID."""
#     handle = Entrez.efetch(db="pubmed", id=pubmed_id, retmode="xml")
#     data = handle.read()
#     handle.close()

#     root = ET.fromstring(data)
#     article_info = {"title": "No title available", "authors": []}

#     # Extract title
#     title_elem = root.find(".//ArticleTitle")
#     if title_elem is not None:
#         article_info["title"] = title_elem.text

#     # Extract authors
#     for author in root.findall(".//Author"):
#         name_elem = author.find("LastName")
#         initials_elem = author.find("ForeName")
#         full_name = f"{name_elem.text} {initials_elem.text}" if name_elem is not None and initials_elem is not None else None

#         affiliation_elem = author.find(".//Affiliation")
#         affiliation = affiliation_elem.text if affiliation_elem is not None else "No affiliation"

#         # Extract email using regex
#         email = None
#         email_match = re.search(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", affiliation)
#         if email_match:
#             email = email_match.group(0)

#         # Extract company name from affiliation (basic heuristic)
#         company_name = "No company"
#         relevant_keywords = ["biotech", "pharma", "biopharmaceutical", "biotechnology", "pharmaceutical"]
#         for keyword in relevant_keywords:
#             if keyword.lower() in affiliation.lower():
#                 company_name = affiliation
#                 break

#         if full_name:
#             article_info["authors"].append({
#                 "name": full_name,
#                 "affiliation": affiliation,
#                 "email": email,
#                 "company": company_name
#             })

#     return article_info


from Bio import Entrez
import xml.etree.ElementTree as ET

# Replace with your email
Entrez.email = "nandinim9391@gmail.com"

def search_pubmed(query, max_results=20):
    """Search PubMed for articles matching the query and return a list of PubMed IDs."""
    handle = Entrez.esearch(db="pubmed", term=query, retmax=max_results)
    record = Entrez.read(handle)
    handle.close()
    return record.get("IdList", [])

def fetch_article_details(pubmed_id):
    """Fetch article details from PubMed given a PubMed ID."""
    handle = Entrez.efetch(db="pubmed", id=pubmed_id, retmode="xml")
    data = handle.read()
    handle.close()

    # Parse XML
    root = ET.fromstring(data)
    article_info = {}

    # Extract title
    title_elem = root.find(".//ArticleTitle")
    article_info["title"] = title_elem.text if title_elem is not None else "No title available"

    # Extract publication date
    pub_date_elem = root.find(".//PubDate")
    if pub_date_elem is not None:
        year_elem = pub_date_elem.find("Year")
        month_elem = pub_date_elem.find("Month")
        day_elem = pub_date_elem.find("Day")
        pub_date = f"{year_elem.text}-{month_elem.text}-{day_elem.text}" if year_elem is not None and month_elem is not None and day_elem is not None else "No date available"
    else:
        pub_date = "No date available"

    article_info["publication_date"] = pub_date

    # Extract author names, affiliations, emails
    authors = []
    for author in root.findall(".//Author"):
        name_elem = author.find("LastName")
        initials_elem = author.find("ForeName")
        full_name = f"{name_elem.text} {initials_elem.text}" if name_elem is not None and initials_elem is not None else None

        affiliation_elem = author.find(".//Affiliation")
        affiliation = affiliation_elem.text if affiliation_elem is not None else "No affiliation"

        email_elem = author.find(".//AffiliationInfo/Identifier")
        email = email_elem.text if email_elem is not None else "No email"

        if full_name:
            authors.append({
                "name": full_name,
                "company": affiliation,
                "email": email
            })

    article_info["authors"] = authors
    return article_info
