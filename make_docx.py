from pathlib import Path
from docx import Document
from docx.shared import Inches
from docx.oxml import OxmlElement
from docx.oxml.ns import qn


# ============================================================
# CONFIGURATION
# ============================================================

CONFIG_FILE = Path("make_docx.cfg")


# ============================================================
# CONFIGURATION LOADING
# ============================================================

def load_config(filename):
    """Load simple key=value configuration file."""

    config = {}

    with filename.open("r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            # Ignore blank lines and comments
            if not line or line.startswith("#"):
                continue

            if "=" not in line:
                continue

            key, value = line.split("=", 1)
            config[key.strip()] = value.strip()

    return config


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def add_hyperlink(paragraph, text, url):
    """Add a clickable hyperlink to a Word paragraph."""

    part = paragraph.part

    relationship_id = part.relate_to(
        url,
        "http://schemas.openxmlformats.org/officeDocument/2006/relationships/hyperlink",
        is_external=True
    )

    hyperlink = OxmlElement("w:hyperlink")
    hyperlink.set(qn("r:id"), relationship_id)

    run = OxmlElement("w:r")
    run_properties = OxmlElement("w:rPr")

    # Blue text
    color = OxmlElement("w:color")
    color.set(qn("w:val"), "0563C1")
    run_properties.append(color)

    # Underline
    underline = OxmlElement("w:u")
    underline.set(qn("w:val"), "single")
    run_properties.append(underline)

    run.append(run_properties)

    text_element = OxmlElement("w:t")
    text_element.text = text
    run.append(text_element)

    hyperlink.append(run)
    paragraph._p.append(hyperlink)


def add_markdown_as_text(document, markdown_file):
    """Read simple Markdown and add it to the document."""

    with markdown_file.open("r", encoding="utf-8") as file:
        lines = file.readlines()

    for line in lines:
        line = line.rstrip()

        if not line:
            document.add_paragraph()
            continue

        # Markdown headings
        if line.startswith("### "):
            document.add_heading(line[4:], level=3)

        elif line.startswith("## "):
            document.add_heading(line[3:], level=2)

        elif line.startswith("# "):
            document.add_heading(line[2:], level=1)

        # Bullet list
        elif line.startswith("- "):
            document.add_paragraph(
                line[2:],
                style="List Bullet"
            )

        # Numbered list
        elif len(line) > 2 and line[0].isdigit() and ". " in line:
            document.add_paragraph(
                line.split(". ", 1)[1],
                style="List Number"
            )

        # Normal paragraph
        else:
            document.add_paragraph(line)


# ============================================================
# MAIN
# ============================================================

def main():

    # --------------------------------------------------------
    # Load configuration
    # --------------------------------------------------------

    if not CONFIG_FILE.exists():
        print(f"ERROR: Configuration file not found: {CONFIG_FILE}")
        return

    config = load_config(CONFIG_FILE)

    required_settings = [
        "assignment_title",
        "student_name",
        "pseudocode_file",
        "screenshot_directory",
        "output_file",
        "source_code_url"
    ]

    for setting in required_settings:
        if setting not in config:
            print(f"ERROR: Missing configuration setting: {setting}")
            return

    assignment_title = config["assignment_title"]
    student_name = config["student_name"]

    pseudocode_file = Path(config["pseudocode_file"])
    screenshot_directory = Path(config["screenshot_directory"])
    output_file = Path(config["output_file"])

    source_code_url = config["source_code_url"]


    # --------------------------------------------------------
    # Create document
    # --------------------------------------------------------

    document = Document()


    # --------------------------------------------------------
    # Title
    # --------------------------------------------------------

    document.add_heading(assignment_title, level=1)

    document.add_paragraph(
        f"Student: {student_name}"
    )


    # --------------------------------------------------------
    # PSEUDOCODE
    # --------------------------------------------------------

    document.add_heading("Pseudocode", level=1)

    if pseudocode_file.exists():
        add_markdown_as_text(
            document,
            pseudocode_file
        )
    else:
        document.add_paragraph(
            f"Pseudocode file not found: {pseudocode_file}"
        )


    # --------------------------------------------------------
    # SCREENSHOTS
    # --------------------------------------------------------

    document.add_heading("Screenshots", level=1)

    if screenshot_directory.exists():

        screenshots = sorted(
            screenshot_directory.glob("*.png"),
            key=lambda path: path.name.lower()
        )

        if screenshots:

            for screenshot in screenshots:

                document.add_paragraph(
                    screenshot.name
                )

                paragraph = document.add_paragraph()
                run = paragraph.add_run()

                run.add_picture(
                    str(screenshot),
                    width=Inches(6.0)
                )

        else:
            document.add_paragraph(
                "No PNG screenshots were found."
            )

    else:
        document.add_paragraph(
            f"Screenshot directory not found: "
            f"{screenshot_directory}"
        )


    # --------------------------------------------------------
    # SOURCE CODE
    # --------------------------------------------------------

    document.add_heading("Source Code", level=1)

    paragraph = document.add_paragraph()

    add_hyperlink(
        paragraph,
        "View Source Code",
        source_code_url
    )


    # --------------------------------------------------------
    # Save document
    # --------------------------------------------------------

    document.save(output_file)

    print(f"Created: {output_file.resolve()}")


if __name__ == "__main__":
    main()
