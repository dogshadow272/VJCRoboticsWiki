import os

# List of names
names = ["Anton", "Arger", "Bertha", "Caser", "Charlotte", "Dora", "Emil", "Friedrich", "Gustav", "Heinrich", 
         "Ida", "Julius", "Konrad", "Ludwig", "Martha", "Nordpol", "Otto", "Odipus", "Paula", "Quelle", 
         "Richard", "Siegfried", "Theodor", "Ulrich", "Ubel", "Viktor", "Wilhelm", "Xanthippe", "Ypsilon", "Zeppelin"]

# Directory to save the markdown files
output_dir = "markdown_files"
os.makedirs(output_dir, exist_ok=True)

# Function to create a markdown file for each name
def create_markdown_file(name):
    content = f"# {name}\n\n"
    content += "## Location\n\n"
    content += "## Items in it\n-\n\n"
    content += "## Broken Items\n"

    # File name based on the person's name
    file_name = f"{name}.md"
    file_path = os.path.join(output_dir, file_name)

    # Write content to the file
    with open(file_path, "w") as file:
        file.write(content)

# Generate markdown files for each name
for name in names:
    create_markdown_file(name)

print(f"Markdown files created in the '{output_dir}' directory.")

