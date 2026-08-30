from pathlib import Path
from docx import Document
from docx.shared import Inches
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

# ============================================================
# CONFIGURATION
# ============================================================

PSEUDOCODE_FILE = Path("m6/pseudo.md")
SCREENSHOT_DIRECTORY = Path("m6")
OUTPUT_FILE = Path("m6/module6_portfolio.docx")
SOURCE_CODE_URL = "https://github.com/frosmear/csc500/blob/main/m6/module6.py"


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def add_hyperlink(paragraph, text, url):
    """Add a clickable hyperlink to a Word paragraph."""

    part = paragraph.part
    r_id = part.relate_to(
        url,
        "http://schemas.openxmlformats.org/officeDocument/2006/relationships/hyperlink",
        is_external=True
    )

    hyperlink = OxmlElement("w:hyperlink")
    hyperlink.set(qn("r:id"), r_id)

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
    """Read the Markdown file and add its contents to the document."""

    with markdown_file.open("r", encoding="utf-8") as file:
        lines = file.readlines()

    for line in lines:
        line = line.rstrip()

        # Preserve blank lines
        if not line:
            document.add_paragraph()
            continue

        # Handle Markdown headings
        if line.startswith("### "):
            document.add_heading(line[4:], level=3)

        elif line.startswith("## "):
            document.add_heading(line[3:], level=2)

        elif line.startswith("# "):
            document.add_heading(line[2:], level=1)

        # Handle Markdown bullet points
        elif line.startswith("- "):
            document.add_paragraph(
                line[2:],
                style="List Bullet"
            )

        # Handle numbered Markdown lists
        elif len(line) > 2 and line[0].isdigit() and ". " in line:
            document.add_paragraph(
                line.split(". ", 1)[1],
                style="List Number"
            )

        else:
            document.add_paragraph(line)


# ============================================================
# CREATE DOCUMENT
# ============================================================

document = Document()

# ------------------------------------------------------------
# PSEUDOCODE
# ------------------------------------------------------------

document.add_heading("Pseudocode", level=1)

if PSEUDOCODE_FILE.exists():
    add_markdown_as_text(document, PSEUDOCODE_FILE)
else:
    document.add_paragraph(
        f"Pseudocode file not found: {PSEUDOCODE_FILE}"
    )


# ------------------------------------------------------------
# SCREENSHOTS
# ------------------------------------------------------------

document.add_heading("Screenshots", level=1)

if SCREENSHOT_DIRECTORY.exists():

    screenshots = sorted(
        SCREENSHOT_DIRECTORY.glob("*.png"),
        key=lambda path: path.name.lower()
    )

    if screenshots:
        for screenshot in screenshots:
            document.add_paragraph(screenshot.name)

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
        f"Screenshot directory not found: {SCREENSHOT_DIRECTORY}"
    )


# ------------------------------------------------------------
# SOURCE CODE
# ------------------------------------------------------------

document.add_heading("Source Code", level=1)

paragraph = document.add_paragraph()

add_hyperlink(
    paragraph,
    "View Source Code",
    SOURCE_CODE_URL
)


# ============================================================
# SAVE DOCUMENT
# ============================================================

document.save(OUTPUT_FILE)

print(f"Created: {OUTPUT_FILE.resolve()}")
