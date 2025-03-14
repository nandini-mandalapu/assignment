

# import csv

# def save_to_csv(filtered_results, filename="filtered_papers.csv"):
#     """Save filtered results to a CSV file."""
#     with open(filename, mode="w", newline="", encoding="utf-8") as file:
#         writer = csv.writer(file)
#         writer.writerow(["PubMed ID", "Author Name"])
#         writer.writerows(filtered_results)
    
#     print(f"📄 Data successfully saved to `{filename}`.")
# import csv

# def save_to_csv(filtered_results, filename="filtered_papers.csv"):
#     """Save filtered results to a CSV file."""
#     with open(filename, mode="w", newline="", encoding="utf-8") as file:
#         writer = csv.writer(file)
#         writer.writerow(["PubMed ID", "Author Name", "Company Name", "Email", "Title"])
#         writer.writerows(filtered_results)

#     print(f"📄 Data successfully saved to `{filename}`.")


import csv

def save_to_csv(filtered_results, filename="filtered_papers.csv"):
    """Save filtered results to a CSV file."""
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["PubMed ID", "Title", "Publication Date", "Author Name", "Company Name", "Email"])
        writer.writerows(filtered_results)
    
    print(f"📄 Data successfully saved to `{filename}`.")
