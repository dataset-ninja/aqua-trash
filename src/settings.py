from typing import Dict, List, Optional, Union

from dataset_tools.templates import (
    AnnotationType,
    Category,
    CVTask,
    Domain,
    Industry,
    License,
    Research,
)

##################################
# * Before uploading to instance #
##################################
PROJECT_NAME: str = "AquaTrash"
PROJECT_NAME_FULL: str = "AquaTrash Dataset"
HIDE_DATASET = False  # set False when 100% sure about repo quality

##################################
# * After uploading to instance ##
##################################
LICENSE: License = License.Custom(
    source_url="https://github.com/Harsh9524/AquaTrash?tab=readme-ov-file#usage"
)
APPLICATIONS: List[Union[Industry, Domain, Research]] = [Industry.Environmental()]
CATEGORY: Category = Category.Environmental()

CV_TASKS: List[CVTask] = [CVTask.ObjectDetection()]
ANNOTATION_TYPES: List[AnnotationType] = [AnnotationType.ObjectDetection()]

RELEASE_DATE: Optional[str] = None  # e.g. "YYYY-MM-DD"
if RELEASE_DATE is None:
    RELEASE_YEAR: int = 2020

HOMEPAGE_URL: str = "https://github.com/Harsh9524/AquaTrash"
# e.g. "https://some.com/dataset/homepage"

PREVIEW_IMAGE_ID: int = 14101962
# This should be filled AFTER uploading images to instance, just ID of any image.

GITHUB_URL: str = "https://github.com/dataset-ninja/aqua-trash"
# URL to GitHub repo on dataset ninja (e.g. "https://github.com/dataset-ninja/some-dataset")

##################################
### * Optional after uploading ###
##################################
DOWNLOAD_ORIGINAL_URL: Optional[Union[str, dict]] = "https://github.com/Harsh9524/AquaTrash"
# Optional link for downloading original dataset (e.g. "https://some.com/dataset/download")

CLASS2COLOR: Optional[Dict[str, List[str]]] = {
    "glass": [230, 25, 75],
    "paper": [60, 180, 75],
    "metal": [255, 225, 25],
    "plastic": [0, 130, 200],
}

# If specific colors for classes are needed, fill this dict (e.g. {"class1": [255, 0, 0], "class2": [0, 255, 0]})

# If you have more than the one paper, put the most relatable link as the first element of the list
# Use dict key to specify name for a button
PAPER: Optional[Union[str, List[str], Dict[str, str]]] = (
    "https://www.sciencedirect.com/science/article/pii/S2666016420300244?via%3Dihub"
)
BLOGPOST: Optional[Union[str, List[str], Dict[str, str]]] = None
REPOSITORY: Optional[Union[str, List[str], Dict[str, str]]] = None

CITATION_URL: Optional[str] = None
AUTHORS: Optional[List[str]] = [
    "Harsh Panwar",
    "P.K. Gupta",
    "Mohammad Khubeb Siddiqui",
    "Ruben Morales-Menendez",
    "Prakhar Bhardwaj",
    "Sudhansh Sharma",
    "Iqbal H. Sarker",
]
AUTHORS_CONTACTS: Optional[List[str]] = [
    "harshpanwar@ieee.org",
    "pkgupta@ieee.org",
    "khubeb@tec.mx",
    "rmm@tec.mx",
    "prakharbhardwaj784@gmail.com",
    "sudhansh0706@gmail.com",
    "iqbal.sarker.cse@gmail.com",
]


ORGANIZATION_NAME: Optional[Union[str, List[str]]] = [
    "Department of Computer Science and Engineering, India",
    "School of Engineering and Sciences, Mexico",
    "Department of Computer Science and Engineering, Bangladesh",
]
ORGANIZATION_URL: Optional[Union[str, List[str]]] = [
    "https://www.cse.iitb.ac.in/",
    "https://maestriasydiplomados.tec.mx/",
    "https://buft.edu.bd/department-of-computer-science-and-engineering",
]

# Set '__PRETEXT__' or '__POSTTEXT__' as a key with string value to add custom text. e.g. SLYTAGSPLIT = {'__POSTTEXT__':'some text}
SLYTAGSPLIT: Optional[Dict[str, Union[List[str], str]]] = None
TAGS: Optional[List[str]] = None


SECTION_EXPLORE_CUSTOM_DATASETS: Optional[List[str]] = None

##################################
###### ? Checks. Do not edit #####
##################################


def check_names():
    fields_before_upload = [PROJECT_NAME]  # PROJECT_NAME_FULL
    if any([field is None for field in fields_before_upload]):
        raise ValueError("Please fill all fields in settings.py before uploading to instance.")


def get_settings():
    if RELEASE_DATE is not None:
        global RELEASE_YEAR
        RELEASE_YEAR = int(RELEASE_DATE.split("-")[0])

    settings = {
        "project_name": PROJECT_NAME,
        "project_name_full": PROJECT_NAME_FULL or PROJECT_NAME,
        "hide_dataset": HIDE_DATASET,
        "license": LICENSE,
        "applications": APPLICATIONS,
        "category": CATEGORY,
        "cv_tasks": CV_TASKS,
        "annotation_types": ANNOTATION_TYPES,
        "release_year": RELEASE_YEAR,
        "homepage_url": HOMEPAGE_URL,
        "preview_image_id": PREVIEW_IMAGE_ID,
        "github_url": GITHUB_URL,
    }

    if any([field is None for field in settings.values()]):
        raise ValueError("Please fill all fields in settings.py after uploading to instance.")

    settings["release_date"] = RELEASE_DATE
    settings["download_original_url"] = DOWNLOAD_ORIGINAL_URL
    settings["class2color"] = CLASS2COLOR
    settings["paper"] = PAPER
    settings["blog"] = BLOGPOST
    settings["repository"] = REPOSITORY
    settings["citation_url"] = CITATION_URL
    settings["authors"] = AUTHORS
    settings["authors_contacts"] = AUTHORS_CONTACTS
    settings["organization_name"] = ORGANIZATION_NAME
    settings["organization_url"] = ORGANIZATION_URL
    settings["slytagsplit"] = SLYTAGSPLIT
    settings["tags"] = TAGS

    settings["explore_datasets"] = SECTION_EXPLORE_CUSTOM_DATASETS

    return settings
